from matplotlib import style
style.use('ggplot')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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

<<<<<<< HEAD


plt.scatter(rand_jitter(x),rand_jitter(y),alpha = 0.5,s=300,c = df.Data,marker= 'o')
=======
plt.scatter(rand_jitter(x),rand_jitter(y),alpha = 0.5,s=100,c = df.Data,marker= '^')
>>>>>>> 180be3e526e697afa4a3090e2056afe02819ddf0
plt.title(clm[first - 1] + " X " + clm[second - 1])
plt.xlabel(clm[first - 1])
plt.ylabel(clm[second - 1])

<<<<<<< HEAD

patch1 = mpatches.Patch(color = '#440154',label='2010')
patch2 = mpatches.Patch(color = '#46327E',label='2011')
patch3 = mpatches.Patch(color = '#365C8D',label='2012')
patch4 = mpatches.Patch(color = '#277F8E',label='2013')
patch5 = mpatches.Patch(color = '#1FA187',label='2014')
patch6 = mpatches.Patch(color = '#4AC16D',label='2015')
patch7 = mpatches.Patch(color = '#A0DA39',label='2016')
patch8 = mpatches.Patch(color = '#FCE625',label='2017')
plt.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6,patch7,patch8])
=======
red_patch1 = mpatches.Patch(color='red', label='2010')
red_patch2 = mpatches.Patch(color='red', label='2011')
red_patch3 = mpatches.Patch(color='red', label='2012')
red_patch4 = mpatches.Patch(color='red', label='2013')
red_patch5 = mpatches.Patch(color='red', label='2014')
red_patch6 = mpatches.Patch(color='red', label='2015')
red_patch7 = mpatches.Patch(color='green', label='2016')
red_patch8 = mpatches.Patch(color='blue', label='2017')
plt.legend(handles=[red_patch1,red_patch2,red_patch3,red_patch4,red_patch5,red_patch6,red_patch7,red_patch8],bbox_to_anchor=(1.2, 1))


>>>>>>> 180be3e526e697afa4a3090e2056afe02819ddf0


plt.show()
