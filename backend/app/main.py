from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routes import estoque, previsoes, produtos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Estoque Inteligente API",
    description="API para controle de estoque, precificação e sugestão de reposição.",
    version="1.0.0",
)

app.include_router(produtos.router)
app.include_router(estoque.router)
app.include_router(previsoes.router)


@app.get("/")
def health_check():
    return {"status": "online", "message": "API Estoque Inteligente funcionando"}
