🚗 Projeto de Monitoramento de Velocidades Veiculares

Sistema completo que coleta, armazena e exibe em tempo real as velocidades capturadas por sensores (reais ou simulados).
O projeto integra FastAPI (backend), SQLite (banco de dados) e Streamlit (painel visual), criando uma solução simples, funcional e didática para monitoramento de tráfego.

🧠 Visão Geral

O sistema é dividido em 3 partes principais:

API (FastAPI)

Recebe os dados de velocidade enviados pelos sensores (ou simulador).

Armazena as informações em um banco SQLite.

Permite visualizar os registros via rotas /dados/ e documentação automática em /docs.

Painel (Streamlit)

Lê os dados do banco e exibe gráficos e métricas em tempo real.

Mostra a evolução das velocidades, médias, máximas e mínimas.

Simulador (Python ou ESP32)

Gera dados aleatórios ou reais (via sensores piezo).

Envia periodicamente as velocidades para a API.

⚙️ Tecnologias Utilizadas

FastAPI
 — API moderna e rápida.

SQLite
 — banco de dados leve e local.

SQLAlchemy
 — ORM para manipulação dos dados.

Streamlit
 — painel interativo e visual.

Plotly
 — geração de gráficos dinâmicos.

Requests
 — envio de dados do simulador.

 🧩 Estrutura do Projeto:
 📂 Projeto-Velocidades
 ├── main.py           # API principal (FastAPI)
 ├── database.py       # Configuração do banco SQLite
 ├── models.py         # Modelo de dados (tabela velocidades)
 ├── simulador.py      # Simulador de sensores
 ├── dashboard.py      # Painel Streamlit
 ├── velocidades.db    # Banco de dados gerado automaticamente
 └── textRequirements.txt # Dependências e instruções

Como Rodar o Projeto:

1️⃣ Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Linux/Mac)

2️⃣ Instale as dependências
pip install fastapi uvicorn sqlalchemy pydantic streamlit plotly requests pytz

3️⃣ Inicie a API
uvicorn main:app --reload
Acesse em: http://IP-DA-MAQUINA
Teste as rotas em: http://IP-DA-MAQUINA/docs
