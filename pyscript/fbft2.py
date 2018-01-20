from sklearn import datasets
from matplotlib import pyplot as plt

iris = datasets.load_iris()
#sepal length
iris_col_1 = iris.data[:,:1]
#sepal width
iris_col_2 = iris.data[:,1:2]
#petal length
iris_col_3 = iris.data[:,2:3]
#petal width
iris_col_4 = iris.data[:,3:4]

iris_list = [iris_col_1,iris_col_2,iris_col_3,iris_col_4]

fig,ax = plt.subplots(4,4)

def label_iris(outer,inner):
	if outer == 0:
		ax[outer][inner].annotate('Sepal Length',(0.10,0.5))
	elif outer == 1:
		ax[outer][inner].annotate('Sepal Width',(0.10,0.5))
	elif outer == 2:
		ax[outer][inner].annotate('Petal Length',(0.10,0.55))
	elif outer == 3:
		ax[outer][inner].annotate('Petal Width',(0.10,0.55))

for outer,i in enumerate(iris_list):
	for inner,j in enumerate(iris_list):
		
		if outer != inner: 
			ax[outer][inner].scatter(i,j,s=0.5)
		else: 
			label_iris(outer,inner)
		if outer < 3: ax[outer][inner].xaxis.set_visible(False)
		if inner > 0: ax[outer][inner].yaxis.set_visible(False)
plt.suptitle('Plot Matrix for Iris Dataset')
plt.show()