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
'''

# Demonstrating the correlation within each individual species and creating heatmaps for each


print ("Correlation table within the Iris Setosa species", file = out)
print (iris_set.corr(), file = out)
print ("", file = out)
'''
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_set.corr(),cmap = "Reds", annot = True)
plt.show()
'''

print ("Correlation table within the Iris Versicolor species", file = out)
print (iris_ver.corr(), file = out)
print ("", file = out)
'''
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_ver.corr(),cmap = "Greens", annot = True)
plt.show()
'''

print ("Correlation table within the Iris Virginica species", file = out)
print (iris_vir.corr(), file = out)
print ("", file = out)
'''
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_vir.corr(),cmap = "Purples", annot = True)
plt.show()
'''

#Creating a histogram for each variable and save it to a png file

'''
def hist_var (n, variable, col, x_label,):
    plt.subplot(2,2,n)
    plt.hist(iris[variable], color = col)
    plt.ylabel ("Frequency")
    plt.xlabel (x_label)
    plt.suptitle ("Variable Distribution")
    plt.tight_layout()
    #plt.show () (This just to confirm all working okay)
    plt.savefig("variable_histograms.png")

hist_var (1, "sepallength", "b", "Sepal Length")
hist_var (2, "petallength", "r", "Petal Length")
hist_var (3, "sepalwidth", "g", "Sepal Width")
hist_var (4, "petalwidth", "m", "Petal Width")
'''

#histogram colour coded by species in order to see spread more clearly

'''
def hist_func (n ,variable, x_label):
    plt.suptitle ("Variable Distribution When Split by Species")
    plt.subplot(2,2,n)
    plt.hist(iris_set[variable], alpha = 0.75, label = "Iris Setosa", color = "m")
    plt.hist(iris_ver[variable], alpha = 0.5, label = "Iris Versicolour", color = "b")
    plt.hist(iris_vir [variable], alpha = 0.5, label = "Iris Virginica", color = "g")
    plt.xlabel (x_label)
    plt.ylabel ("Frequency")
    plt.tight_layout()
    plt.savefig ("variable_species_histogram.png")

hist_func (1, "petalwidth", "Petal Width (cm's)")
hist_func (2, "petallength", "Petal length (cm's)")
hist_func (3, "sepalwidth", "Sepal Width (cm's)")
hist_func (4, "sepallength", "Sepal Length (cm's)")
'''

# scatterplots x 6 for investigations on linear relationships

'''
def scatter_func (x_name,y_name,x_variable,y_variable,output_name):
   plt.xlabel (x_name)
   plt.ylabel (y_name)
   sns.scatterplot (x_variable, y_variable , data = iris, hue = "class") #This works
   plt.savefig(output_name)

scatter_func ("Sepal Length", "Petal Length", "sepallength", "petallength", "SlengthPlength.png")
scatter_func ("Sepal Length", "Sepal Width", "sepallength", "sepalwidth", "SwidthSlength.png")
scatter_func ("Petal Length", "Petal Width", "petallength", "petalwidth", "PwidthPlength.png")
scatter_func ("Sepal Width", "Petal Length", "sepalwidth", "petallength", "SwidthPlength.png")
scatter_func ("Sepal Width", "Petal Width", "sepalwidth", "petalwidth", "SwidthPwidth.png")
scatter_func ("Sepal Length", "Petal Width", "sepallength", "petalwidth", "SlengthPwidth.png") 
'''

#linear regression model plot function w/outputs 
'''
def lm_plot( x_value, y_value,output_file):
    sns.lmplot (x = x_value, y = y_value, data = iris, hue = "class")
    plt.savefig (output_file)
lm_plot("sepallength", "petallength", "lm_1.png")
lm_plot("sepallength", "sepalwidth", "lm_2.png")
lm_plot("petallength", "petalwidth", "lm_3.png")
lm_plot("sepalwidth", "petallength", "lm_4.png")
lm_plot("sepalwidth", "petalwidth", "lm_5.png")
lm_plot("sepallength", "petalwidth", "lm_6.png")
'''

# boxplot/swarmplot

'''
def swarmbox_plt(n, variable):
    plt. subplot (2,2,n)
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 1, color = "w")
swarmbox_plt(1, "petalwidth")
swarmbox_plt(2, "petallength")
swarmbox_plt(3, "sepallength")
swarmbox_plt(4, "sepalwidth")
plt.tight_layout()
plt.savefig("box_swarm_plot.png")
'''

#swarmplot/boxplot 

'''
def swarmbox_plt(variable, output):
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 3, color = "w")
    plt.savefig (output)
#swarmbox_plt("petalwidth", "boxplot_petal_w.png")
#swarmbox_plt("petallength", "boxplot_petal_l.png")
#swarmbox_plt("sepallength", "boxplot_sepal_l.png")
#swarmbox_plt("sepalwidth", "boxplot_sepal_w.png")
'''

# figure pair plot 

'''
figurepairplot = sns.pairplot(data = iris, kind = "scatter", hue = "class") 
plt.savefig ("pair-plot")
'''