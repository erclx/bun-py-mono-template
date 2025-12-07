from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings

app = FastAPI(title='Bun Py Backend API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'mode': 'web-only'}


@app.get('/items/{item_id}')
def read_item(item_id: int) -> dict[str, int]:
    return {'item_id': item_id}
