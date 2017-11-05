from tkinter import filedialog,Tk
import pandas as pd
from matplotlib import style
style.use('ggplot')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def rand_jitter(arr):
    if type(arr) != str:
        stdev = .001*(max(arr)-min(arr))
        return arr + np.random.randn(len(arr)) * stdev
    return arr

def Preprocessing(df,columns):
    pd.DataFrame(
        columns= columns)

    def handle_non_numerical_data(df):
        columns = df.columns.values
        for column in columns:
            text_digit_vals = {}

            def convert_to_int(val):
                return text_digit_vals[val]

            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                column_contents = df[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x += 1
                df[column] = list(map(convert_to_int, df[column]))
        return df

    df = handle_non_numerical_data(df)
    return df


root = Tk()
root.fileName = filedialog.askopenfilename(filetypes = (("howCode files","*.csv"),("All files","*.*")))
root.destroy()
df = pd.read_csv(root.fileName,delimiter=',')


##########################################################################################################
print("DEFINICAO DE RELACOES")
print("1-Codigo_do_Jogador")
print("2-Sexo")
print("3-Data")
print("4-Idade")
print("5-Tempo")
print("6-TipoAprendizagem")
print("7-CodigoAprendizagem")
print("8-ValorAprendizagem")
print("9-Classificacao")
first = input("Eixo-X:")
second = input("Eixo-Y:")
##########################################################################################################

if (df[df.columns[first-1]].dtype != np.int64 and df[df.columns[first-1]].dtype != np.float64) or \
        (df[df.columns[second-1]].dtype != np.int64 and df[df.columns[second-1]].dtype != np.float64):
    #########################################################################################################
    if(df[df.columns[first-1]].dtype != np.int64 and df[df.columns[first-1]].dtype != np.float64):
        names = set(df[df.columns.values[first - 1]].values.tolist())
        x = range(len(set(df[df.columns.values[first - 1]].values.tolist())))
        plt.xticks(x, names)
    if(df[df.columns[second-1]].dtype != np.int64 and df[df.columns[second-1]].dtype != np.float64):
        names = set(df[df.columns.values[second - 1]].values.tolist())
        y = range(len(set(df[df.columns.values[second - 1]].values.tolist())))
        plt.yticks(y, names)
    #########################################################################################################
    df = Preprocessing(df, df.columns)

    x = df[df.columns[first-1]]
    y = df[df.columns[second-1]]

    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.6, s=100, c=df.Data, marker='o')
    plt.title(df.columns.values[first - 1] + " X " + df.columns.values[second - 1])


else:
    x = df[df.columns[first - 1]]
    y = df[df.columns[second - 1]]

    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.6, s=100, c=df.Data, marker='o')
    plt.title(df.columns.values[first - 1] + " X " + df.columns.values[second - 1])
    plt.xlabel(df.columns.values[first - 1])
    plt.ylabel(df.columns.values[second - 1])

patch1 = mpatches.Patch(color = '#440154',label='2010')
patch2 = mpatches.Patch(color = '#46327E',label='2011')
patch3 = mpatches.Patch(color = '#365C8D',label='2012')
patch4 = mpatches.Patch(color = '#277F8E',label='2013')
patch5 = mpatches.Patch(color = '#1FA187',label='2014')
patch6 = mpatches.Patch(color = '#4AC16D',label='2015')
patch7 = mpatches.Patch(color = '#A0DA39',label='2016')
patch8 = mpatches.Patch(color = '#FCE625',label='2017')
plt.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6,patch7,patch8])



plt.show()
