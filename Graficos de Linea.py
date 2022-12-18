import matplotlib
print(matplotlib.__version__)
import matplotlib.pyplot as plt
## Nos muestra las distintas interfaces de colores que tiene matplotlib
print(plt.style.available)
## Usamos el siguiente estilo
plt.style.use('seaborn-v0_8-colorblind')
edad_x = [20,25,30,35,40,45,50,55,60,65]
salario_cd_y = [20000,30000,33000,40000,42000,45000,47000,60000,70000,80000]
salario_fed_y = [10000,15000,17000,25000,30000,32000,35000,40000,49000,50000]
salario_bed_y = [15000,20000,25000,27000,35000,40000,45000,50000,55000,60000]
plt.plot(edad_x, salario_cd_y, label = 'Data Scientist', linewidth = 3, marker = '.', markersize = 15, linestyle = '--', color = '#d62728')
plt.plot(edad_x, salario_fed_y, label = 'Front End Developer')
plt.plot(edad_x, salario_bed_y, label = 'Back End Developer')
plt.legend()
plt.title('Salario medio en $USD por edad')
plt.xlabel('Edad')
plt.ylabel('Salario medio en $USD')
plt.savefig('Gráfico de salario medio.png')
plt.show()
