from pyboy import PyBoy

pyboy = PyBoy("PokemonRed.gb")
with open("has_pokedex.state", "rb") as f:
    pyboy.load_state(f)
while pyboy.tick():
    pass
pyboy.stop()
