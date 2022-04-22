import matplotlib.pyplot as plt

x = list(range(1, 9))
y = notas_matematica
plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
