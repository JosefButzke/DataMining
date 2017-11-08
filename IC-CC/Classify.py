import graphviz
from sklearn import tree
import pandas as pd
import numpy as np

alun = pd.read_csv('teste18.csv',delimiter=',')
results = {0: 'Bom',1:'Dificuldade' ,2: 'Medio'}

def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x=0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))
    return df
alun = handle_non_numerical_data(alun)



alun.data = alun.values[:,0:8]
alun.target = alun.values[:,8]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(alun.data,alun.target)

"""
A-              0
H-              1
C-              2
------------------
F-              1
M-              0
------------------
DIFICULDADE-    1
MEDIO-          2
BOM-            0
"""
vet = []
print("Entre com os dados(string devem ser declarados como numeros de acordo com a tabela acima):")
vet.append(input("Codigo_do_Jogador: "))
vet.append(input("Sexo(M=0,F = 1): "))
vet.append(input("Data: "))
vet.append(input("Idade: "))
vet.append(input("Tempo: "))
vet.append(input("TipoAprendizagem(A=0,H=1,C=2): "))
vet.append(input("CodigoAprendizagem: "))
vet.append(input("ValorAprendizagem: "))




resul = clf.predict([vet])

print ("Predicao para: " + str(vet)+ "\n" + "eh: " + str(results[int(resul)]))

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("Alun")

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render()


"""
A-              0
H-              1
C-              2
------------------
F-              1
M-              0
------------------
DIFICULDADE-    1
MEDIO-          2
BOM-            0
"""




"""
alun_X = alun.data
alun_y = alun.target
np.random.seed(0)
indices = np.random.permutation(len(alun_X))
alun_X_train = alun_X[indices[:-10]]
alun_y_train = alun_y[indices[:-10]]
alun_X_test  = alun_X[indices[-10:]]
alun_y_test  = alun_y[indices[-10:]]

knn = KNeighborsClassifier()
knn.fit(alun_X_train, alun_y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
print(knn.predict(alun_X_test))
print(alun_y_test)
"""