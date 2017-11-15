from tkinter import filedialog,Tk
import pandas as pd
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


menu = df.columns.values
indice = 1
for i in menu:
    print(str(indice) + str("-") + str(i))
    indice += 1
first = input("Eixo-X:")
second = input("Eixo-Y:")
third = input("Cor dos Pontos:")
cores = ['#440154','#46327E','#365C8D','#277F8E','#1FA187','#4AC16D','#A0DA39','#FCE625']
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
    z = df[df.columns[third - 1]]


    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.6, s=100, c=z, marker='o')
    plt.title(df.columns.values[first - 1] + " X " + df.columns.values[second - 1])


else:
    x = df[df.columns[first - 1]]
    y = df[df.columns[second - 1]]
    z = df[df.columns[third - 1]]


    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.6, s=100, c=z, marker='o')
    plt.title(df.columns.values[first - 1] + " X " + df.columns.values[second - 1])
    plt.xlabel(df.columns.values[first - 1])
    plt.ylabel(df.columns.values[second - 1])

plt.subplots_adjust(top=0.95, bottom=0.1, left=0.11, right=0.8)

if(third is not None):
    legenda =  set(df[df.columns.values[third - 1]])
    legenda = sorted(legenda)


    vet = []
    x = sorted(legenda)
    vet.append(min(x))
    vet.append(x[len(x) / 8])
    vet.append(x[2 * len(x) / 8])
    vet.append(x[3 * len(x) / 8])
    vet.append(x[4 * len(x) / 8])
    vet.append(x[5 * len(x) / 8])
    vet.append(x[6 * len(x) / 8])
    vet.append(max(x))


    ind = 0
    patch = []
    while(ind <= len(vet) - 1):
        patch.append(mpatches.Patch(color = cores[ind] , label=vet[ind]))
        ind += 1

    plt.legend(handles=patch,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


plt.show()
