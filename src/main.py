import logging
import time

from config.logging import setup_logging
from extract.pokemon_api import fetch_pokemon_data
from transform.pokemon import transform_pokemon
from schemas.pokemon import PokemonSchema
from load.pokemon_db import add_pokemon_to_db
from utils.id_generator import generate_pokemon_id


setup_logging()

logger = logging.getLogger(__name__)


def main():

    logger.info("Starting Pokemon ETL pipeline")

    while True:

        logger.info("========== STARTING ITERATION ==========")

        try:
            pokemon_id = generate_pokemon_id()

            raw_data = fetch_pokemon_data(pokemon_id)

            transformed_data = transform_pokemon(raw_data)

            pokemon_schema = PokemonSchema(**transformed_data)

            pokemon = add_pokemon_to_db(pokemon_schema)

            logger.info(
                "Pokemon loaded successfully | id=%s | name=%s",
                pokemon.id,
                pokemon.name
            )

        except Exception:
            logger.exception("Pokemon pipeline execution failed")

        logger.info("Waiting 5 seconds before next execution")

        time.sleep(5)

        logger.info("5 seconds elapsed")


if __name__ == "__main__":
    main()

