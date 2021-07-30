print("This program is able to covert your weight in other planets of the solar system")
print("\nThe formula is:")
planet = input("Type the name of the planet:")
grv = 9.807
planets = {"Saturn": 10.44, "Earth": 9.807, "Mercury": 3.7, "Venus": 8.87, "Mars": 3.711, "Jupiter": 24.79, "Uranus": 8.69, "Neptune": 11.15, "Pluto": 0.62}
end = ""
while end != "quit":
    planet_grv = planets.get(planet,"Sorry, that's not valid information.")
    weight = float(input("Type your weight:"))
    result = (weight/grv) * planet_grv
    print(round(result,2))

