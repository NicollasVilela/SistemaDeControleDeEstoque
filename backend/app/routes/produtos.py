from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Produto
from app.services.calculo_precificacao import calcular_preco_venda

router = APIRouter(prefix="/produtos", tags=["Produtos"])


class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    quantidade: int
    estoque_minimo: int
    custo: float
    margem_lucro: float = 30.0


class ProdutoResponse(ProdutoCreate):
    id: int
    preco_venda: float


@router.post("/", response_model=ProdutoResponse)
def criar_produto(payload: ProdutoCreate, db: Session = Depends(get_db)):
    produto = Produto(**payload.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)

    return {
        **payload.model_dump(),
        "id": produto.id,
        "preco_venda": calcular_preco_venda(produto.custo, produto.margem_lucro),
    }


@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()

    return [
        {
            "id": produto.id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "estoque_minimo": produto.estoque_minimo,
            "custo": produto.custo,
            "margem_lucro": produto.margem_lucro,
            "preco_venda": calcular_preco_venda(produto.custo, produto.margem_lucro),
        }
        for produto in produtos
    ]


@router.get("/{produto_id}")
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    return produto
