import pandas as pd
df = pd.read_csv('/storage/emulated/0/Alarms/iris.csv')
print(df.head())

#Affiche les infos du Dataset
print (df.info())

#Verifiez les valeurs manquand
print(df.isnull().sum())

#Voir les Statistiques
print(df.describe())

#Ici on visualiser la longueur et largeur des sépales en fonction des espèces 
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.show()
