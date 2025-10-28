from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from database import Base
import pytz


class Velocidade(Base):
    __tablename__ = "velocidades"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, nullable=False)
    velocidade = Column(Float, nullable=False)
    aceleracao= Column(Float, nullable=False)
    data_captura = Column(DateTime, default=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))
