type ProductCardProps = {
  nome: string;
  categoria: string;
  quantidade: number;
  estoqueMinimo: number;
  precoVenda: number;
};

export function ProductCard({
  nome,
  categoria,
  quantidade,
  estoqueMinimo,
  precoVenda,
}: ProductCardProps) {
  const status = quantidade <= estoqueMinimo ? "Reposição necessária" : "Estoque saudável";

  return (
    <div className="card">
      <h3>{nome}</h3>
      <p>Categoria: {categoria}</p>
      <p>Quantidade: {quantidade}</p>
      <p>Preço de venda: R$ {precoVenda.toFixed(2)}</p>
      <strong>{status}</strong>
    </div>
  );
}
