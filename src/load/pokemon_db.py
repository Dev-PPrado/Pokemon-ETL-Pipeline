from config.database import SessionLocal
from models.pokemon import Pokemon
from schemas.pokemon import PokemonSchema

import logging

logger = logging.getLogger(__name__)


def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:

    logger.info(
        "Starting database load | pokemon=%s",
        pokemon_schema.name
    )

    try:

        with SessionLocal() as db:

            db_pokemon = Pokemon(
                name=pokemon_schema.name,
                type=pokemon_schema.type
            )

            db.add(db_pokemon)

            logger.info(
                "Pokemon added to session | pokemon=%s",
                pokemon_schema.name
            )

            db.commit()

            db.refresh(db_pokemon)

            logger.info(
                "Database load successful | database_id=%s",
                db_pokemon.id
            )

            return db_pokemon

    except Exception:

        logger.exception(
            "Database load failed | pokemon=%s",
            pokemon_schema.name
        )

        raise