sistema_solar="Mercurio venus Tierra Marte Júpiter Saturno Urano Neptuno Plutón Tierra Mercurio"

planetas=set()

for planeta in sistema_solar.split(" "):

    planetas.add(planeta)

print(planetas)
print(len(planetas))
