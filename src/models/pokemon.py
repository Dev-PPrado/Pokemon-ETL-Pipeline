from sqlalchemy import Column, Integer, String, DateTime, func
from config.database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

    created_at = Column(
        DateTime,
        default=func.now()
    )