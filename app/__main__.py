import typer

from app.manage import table_file_to_db, download

app = typer.Typer()
app.command(name='table_file_to_db')(table_file_to_db.app)
app.command(name='download')(download.app)

if __name__ == '__main__':
    app()
