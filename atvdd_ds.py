import pandas as pd
import matplotlib.pyplot as plt

dictClubes = {
    'Everton': 380.700,
    'West Ham': 394.000,
    'Aston Villa': 502.000,
    'Leicester': 511.500,
    'Arsenal': 677.000,
    'Manchester United': 708.800,
    'Tottenham': 749.300,
    'Chelsea': 866.700,
    'Liverpool': 870.000,
    'Manchester City': 999.999
}

serie1 = pd.Series(dictClubes)

#print(serie1)

clubes = list(dictClubes.keys())

#print(clubes)

milhoes = list(dictClubes.values())

#print(milhoes)

#serie2 = pd.Series(milhoes, index=clubes)

plt.bar(clubes, milhoes)

plt.show()