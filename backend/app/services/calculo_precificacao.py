def calcular_preco_venda(custo: float, margem_lucro: float) -> float:
    if custo < 0:
        raise ValueError("O custo não pode ser negativo.")

    if margem_lucro < 0:
        raise ValueError("A margem de lucro não pode ser negativa.")

    preco = custo + (custo * margem_lucro / 100)
    return round(preco, 2)
