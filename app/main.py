from fastapi import FastAPI

from app import __version__
from app.routers import d_sh2, d_via, f_comex
from fastapi_pagination import add_pagination

app = FastAPI(
    title='Comex',
    description='API REST para acessar dados de Comércio Exterior.',
    version=__version__,
)
app.include_router(d_sh2.router, prefix='/api')
app.include_router(d_via.router, prefix='/api')
app.include_router(f_comex.router, prefix='/api')
add_pagination(app)


@app.get('/')
def root():
    """Root endpoint to check status."""
    return {'status': 'ok'}
