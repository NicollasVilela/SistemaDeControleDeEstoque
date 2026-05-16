import { useEffect, useState } from "react";
import { ProductCard } from "../components/ProductCard";
import { api } from "../services/api";

type Produto = {
  id: number;
  nome: string;
  categoria: string;
  quantidade: number;
  estoque_minimo: number;
  preco_venda: number;
};

export function Dashboard() {
  const [produtos, setProdutos] = useState<Produto[]>([]);

  useEffect(() => {
    api.get("/produtos").then((response) => {
      setProdutos(response.data);
    });
  }, []);

  return (
    <main>
      <h1>Estoque Inteligente</h1>
      <p>Dashboard de produtos, estoque e precificação.</p>

      <section className="grid">
        {produtos.map((produto) => (
          <ProductCard
            key={produto.id}
            nome={produto.nome}
            categoria={produto.categoria}
            quantidade={produto.quantidade}
            estoqueMinimo={produto.estoque_minimo}
            precoVenda={produto.preco_venda}
          />
        ))}
      </section>
    </main>
  );
}
