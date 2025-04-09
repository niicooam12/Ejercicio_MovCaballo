from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Movimiento(Base):
    __tablename__ = 'movimientos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    paso = Column(Integer, nullable=False)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

# Configuración de la base de datos
DATABASE_URL = "sqlite:///movimientos.db"  # Cambia esto si usas otra base de datos
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)