from sqlalchemy import inspect

from config.database import engine, init_db
from models.pokemon import Pokemon  # noqa: F401


def test_pokemon_table_exists():
    init_db()

    with engine.connect() as connection:
        assert inspect(connection).has_table("pokemons")
