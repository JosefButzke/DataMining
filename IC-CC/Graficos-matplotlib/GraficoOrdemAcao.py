import matplotlib.pyplot as plt
from tkinter import filedialog,Tk
import pandas as pd
import time
import random
import numpy as np

def rand_jitter(arr):
    if type(arr) != str:
        stdev = .01*(max(arr)-min(arr))
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
                resultado1 = str(df["Hora_captura"][j])
                (h, m, s) = resultado1.split(':')
                resultado2 = str(df["Data_captura"][j])
                (dd, mm, yyyy) = resultado2.split('/')
                lista.append([yyyy,mm,dd,h,m,s, df["Codigo_AEEJ"][j]])

        alunosLista[i].append(lista)
        alunosLista[i][1] = sorted(alunosLista[i][1], key=lambda x: (x[0],x[1],x[2],x[3],x[4],x[5]))
        
    x = []
    y = []
    maxOrdem = 100
    for i in range(len(alunosLista)):
        if maxOrdem > len(alunosLista[i][1]):
            maxOrdem = len(alunosLista[i][1])
    for i in range(len(alunosLista)):
        for j in range(maxOrdem):
            x.append(alunosLista[i][1][j][6])
            y.append(j + 1)
            
        labelX = rand_jitter(x)
        labelY = rand_jitter(y)
        plt.plot(labelX,labelY)
        plt.scatter(labelX,labelY)
        x = []
        y = []
    
        """
    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.6, s=40, marker='o')
    """
    plt.xlabel('Código AEEJ')
    plt.ylabel('Ordem Realizada')
    plt.title('Tendência')
    plt.show()
    


if __name__ == '__main__':
    filtraArquivo()
