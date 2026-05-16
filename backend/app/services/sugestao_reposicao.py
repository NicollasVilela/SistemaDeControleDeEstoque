def calcular_sugestao_reposicao(quantidade: int, estoque_minimo: int) -> dict:
    precisa_repor = quantidade <= estoque_minimo

    quantidade_sugerida = 0
    if precisa_repor:
        quantidade_sugerida = max((estoque_minimo * 2) - quantidade, 1)

    return {
        "precisa_repor": precisa_repor,
        "quantidade_sugerida": quantidade_sugerida,
    }
