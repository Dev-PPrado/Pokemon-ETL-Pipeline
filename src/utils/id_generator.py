import logging
import random

logger = logging.getLogger(__name__)


def generate_pokemon_id(min_id: int = 1,max_id: int = 1025) -> int:

    pokemon_id = random.randint(min_id, max_id)

    logger.info("Pokemon ID generated | id=%s",pokemon_id)

    return pokemon_id