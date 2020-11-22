import pandas as pd
import matplotlib.pyplot as plt
import json

ecv = pd.read_csv("https://raw.githubusercontent.com/PitchInteractiveInc/tilegrams/master/data/us/electoral-college-votes-by-state.csv", header=None)
gdp = pd.read_csv("https://raw.githubusercontent.com/PitchInteractiveInc/tilegrams/master/data/us/gdp-by-state.csv", header=None)
pop = pd.read_csv("https://raw.githubusercontent.com/PitchInteractiveInc/tilegrams/master/data/us/population-by-state.csv", header=None)

nhpop = pd.read_csv("race_makeup/data/rmf.txt", sep="\t", header = None)

nhpop[2] = nhpop[2].str.rstrip(r'\d%').astype(float)

with open("race_makeup/data/statekey.json") as f:
    info = json.load(f)

states = []
for value in info.values():
    states.append(value["name_short"])

# print(states)
# print(pop[1])


df = pd.DataFrame({
    "State": states,
    "E.C. Votes": ecv[1],
    "GDP": gdp[1],
    "Population": pop[1],
    "N.H.W Percentage": nhpop[2]
})



df.to_csv("race_makeup/data/state_data", index = False)