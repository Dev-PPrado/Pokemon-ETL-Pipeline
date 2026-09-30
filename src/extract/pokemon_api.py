import requests
import logging

from config.settings import POKEAPI_URL

logger = logging.getLogger(__name__)

def fetch_pokemon_data(pokemon_id: int) -> dict:

    url = f"{POKEAPI_URL}/pokemon/{pokemon_id}"

    logger.info("Starting extraction | pokemon_id=%s", pokemon_id)

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        logger.info(
            "Extraction successful | pokemon_id=%s | status_code=%s",
            pokemon_id,
            response.status_code
        )

        return response.json()

    except requests.RequestException:

        logger.exception(
            "Extraction failed | pokemon_id=%s",
            pokemon_id
        )

        raise