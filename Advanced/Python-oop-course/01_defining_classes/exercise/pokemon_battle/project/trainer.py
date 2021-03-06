class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon_info in self.pokemon:
            if pokemon_name == pokemon_info.name:
                self.pokemon.remove(pokemon_info)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        info = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}"
        for p in self.pokemon:
            info += f"\n- {p.pokemon_details()}"
        return info
