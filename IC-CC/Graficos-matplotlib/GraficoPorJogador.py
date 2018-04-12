import matplotlib.pyplot as plt
from tkinter import filedialog,Tk
import pandas as pd


root = Tk()
root.fileName = filedialog.askopenfilename(filetypes = (("howCode files", "*.csv"), ("All files", "*.*")))
root.destroy()
df = pd.read_csv(root.fileName, delimiter=',')

alunosLista = sorted([list(x) for x in set(tuple(x) for x in df[['Codigo_jogador']].values.tolist())])

alunoSelecionado = int(input("Escolha o aluno:" + str(alunosLista) + "\n=>"))

aluno = (df['Codigo_jogador']).tolist()
x = []
y = []
cont = 0
for i in range(len(aluno)):
    if aluno[i] is alunoSelecionado:
        x.append(df['Codigo_expressao'][i])
        t = str(df['Hora_captura'][i])
        (h, m, s) = t.split(':')
        y.append(int(h) * 3600 + int(m) * 60 + int(s))

w = []
for i in range(len(x)):
    w.append([x[i],y[i]])


w.sort(key=lambda x: x[1])

x = []
y = []

for i in range(len(w)):
    x.append(w[i][0])
    y.append(w[i][1])

plt.plot(y,x, color='red')
plt.xlabel('Hora_captura')
plt.ylabel('Codigo_expressao')
plt.title('Hora_captura X Codigo_expressao')
plt.grid(True, color='g', linewidth="3")
plt.show()

