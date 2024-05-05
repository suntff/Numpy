import numpy as np
x = np.array([2, 2, 2, 3, 3, 3, 5])
unique_species, species_counts = np.unique(x, return_counts=True)
print((unique_species, species_counts))