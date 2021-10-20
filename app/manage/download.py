import requests
import pandas as pd
from datetime import datetime
import ssl
from tqdm.auto import tqdm
from pathlib import Path
import typer


ssl._create_default_https_context = ssl._create_unverified_context


def app(
    out_path: Path = typer.Argument(
        'f_comex.csv', help='Caminho para o arquivo csv de organogramas.'
    ),
):
    """
    Baixa os dados de Comercio Exterior dos ultimos 3 anos.
    """
    col_mapping = {
        'CO_ANO': 'ANO',
        'CO_MES': 'MES',
        'CO_NCM': 'COD_NCM',
        'CO_UNID': 'COD_UNIDADE',
        'CO_PAIS': 'COD_PAIS',
        'SG_UF_NCM': 'SG_UF',
        'CO_VIA': 'COD_VIA',
        'CO_URF': 'COD_URF',
        'QT_ESTAT': 'VL_QUANTIDADE',
        'KG_LIQUIDO': 'VL_PESO_KG',
        'VL_FOB': 'VL_FOB',
    }

    def fetch_data_last_3_year(movimentacao):
        if movimentacao not in ['EXP', 'IMP']:
            raise ValueError('movimentacao must be one of EXP or IMP')
        ano = datetime.now().year
        ncm_url = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/{}_{}.csv'
        while not requests.head(
            ncm_url.format(movimentacao, ano), verify=False
        ).ok:
            ano -= 1

        with typer.progressbar(
            length=3, label=f'Downloading {movimentacao} data'
        ) as progress:
            years = []
            for a in range(ano, ano - 3, -1):
                years.append(pd.read_csv(ncm_url.format(movimentacao, a), sep=';'))
                progress.update(1)

        data = pd.concat(years)
        del years
        if len(set(col_mapping.keys()) & set(data.columns)) != len(col_mapping.keys()):
            raise AttributeError('data does not has expected columns')
        data = data.rename(columns=col_mapping)
        data['COD_NCM'] = data['COD_NCM'].apply(lambda x: f'{x:08d}')
        data['COD_URF'] = data['COD_URF'].apply(lambda x: f'{x:07d}')
        data['COD_PAIS'] = data['COD_PAIS'].apply(lambda x: f'{x:03d}')
        return data[col_mapping.values()]

    exp = fetch_data_last_3_year('EXP')
    exp['MOVIMENTACAO'] = 'Exportação'
    exp.head()

    imp = fetch_data_last_3_year('IMP')
    imp['MOVIMENTACAO'] = 'Importação'
    imp.head()

    typer.echo(f'Saving data to {out_path}')
    exp.append(imp).to_csv(out_path, sep=';', index=False)
