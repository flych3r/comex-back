from pathlib import Path

import pandas as pd
import typer
from sqlalchemy import create_engine, text

from app.dependencies.config import SETTINGS
from app.manage.table import create_serial_id


def app(
    file_path: Path = typer.Argument(
        ..., help='Caminho para o arquivo csv de organogramas.'
    ),
    table_name: str = typer.Argument(
        ..., help='Nome da tabela no banco de dados'
    ),
    xlsx: bool = typer.Option(
        False, help='Se o arquivo é do tipo excel. Caso contrário assume tipo csv'
    ),
    sep: str = typer.Argument(
        ';', help='Separador do arquivo csv'
    ),
    append: bool = typer.Option(
        False, help='Se deve concatenar ou substituir a tabelas existentes.'
    ),
    chunksize: int = typer.Argument(
        10**6, help='Tamanho do chunk em linhas.'
    )
):
    """
    Insere o arquivo na db da API.

    Se usar --append, concatena a tabelas existentes, caso contrario substitui.
    """
    conn = create_engine(SETTINGS.database_url)

    if not append:
        conn.execute(text(f'DROP TABLE IF EXISTS {table_name};'))

    if xlsx:
        data = pd.read_excel(file_path)
        data.to_sql(table_name, con=conn, index=False, if_exists='append')
    else:
        total = sum(1 for _ in open(file_path, 'rb'))
        with typer.progressbar(
            length=total, label=f'Inserindo arquivos csv de {file_path}.'
        ) as progress:
            with pd.read_csv(file_path, sep=sep, chunksize=chunksize) as reader:
                for chunk in reader:
                    chunk.to_sql(table_name, con=conn, index=False, if_exists='append')
                    progress.update(chunk.shape[0])
            progress.update(chunksize)

    create_serial_id(table_name, conn)
    conn.dispose()

    typer.echo(f'Tabela {table_name} criada.')
