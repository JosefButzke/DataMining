from sklearn import cluster
import pandas as pd
from matplotlib import style
style.use('ggplot')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.cluster import KMeans


def rand_jitter(arr):
    stdev = .001*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

def Preprocessing(name,columns):
    df = pd.read_csv(name, delimiter=',')
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


##########################################################################################################
##########################################################################################################
clm = ['Codigo_do_Jogador', 'Sexo', 'Data', 'Idade', 'Tempo', 'TipoAprendizagem','CodigoAprendizagem',
       'ValorAprendizagem', 'Classificacao']


df = Preprocessing('teste18.csv',clm)


dict = {1: df.Codigo_do_Jogador,2: df.Sexo,3: df.Data,4: df.Idade,5: df.Tempo,6: df.TipoAprendizagem,7: df.CodigoAprendizagem,8: df.ValorAprendizagem,9: df.Classificacao}
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
x = dict[first]
y = dict[second]

data = []

for i in x:
    data.append([x[i],y[i]])


kmeans = KMeans(n_clusters=3, random_state=10).fit(data)
centers = kmeans.cluster_centers_


plt.scatter(rand_jitter(x),rand_jitter(y),alpha = 0.6,s=100,c = df.Data,marker= 'o')
plt.title(clm[first - 1] + " X " + clm[second - 1])
plt.xlabel(clm[first - 1])
plt.ylabel(clm[second - 1])


cx = []
cy = []
for i in range (len(kmeans.cluster_centers_)):
    cx.append(kmeans.cluster_centers_[i][0])
    cy.append(kmeans.cluster_centers_[i][1])


plt.scatter(cx,cy,s=100,c = 'red',marker= 'x')


plt.show()
