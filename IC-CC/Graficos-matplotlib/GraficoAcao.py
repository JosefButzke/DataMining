import matplotlib.pyplot as plt
from tkinter import filedialog,Tk
import pandas as pd

root = Tk()
root.fileName = filedialog.askopenfilename(filetypes = (("howCode files", "*.csv"), ("All files", "*.*")))
root.destroy()
df = pd.read_csv(root.fileName, delimiter=',')


tipoAEEJ = (df['Tipo_AEEJ']).tolist()

axisX = []
axisY = []

for i in range(len(tipoAEEJ)):
    if tipoAEEJ[i] is 1:
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

    plt.annotate(repetiu, (combinacoesSingulares[i]), xytext=(5,5), textcoords='offset points')

plt.xlabel('Ação')
plt.ylabel('Expressão')
plt.title('Ação X Expressão')
plt.show()
