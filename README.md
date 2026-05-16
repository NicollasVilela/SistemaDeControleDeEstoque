# Sistema de Controle de Estoque Inteligente

Projeto full stack para controle de estoque, cálculo de precificação e sugestão automática de reposição de produtos.

Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- React.js
- Docker

Funcionalidades

- Cadastro e listagem de produtos
- Controle de quantidade em estoque
- Sugestão automática de reposição
- Cálculo de preço de venda com base em margem de lucro
- Endpoints REST documentados automaticamente pelo Swagger

Como executar

```bash
docker compose up --build
```

Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```
