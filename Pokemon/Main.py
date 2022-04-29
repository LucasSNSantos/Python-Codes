from numpy import correlate
import pandas
pokemons = pandas.read_csv('pokemon.csv', header=None)

pokemons.columns = [
    "ID",
    "Name",
    "Type1",
    "Type2",
    "Total",
    "HP",
    "Attack",
    "Defense"
    "Atk.Speed",
    "Def.Speed",
    "Speed",
    "Generation",
    "Legendary",
    "what"
]

pokemons = pokemons.drop("what",axis=1)
pokemons = pokemons.drop("ID",axis=1)

correlation_matrix =  pokemons.corr()
print(correlation_matrix.columns)

