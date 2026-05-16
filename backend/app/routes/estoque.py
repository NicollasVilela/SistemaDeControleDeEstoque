from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Produto

router = APIRouter(prefix="/estoque", tags=["Estoque"])


class AtualizarEstoque(BaseModel):
    quantidade: int


@router.patch("/{produto_id}")
def atualizar_estoque(
    produto_id: int,
    payload: AtualizarEstoque,
    db: Session = Depends(get_db),
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    produto.quantidade = payload.quantidade
    db.commit()
    db.refresh(produto)

    return {
        "message": "Estoque atualizado com sucesso.",
        "produto_id": produto.id,
        "quantidade": produto.quantidade,
    }
