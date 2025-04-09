from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Juego(Base):
    __tablename__ = 'juegos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    ruta = Column(String, nullable=False)

    def __repr__(self):
        return f"<Juego(nombre='{self.nombre}', descripcion='{self.descripcion}', ruta='{self.ruta}')>"

# Configuración de la base de datos
DATABASE_URL = "sqlite:///juegos.db"  # Base de datos SQLite
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos iniciales
juegos = [
    Juego(nombre="Movimiento del Caballo", descripcion="Juego para resolver el movimiento del caballo en un tablero de ajedrez.", ruta="Caballo/lanzador.py"),
    Juego(nombre="N Reinas", descripcion="Juego para resolver el problema de las N reinas en un tablero de ajedrez.", ruta="Reina/lanzador.py"),
    Juego(nombre="Torres de Hanoi", descripcion="Juego para resolver el problema de las Torres de Hanoi.", ruta="Hanoi/lanzador.py")
]

# Insertar datos si la tabla está vacía
if not session.query(Juego).first():
    session.add_all(juegos)
    session.commit()

print("Base de datos creada y juegos añadidos.")