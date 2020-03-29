# Python course

# ---------------------------------------------------------------
# Operations
# ---------------------------------------------------------------
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(1 % 1) 	# Módulo
print(10 ** 2) 	# Exponenciação
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Variables
# ---------------------------------------------------------------
meter = 100		# integer

height = 1.89 	# float
weight = 79		# float

my_name = "João"		# str
my_last_name = 'Gross'	# str
len(my_last_name)	# retorna 5 - tamanho da string

my_bool = True		# bool
my_bool2 = False	# bool

type(height) 	# check variable type

# Converting variable types
str(savings) 	# convert to string
int(height)		# convert to integer
float(meter)	# convert to float
bool(meter)		# convert to bool

savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result))
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Lists
#----------------------------------------------------------------
fam = [1.8, 1.9, 2.4, 1.76] # lista simples

fam2 = [["dad", 1.86],
		["mom", 1.74],
		["love", 1.74],
		["me", 1.89]]		# lista de listas - matriz
		
type(fam) 	# list
type(fam2)	# list

fam[0] 	# retorna 1.8
fam[2]	# retorna 2.4
fam[-1]	# último elemento da lista = 1.76
fam[3]	# retorna 1.76

# List slicing
my_list[start:end]  # The start index will be included, 
					# while the end index is not.

fam[1:3] 	# retorna sublista de fam com elementos [1.9, 2.4]
			# o final da seleção não é selecionado
fam[:3]		# retorna sublista [1.8, 1.9, 2.4]
fam[2:]		# retorna sublista [2.4, 1.76]

fam2[-1][0] # retorna "me"

fam[0:2] = [2.0, 2,2]
print(fam) # [2.0, 2.2, 2.4, 1.76]

# Adding and removing elements
fam + [3.0, 4,0] # fam fica com [2.0, 2.2, 2.4, 1.76, 3.0, 4.0]
del(fam[-1]) 	 # fam fica com [2.0, 2.2, 2.4, 1.76, 3.0]

# List reference and copy
x = ["a", "b", "c"]
y = x 		# diferentes referências à mesma lista
y[1] = "z"	# x = ["a", "z", "c"], y = ["a", "z", "c"]

x = ["a", "b", "c"]
y = list(x) # cria uma nova lista para y
y[1] = "z"	# x = ["a", "b", "c"], y = ["a", "z", "c"]

#----------------------------------------------------------------


# ---------------------------------------------------------------
# Functions
#----------------------------------------------------------------
help(function_name) # mostra detalhes sobre a função
?function_name		# mostra detalhes sobre a função

# Métodos
# funções que pertencem à determinado objeto

type list
	.index("dad")	# retorna índice de "dad"
	.count(1.79)	# retorna qtde de 1.79
	.append("me")	# adiciona "me" ao final da lista
	.remove()
	.reverse()

type str
	.index("a")		# retorna posição de "a"
	.capitalize()	# coloca primeiro caractere em maiúsculo
	.replace("z", "sa")	# substitui um trecho da stirng for outro

# Packages
1. pip.readthedocs.org/en/stable/installing
2. Download get-pip.py
3. Terminal: python3 get-pip.py

pip3 install numpy

import numpy
numpy.array([1, 2, 3])

import numpy as np
np.array([1, 2, 3])
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Numpy
#----------------------------------------------------------------
# Numeric Python
pip3 install numpy

import numpy as np
a = np.array([21, 22, 23, 24, 25])
a[a > 23] # retorna [24, 25]

import numpy as np
a = np.array([21, 22, 23, 24, 25])
my_bools = a > 23	# cria lista de bools com False e True
print(a[my_bools]) 	# imprime apenas elementos True, ou seja,
					# > 23

np_2d = np_array([	[1.74, 1.64, 1.86, 1.89],
					[83, 74, 115, 79] ])
np_2d.shape # retorna a forma da estrutura
np_2d[0][2] # retorna 1.86
np_2d[0,2] 	# retorna 1.86

np_2d[:,1:3]	# retorna as duas linhas, porém apenas as colunas 1 e 2
np_height_in = np_baseball[:,0] # retorna todas as linhas, mas apenas a coluna 0


# Statistics
np.mean()	# média de um conjunto de valores
np.median()	# mediana de um conjunto de valores
np.random.normal() # atributos são média da distribuição, limite de variação e número de amostras

height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
# cria uma lista com 5000 alturas, a média das laturas é 1.75 e elas podem variar até -0.2 e + 0.2
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Data visualization
#----------------------------------------------------------------
# Matplolib
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.scatter(year, pop)
plt.show()

# Histogram
import matplotlib.pyplot as plt
x = np.array([])
plt.hist(x, bins=y)
plt.show()

plt.clf() # clean plot

# Customization
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.xscale('log') # muda escala do gráfico para logarítmico

plt.yticks(	[0, 2, 4, 6, 8, 10], 
			['0', '2B', '4B', '6B', '8B', '10B']) # intervalos de valores para o eixo y e comoos correspondentes labels de exibição de cada valor

plt.scatter(year, pop, size)	# size é o tamanho de cada ponto no gráfico 
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Dictionaries
#----------------------------------------------------------------
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

world_dict = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world_dict["albania"] # retorna 39.21

