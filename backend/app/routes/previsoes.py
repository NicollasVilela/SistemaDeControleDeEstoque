from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Produto
from app.services.sugestao_reposicao import calcular_sugestao_reposicao

router = APIRouter(prefix="/previsoes", tags=["Previsões"])


@router.get("/reposicao")
def listar_sugestoes_reposicao(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()

    sugestoes = []
    for produto in produtos:
        analise = calcular_sugestao_reposicao(
            quantidade=produto.quantidade,
            estoque_minimo=produto.estoque_minimo,
        )

        sugestoes.append(
            {
                "produto_id": produto.id,
                "nome": produto.nome,
                "quantidade_atual": produto.quantidade,
                "estoque_minimo": produto.estoque_minimo,
                **analise,
            }
        )

    return sugestoes
