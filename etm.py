import numpy as np

# Define the element-mineral conversion matrix
element_mineral_matrix = np.array([
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1]
])

# Define the element composition of the sample
sample_element_composition = np.array([50, 30, 20, 10, 40])

# Perform singular value decomposition (SVD)
U, s, V = np.linalg.svd(element_mineral_matrix)

# Compute the mineral composition of the sample using SVD
mineral_composition = np.dot(np.dot(sample_element_composition, V.T), np.linalg.inv(np.diag(s)))

# Print the results
print("Mineral composition of the sample:")
print(mineral_composition)