# Dicionário possui chaves imutáveis. 
# Não permite chaves duplicadas
# É possível atualizar o valor associado à uma chave

"algeria" in world_dict # retorna True

del(world_dict["albania"]) # remove elemento "albania" do dicionário


europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
europe['spain']['capital']  # retorna 'madrid'
data = { 'capital':'rome', 'population':59.83 }
europe['italy'] = data # novo registro para 'italy'

#----------------------------------------------------------------


# ---------------------------------------------------------------
# Pandas
#----------------------------------------------------------------
# DataFrame
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(my_dict) 

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels # Specify row labels of cars


# Read from CSV file
cars = pd.read_csv('cars.csv', index_col = 0) # lê do arquivo e diz que o índice do DataGrame é a coluna 0 do arquivo


# Column Access []
cars[[names]] # retorna DataFrame dos nomes, com seus respectivos índices

# Row Access []
cars[1:4] #seleciona as linhas correspondentes 1, 2 e 3

# Row Access loc
cars.loc[['US']] # retorna toda informações sobre esse índice
cars.loc[['US', 'JPN', 'IN']] 
cars.loc[['US', 'JPN', 'IN'], ['names', 'cpc']] 

# Row Access iloc
cars.iloc[[0]]
cars.iloc[[0, 2, 3]]
cars.iloc[[0, 2, 3], [0, 2]]

# Função apply
import pandas as pd
brics = pd.read_csv("path/to/brics.csv", index_col = 0)
brics["name_lenght"] = brics["country"].apply(len) # Cria nova coluna no DataFrame com o comprimento do nome do país

#----------------------------------------------------------------

# ---------------------------------------------------------------
# Comparison Operators
#----------------------------------------------------------------
2 < 3 	# True
2 == 3 	# False
2 <= 3	# True
2 != 3 	# True
"carl" < "chris" # True
3 < "chris"	# Error

bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])
bmi > 23 # array([False, False, False, True, False])
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Boolean Operators
#----------------------------------------------------------------
True and False	# False
False or True	# True
not True		# False

bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])
bmi > 23 # array([False, False, False, True, False])

bmi > 23 and bmi < 22	# Error

# For Numpy Arrays
logical_and()
logical_or()
logical_not()

np.logical_and(bmi > 21, bmi < 22) # array([True, False, True, False, True])
bmi[np.logical_and(bmi > 21, bmi < 22)] # array([21.852, 21.75, 21.441])
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Conditional Statements
#----------------------------------------------------------------
z = 4
if z % 2 == 0 : 	# True
	print("z is even")	# É par
	print("other text")
elif z == 3 :
	pint("z equal 3")	# Igual a 3
else :
	print("z is odd")	# É ímpar
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Filtering Pandas DataFrames
#----------------------------------------------------------------
import pandas as pd
brics = pd.read_csv("path/to/brics.csv", index_col = 0)

brics["area"]	# Faz seleção de uma da coluna "area" no formato Series em cima do DataFrame
is_huge = brics["area"] > 8	# Retorna uma Series de bools 
brics[is_huge]	# Retorna apenas os registros do DataFrame com "area" > 8

# Uso de operadores booleanos para Numpy em DataFrames
import numpy as np
area = brics["area"] # Seleciona coluna - formato Series
result = np.logical_and(area > 8, area < 10) # Cria bool Series para utilizar na seleção
brics[result] # seleciona apenas os registros com área > 8 e área < 10
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Loop statements
#----------------------------------------------------------------
# While loop
error 50.0
while error > 1:
	error = error / 4
	print(error)
	
# For loop
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
	print(height)
for index, height in enumerate(fam):
	print("person " + str(index) + ": " + str(height))

# For for dictionaries
world_dict = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
for key, valeu in world.items():
	print(key + " -- " + str(value))
	
# For for Numpy Arrays
np_height = np.array([1.73, 1.68, 1.71, 1.89])
np_weight = np.array([65,4, 59.2, 63.5, 88.4])
meas = np.array([np_height, np_weight])
for val in meas:
	print(val)	# Faz duas impressões, cada uma de um array inteiro
for val in np.nditer(meas):
	print(val)	# Faz oito impressões, primeiro das alturas e depois dos pesos

# For for Pandas DataFrame
import pandas as pd
brics = pd.read_csv("path/to/brics.csv", index_col = 0)
for val in brics:
	print(val)	# Imprime apenas os títulos das colunas
for label, row in brics.iterrows():
	print(label)	# Imprime o label do DataFrame
	print(row)		# Imprime todo os restante dos dados do registro
for label, row in brics.iterrows():
	print(label + ": " + row["capital"]) # Imprime o "label" e mais a capital
#----------------------------------------------------------------


# ---------------------------------------------------------------
# Random Numbers
#----------------------------------------------------------------
# Random Generators
import numpy as np
np.random.rand()	# Pseudo-random numbers

np.random.seed(123)	# Starting from a seed
np.random.rand()

# Coin Toss
import numpy as np
np.random.seed(123)	# Starting from a seed
coin = np.random.randint(0,2)	# Randomly generate 0 or 1
if coin == 0:
	print("heads")
else:
	print("tails")


#----------------------------------------------------------------














