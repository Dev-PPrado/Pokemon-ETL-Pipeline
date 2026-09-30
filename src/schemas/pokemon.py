from pydantic import BaseModel

class PokemonSchema(Basemodel):
    name: str
    type: str