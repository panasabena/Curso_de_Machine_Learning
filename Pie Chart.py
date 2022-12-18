import matplotlib
import matplotlib.pyplot as plt

## Datos
edad_x = [20,25,30,35,40,45,50,55,60,65]
salario_cd_y = [20000,30000,33000,40000,42000,45000,47000,60000,70000,80000]
salario_fed_y = [10000,15000,17000,25000,30000,32000,35000,40000,49000,50000]
salario_bed_y = [15000,20000,25000,27000,35000,40000,45000,50000,55000,60000]

## Imprimimos gráfico

plt.pie(salario_cd_y, labels = edad_x, shadow = True,
        wedgeprops = {'edgecolor': 'black'},
        autopct = '%1.1f%%')
plt.title('Edad y Salario')
plt.show()
