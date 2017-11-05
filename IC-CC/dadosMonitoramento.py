import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def rand_jitter(arr):
    stdev = .01*(max(arr)-min(arr))
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


def main():
    clm = ["codigo_do_jogador", "data_inicio", "horario_inicio", "codigo_do_jogo",
           "nivel_do_jogo", "fase_do_jogo", "etapa", "tipo_AEEJ", "codigo_AEEJ",
           "Val_1", "Val_2", "Val_3", "Data_Gravacao", "Hora_Gravacao ", "Nome_Aruivo"]

    dados = Preprocessing("dadosMonitoramento.csv", clm)

    dictClm = {1: dados.codigo_do_jogador, 2: dados.data_inicio, 3: dados.horario_inicio, 4: dados.codigo_do_jogo,
               5: dados.nivel_do_jogo, 6: dados.fase_do_jogo, 7: dados.etapa, 8: dados.tipo_AEEJ, 9: dados.codigo_AEEJ,
               10: dados.Val_1, 11: dados.Val_2, 12: dados.Val_3, 13: dados.Data_Gravacao, 14: dados.Hora_Gravacao, 15: dados.Nome_Aruivo}



    print("""
    DEFINICAO DE RELACOES
    1-codigo_do_jogador
    2-data_inicio
    3-horario_inicio
    4-codigo_do_jogo
    5-nivel_do_jogo
    6-fase_do_jogo
    7-etapa
    8-tipo_AEEJ
    9-codigo_AEEJ
    10-Val_1
    11-Val_2
    12-Val_3
    13-Data_Gravacao
    14-Hora_Gravacao
    15-Nome_Arquivo
    """)

    first = input("Eixo-X:")
    second = input("Eixo-Y:")

    x = dictClm[first]
    y = dictClm[second]

    data = []

    for i in x:
        data.append([x[i], y[i]])

    kmeans = KMeans(n_clusters=3, random_state=10).fit(data)
    centers = kmeans.cluster_centers_

    plt.scatter(rand_jitter(x), rand_jitter(y), alpha=0.5, s=100, color='green', marker='^')
    plt.title(clm[first - 1] + " X " + clm[second - 1])
    plt.xlabel(clm[first - 1])
    plt.ylabel(clm[second - 1])
    plt.show()

    cx = []
    cy = []
    for i in range(len(kmeans.cluster_centers_)):
        cx.append(kmeans.cluster_centers_[i][0])
        cy.append(kmeans.cluster_centers_[i][1])

    plt.scatter(cx, cy, s=100, c='red', marker='x')

if __name__ == "__main__":
    main()
