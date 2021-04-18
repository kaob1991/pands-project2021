# Program to analyse and produce plots from a dataset imported into the program 

# This dataset is fisher's dataset and we will be obtaining a summary of each variable 
# saving it to a text output and then saving a histogram of each variable to a png file 

# Author: Katie O'Brien 


# Importing required libraries
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

# reading in the iris datafile 
iris = pd.read_csv ("iris_csv.csv")

# Outputting the data to a .txt file 
out = open("summary_file_text_output.txt", "w")



# Sanity check to ensure all libraries and file for reading in is correctly loading
# print ("all okay") # Commented out post check

# Using shape () to get the size and shape of the datafile, confirming the number of
# rows in the dataset is 150 as expected 
print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)
print ("",file = out)
print ("", file = out)

# And demonstrating the layout of the datafile 
print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)
print ("", file = out)
print ("", file = out)

#This provides a numerical summary of the data including mean max std etc 
print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)
print ("", file = out)
print ("", file = out)

#dividing the dataset into the corresponding datatypes 
iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]


# running a summary of the data sorted by datatype 
print ("Numerical summary of the Iris Setosa", file = out)
print (iris_set.describe(), file = out)
print ("", file = out)
print ("Numerical summary of the Iris Versicolor", file = out)
print (iris_ver.describe(), file = out)
print ("", file = out)
print ("Numerical summary of the Iris Virginica", file = out)
print (iris_vir.describe(), file = out)
print ("", file = out)
print ("", file = out)

# Demonstrating the correlation between the various variable types 
print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 
print ("", file = out)
print ("", file = out)

# Demonstrating a heatmap for correlation above 
# (ref:https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d)
'''
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris.corr(),cmap = "Blues", annot = True)
plt.show()

# Demonstrating the correlation within each individual species and creating heatmaps for each
print ("Correlation table within the Iris Setosa species", file = out)
print (iris_set.corr(), file = out)
print ("", file = out)
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_set.corr(),cmap = "Reds", annot = True)
plt.show()
print ("Correlation table within the Iris Versicolor species", file = out)
print (iris_ver.corr(), file = out)
print ("", file = out)
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_ver.corr(),cmap = "Greens", annot = True)
plt.show()
print ("Correlation table within the Iris Virginica species", file = out)
print (iris_vir.corr(), file = out)
print ("", file = out)
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_vir.corr(),cmap = "Purples", annot = True)
plt.show()


#Creating a histogram for each variable and save it to a png file

plt.subplot (2,2,1)
plt.hist(iris["sepallength"], color = "b")
plt.ylabel ("Frequency")
plt.xlabel ("Sepal length (cm's)")
#plt.show()

plt.subplot (2,2,2)
plt.hist(iris["petallength"],color = "r")
plt.ylabel ("Frequency")
plt.xlabel ("Petal length (cm's)")
#plt.show()

plt.subplot (2,2,3)
plt.hist(iris["sepalwidth"], color = "g")
plt.ylabel ("Frequency")
plt.xlabel ("Sepal width (cm's)")
#plt.show()

plt.subplot(2,2,4)
plt.hist(iris["petalwidth"], color = "m")
plt.ylabel ("Frequency")
plt.xlabel ("Petal width (cm's)")

plt.suptitle ("Variable Distribution")
plt.tight_layout()
#plt.show ()
plt.savefig("variable_histograms.png")


# Next I wanted to run a histogram splitting the variables by species in order to see the distribution correctly 

plt.suptitle ("Variable Distribution When Split By Species")

plt.subplot(2,2,1)
plt.hist(iris_set["petalwidth"], alpha = 0.75, label = "Iris Setosa", color = "m")
plt.hist(iris_ver["petalwidth"], alpha = 0.5, label = "Iris Versicolour", color = "b")
plt.hist(iris_vir ["petalwidth"], alpha = 0.5, label = "Iris Virginica", color = "g")
plt.xlabel ("Petal Width")
plt.ylabel ("Count")
plt.legend (loc = "best")

plt.subplot(2,2,2)
plt.hist(iris_set["petallength"], alpha = 0.75, label = "Iris Setosa", color = "m")
plt.hist(iris_ver["petallength"], alpha = 0.5, label = "Iris Versicolour", color = "b")
plt.hist(iris_vir ["petallength"], alpha = 0.5, label = "Iris Virginica", color = "g")
plt.xlabel ("Petal Length")
plt.ylabel ("Frequency")

plt.subplot(2,2,3)
plt.hist(iris_set["sepalwidth"], alpha = 0.75, label = "Iris Setosa", color = "m")
plt.hist(iris_ver["sepalwidth"], alpha = 0.5, label = "Iris Versicolour", color = "b")
plt.hist(iris_vir ["sepalwidth"], alpha = 0.5, label = "Iris Virginica", color = "g")
plt.xlabel ("Sepal Width (cm's)")
plt.ylabel ("Frequency")

plt.subplot(2,2,4)
plt.hist(iris_set["sepallength"], alpha = 0.75, label = "Iris Setosa", color = "m")
plt.hist(iris_ver["sepallength"], alpha = 0.5, label = "Iris Versicolour", color = "b")
plt.hist(iris_vir ["sepallength"], alpha = 0.5, label = "Iris Virginica", color = "g")
plt.xlabel ("Sepal Length (cm's)")
plt.ylabel ("Frequency")
plt.tight_layout()
plt.savefig ("variable_species_histograms.png")





figurepairplot = sns.pairplot(data = iris, kind = "scatter", hue = "class") # This needs its color fixing - all blue atm 
plt.savefig ("pair-plot")


sns.lmplot (x = "petallength", y = "petalwidth", data = iris)
plt.savefig ("l_model_petal")
sns.lmplot (x = "sepallength", y = "sepalwidth", data = iris)
plt.savefig ("l_model_sepal") # linear model research needed 
'''

w = "petallength"
x = "sepallength"
y = "sepalwidth"
z = "petalwidth"
'''
plt.xlabel ("Sepal Length")
plt.ylabel ("Sepal Width")
sns.scatterplot (x, y , data = iris, hue = "class") #This works
plt.savefig("SWidthSLength.png")

plt.xlabel ("Sepal Length")
plt.ylabel ("Petal Length")
sns.scatterplot (x, w , data = iris, hue = "class")
plt.savefig ("SlengthPlength.png")

plt.xlabel ("Sepal Length")
plt.ylabel ("Petal Width")
sns.scatterplot (x, z , data = iris, hue = "class")
plt.savefig ("SlengthPwidth.png")

plt.xlabel ("Sepal Width")
plt.ylabel ("Petal Width")
sns.scatterplot (y , z, data = iris, hue = "class")
plt.savefig ("SwidthPwidth.png")

plt.xlabel ("Sepal Width")
plt.ylabel ("Petal Length")
sns.scatterplot (y, w , data = iris, hue = "class")
plt.savefig ("SwidthPlength.png")

plt.xlabel ("Petal Width")
plt.ylabel ("Petal length")
sns.scatterplot (z , w , data = iris, hue = "class")
plt.savefig ("PwidthPlength.png")

'''



