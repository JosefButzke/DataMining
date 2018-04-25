import matplotlib.pyplot as plt
from tkinter import filedialog,Tk
import pandas as pd
import time
import random
import numpy as np

def rand_jitter(arr):
    if type(arr) != str:
        stdev = .001*(max(arr)-min(arr))
        return arr + np.random.randn(len(arr)) * stdev
    return arr

def filtraArquivo():
    root = Tk()
    root.fileName = filedialog.askopenfilename(filetypes = (("howCode files", "*.csv"), ("All files", "*.*")))
    root.destroy()
    df = pd.read_csv(root.fileName, delimiter=',')

    alunosLista = sorted([list(x) for x in set(tuple(x) for x in df[['Codigo_jogador']].values.tolist())])

    for i in range(len(alunosLista)):
        lista = []
        for j in range(len(df)):
            if (df["Tipo_AEEJ"][j] == 1 and df["Codigo_jogador"][j] == alunosLista[i][0]):
                resultado = str(df["Hora_captura"][j])
                (h, m, s) = resultado.split(':')
                lista.append([(int(h) * 3600 + int(m) * 60 + int(s)), df["Codigo_AEEJ"][j]])
        alunosLista[i].append(lista)
    for i in range(len(alunosLista)):
        alunosLista[i][1] = sorted(alunosLista[i][1], key=lambda x: x[0])
    for i in range(len(alunosLista)):
        print(alunosLista[i])

    cores = ["green","blue","red","white","black","orange","yellow","#FF00FF","#40E0D0","#00FA9A","#006400","#00FF00"
        ,"#DAA520","#D2691E","#2E8B57","#FFD700"]
    x = []
    y = []
    cor = []
    for i in range(len(alunosLista)):
        for j in range(10):
            x.append(alunosLista[i][1][j][1])
            y.append(j + 1)
            cor.append(cores[i])
        """  
        plt.plot(x,y)
        x = []
        y = []
        """
    plt.scatter(rand_jitter(x), rand_jitter(y), c=cor, alpha=0.6, s=40, marker='o')
    plt.xlabel('Código AEEJ')
    plt.ylabel('Ordem Realizada')
    plt.title('Tendência')
    plt.show()


if __name__ == '__main__':
    filtraArquivo()