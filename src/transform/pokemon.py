import logging

logger = logging.getLogger(__name__)


def transform_pokemon(data: dict) -> dict:

    logger.info("Starting transformation | pokemon=%s", data.get("name"))

    types = ", ".join(
        pokemon_type["type"]["name"]
        for pokemon_type in data["types"]
    )

    transformed_data = {
        "name": data["name"],
        "type": types
    }

    logger.info(
        "Transformation successful | pokemon=%s | type=%s",
        data["name"],
        types
    )

    return transformed_data