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
plt.hist(iris["sepallength"], color = "b")
plt.title ("Sepal Length")
plt.ylabel ("Count")
plt.xlabel ("Sepal length (cm's)")
#plt.show()
plt.savefig("sepal_length_hist.png")


plt.hist(iris["petallength"],color = "r")
plt.title ("Petal Length")
plt.ylabel ("Count")
plt.xlabel ("Petal length (cm's)")
#plt.show()
plt.savefig("petal_length_hist.png")


plt.hist(iris["sepalwidth"], color = "g")
plt.title ("Sepal Width")
plt.ylabel ("Count")
plt.xlabel ("Sepal width (cm's)")
#plt.show()
plt.savefig("sepal_width_hist.png")

'''
plt.hist(iris["petalwidth"], color = "m")
plt.title ("Petal Width")
plt.ylabel ("Count")
plt.xlabel ("Petal width (cm's)")
#plt.show()
plt.savefig("petal_width_hist.png")










