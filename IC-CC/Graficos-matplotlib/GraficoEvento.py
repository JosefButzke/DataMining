import matplotlib.pyplot as plt
from tkinter import filedialog,Tk
import pandas as pd
import time

root = Tk()
root.fileName = filedialog.askopenfilename(filetypes = (("howCode files", "*.csv"), ("All files", "*.*")))
root.destroy()
df = pd.read_csv(root.fileName, delimiter=',')


tipoAEEJ = (df['Tipo_AEEJ']).tolist()

axisX = []
axisY = []

for i in range(len(tipoAEEJ)):
    if tipoAEEJ[i] is 3:
        axisX.append(df['Codigo_AEEJ'][i])
        axisY.append(df['Codigo_expressao'][i])

combinacoesSingulares = []
for i in range(len(axisX)):
    combinacoesSingulares.append([axisX[i], axisY[i]])

combinacoesSingulares = sorted([list(x) for x in set(tuple(x) for x in combinacoesSingulares)])

plt.scatter(axisX, axisY)

for i in range(len(combinacoesSingulares)):
    repetiu = 0
    for j in range(len(axisX)):
        if combinacoesSingulares[i] == [axisX[j], axisY[j]]:
            repetiu += 1

    plt.annotate(repetiu, (combinacoesSingulares[i]), xytext=combinacoesSingulares[i], textcoords='offset points')

plt.xlabel('Evento')
plt.ylabel('Expressão')
plt.title('Evento X Expressão')
plt.show()
