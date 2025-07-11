import numpy as np

tabela1 = np.array([3, 6.1, 4.5])
w = np.array([[1.1, 3.5, 16.2],
             [38.1, 7, 5.5],
             [8.5, 3, 5]])

resultado = np.dot(tabela1, w)

print(resultado)
