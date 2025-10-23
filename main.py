from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Velocidade

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Velocidade - Projeto UPX")

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dados/")
def receber_dado(sensor_id: int, velocidade: float, db: Session = Depends(get_db)):
    dado = Velocidade(sensor_id=sensor_id, velocidade=velocidade)
    db.add(dado)
    db.commit()
    db.refresh(dado)
    return {"status": "OK", "id": dado.id}

@app.get("/dados/")
def listar_dados(db: Session = Depends(get_db)):
    dados = db.query(Velocidade).all()
    return dados

@app.get("/")
def home():
    return {"mensagem": "API de velocidade funcionando! Acesse /docs para ver os endpoints."}
