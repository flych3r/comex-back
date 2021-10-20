from typing import List, Tuple

import typer
from sqlalchemy import text
from sqlalchemy.engine.base import Engine


def create_index(table: str, columns: List[Tuple[str, ]], conn: Engine):
    """
    Creates index on database for table in columns combination.

    Parameters
    ----------
    table : str
        name of the table
    columns : list or tuple of string
        names of the columns
    conn : Engine
        connected engine
    """
    for cols in columns:
        idx_names = '_'.join(cols)
        col_names = ','.join(cols)
        conn.execute(f'CREATE INDEX idx_{table}_{idx_names} ON {table}({col_names});')
        typer.echo(f'Indice idx_{table}_{idx_names} criado.')


def create_serial_id(table: str, conn: Engine) -> Tuple[str, str]:
    """
    Creates id primary key on table.

    Parameters
    ----------
    table : str
        name of the table
    conn : Engine
        connected engine

    Returns
    -------
    str
        names of columns
    """
    columns = [
        (c[0], c[1]) for c in
        conn.execute(text(f"""
            SELECT column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{table}';
        """))
    ]

    col_names = [c[0] for c in columns]
    col_types = [c[1] for c in columns]

    col_names_str = ', '.join(col_names)
    col_names_types_str = ', '.join(f'{n} {t}' for n, t in zip(col_names, col_types))

    typer.echo(f'Criação de chave primária id (auto incremento) na tabela {table}')
    conn.execute(text(f"""
        ALTER TABLE {table} ADD COLUMN id SERIAL PRIMARY KEY;
    """))

    return col_names_str, col_names_types_str
