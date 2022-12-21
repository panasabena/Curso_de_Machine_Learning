import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
df = pd.read_csv('./Datasets/data_regression.csv')
print(df)
print(df.info())
#print('Los valores unicos de Topicos son: \n',df['Topico'].unique())
x_1 = df['X1']
x_2 = df['X2']
x_3 = df['X3']
y = df['y']


X_train, X_test, y_train, y_test = train_test_split(x_1, y, test_size = 0.2, random_state = 42)

print('Cantidad de datos separados:\n')
print('X_train: ',X_train.shape)
print('X_test: ',X_test.shape)
print('y_train: ',y_train.shape)
print('X_test: ',y_test.shape)
print('###############')
lin_model = LinearRegression()

#print('lin_model.fit(X_train, y_train): \n', lin_model.fit(X_train, y_train))

plt.title('Distribución de los valores de X')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.plot(x_1,y, color = 'blue', label = 'X_1')
plt.plot(x_2,y, color = 'red', label = 'X_2')
plt.plot(x_3,y, color = 'orange', label = 'X_3')
plt.legend()
plt.grid()
plt.show()

