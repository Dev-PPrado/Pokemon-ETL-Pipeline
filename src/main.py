from extract.pokemon_api import fetch_pokemon_data
from transform.pokemon import transform_pokemon
from schemas.pokemon import PokemonSchema
from load.pokemon_db import add_pokemon_to_db
from utils.id_generator import generate_pokemon_id

import logging
from config.database import init_db
from config.logging import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

def main():

    init_db()

    logger.info("Starting Pokemon ETL pipeline")
    
    pokemon_id = generate_pokemon_id()

    logger.info("Generated Pokemon ID: %s", pokemon_id)

    raw_data = fetch_pokemon_data(pokemon_id)

    transformed_data = transform_pokemon(raw_data)

    pokemon_schema = PokemonSchema(**transformed_data)

    pokemon = add_pokemon_to_db(pokemon_schema)

    logger.info(
        "Pokemon loaded successfully: id=%s name=%s",
        pokemon.id,
        pokemon.name
    )

    logger.info("Pokemon ETL pipeline finished successfully")

if __name__ == "__main__":
    main()

