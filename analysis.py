# Program to analyse and produce plots from a dataset imported into the program 

# This dataset is fisher's dataset and we will be obtaining a summary of each variable 
# saving it to a text output and then saving multiple plots of each variable to a png file 

# Further information is within the README file.

# Author: Katie O'Brien (G00398250)



# importing required libraries for the dataset analysis

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns


# reading in the csv iris datafile

iris = pd.read_csv ("iris_csv.csv")


# outputting the data to a .txt file, the "w" ensures the file will be
# overwritten each time the program is ran 

out = open("summary_file_text_output.txt", "w")


# sanity check to ensure all libraries and file for reading in is correctly loading
# print ("all okay") 
# commented out post check as it is not required for the program



# using shape() to get the size and shape of the datafile, confirming the number of
# rows in the dataset is 150 as expected;
# and printing the header for ease of differentiation between various outputs
# file = out outputs the file to the .txt doc

print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)
print ("",file = out) # This is for empty rows for formatting
print ("", file = out)


# and demonstrating the layout of the datafile using head() 
# with 5 denoting the number of rows of the dataset to display 

print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)
print ("", file = out)
print ("", file = out)


# this provides a numerical summary of the data including mean max std etc using describe()
# and outputs it to the datafile above 

print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)
print ("", file = out)
print ("", file = out)


# after running the initial analysis the data was then divided
# into the corresponding "class", ie species of flower using loc()

iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]


# running a summary of the data sorted by class using describe() 
# and outputting to file

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


# demonstrating the correlation between the various variable types using corr() and outputting to file

print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 
print ("", file = out)
print ("", file = out)


# demonstrating a heatmap for the correlations above using heatmap() 
# cmap determines the colours used and annot writes the data value in each cell

fig = plt.figure(figsize = (8,3))
sns.heatmap(iris.corr(),cmap = "Blues", annot = True)
plt.savefig ("heatmap_correlation.png")


# demonstrating the correlation within each individual species and creating heatmaps for each

print ("Correlation table within the Iris Setosa species", file = out)
print (iris_set.corr(), file = out)
print ("", file = out)

fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_set.corr(),cmap = "Reds", annot = True)
plt.savefig ("heatmap_setosa.png")


print ("Correlation table within the Iris Versicolor species", file = out)
print (iris_ver.corr(), file = out)
print ("", file = out)

fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_ver.corr(),cmap = "Greens", annot = True)
plt.savefig("heatmap_versicolor.png")


print ("Correlation table within the Iris Virginica species", file = out)
print (iris_vir.corr(), file = out)
print ("", file = out)

fig = plt.figure(figsize = (8,3))
sns.heatmap(iris_vir.corr(),cmap = "Purples", annot = True)
plt.savefig("heatmap_virginica.png")


# creating a histogram function that will save to a png file
# using the axes to set subplots for the file
# histplot() creates the plot with the following variables
# (datafile, x axis/varaible, setting the labels size, the colour of the histgrams, the kernel density estimation, and the plot position)
# savefig() saves the plots to a .png file name set below 

f, axes = plt.subplots (2,2)
sns.histplot(iris, x = "sepallength", label = "small", color = "green", kde = True, ax = axes [0][0])
sns.histplot(iris, x = "sepalwidth", label = "small", color = "black", kde = True, ax = axes [1][1])
sns.histplot(iris, x = "petallength", label = "small", color = "blue", kde = True, ax = axes [0][1])
sns.histplot(iris, x = "petalwidth", label = "small",color = "red", kde = True, ax = axes [1][0])
plt.savefig("variable_histograms.png")


# function created for a histogram colour coded by species in order to see spread more clearly
# suptitle() gives the plots an overall title
# subplot() allows multiple eplots on one .png file
# hist() creates the histogram
# alpha = denotes the transparancy of the bars, allowing overlapping variables to still be seen
# label = labels the colours allowing a legend to also be displayed
# x/ylabel sets the titles on the axis
# tight_layout() resizes the fonts of the plots to make them all fit better in the graphic 
# savefig() saves output as a .png file

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


# the 4 lines below are creating a histogram for each 
# the variables are as follows: plot number (n out of 4), variable, x-axis label

hist_func (1, "petalwidth", "Petal Width (cm's)")
hist_func (2, "petallength", "Petal length (cm's)")
hist_func (3, "sepalwidth", "Sepal Width (cm's)")
hist_func (4, "sepallength", "Sepal Length (cm's)")


# defining a function for scatterplot analysis with variables
# x/ylabel takes in axis names
# scatterplot () takes in 2 variables (x & y), data takes in the dataset
# hue splits the data by class
# savefig() saves the file as a png file

def scatter_func (x_name,y_name,x_variable,y_variable,output_name):
    plt.figure()
    plt.xlabel (x_name)
    plt.ylabel (y_name)
    sns.scatterplot (x_variable, y_variable , data = iris, hue = "class") 
    plt.savefig(output_name)


# creating the scatterplots using each variable as required. The variables are as follows 
# (x and y axes labels, x and y variables, output_name)

scatter_func ("Sepal Length", "Petal Length", "sepallength", "petallength", "SlengthPlength.png")
scatter_func ("Sepal Length", "Sepal Width", "sepallength", "sepalwidth", "SwidthSlength.png")
scatter_func ("Petal Length", "Petal Width", "petallength", "petalwidth", "PwidthPlength.png")
scatter_func ("Sepal Width", "Petal Length", "sepalwidth", "petallength", "SwidthPlength.png")
scatter_func ("Sepal Width", "Petal Width", "sepalwidth", "petalwidth", "SwidthPwidth.png")
scatter_func ("Sepal Length", "Petal Width", "sepallength", "petalwidth", "SlengthPwidth.png") 


# defines the linear model regression plot function 
# lmplot() takes in the following values: x/y_value as variables, data reads in the dataset
# height takes in the axis length, hue sorts the data by species, and scatter_kws sets the size of the markers
# savefig() saves the plot as a .png file

def lm_plot( x_value, y_value,output_file):
    sns.lmplot (x = x_value, y = y_value, data = iris,height = 8,  hue = "class", scatter_kws = {"s": 50})
    plt.savefig (output_file)


# creating the lmplots using the following variables:
# (x and y variables, output name)

lm_plot("sepallength", "petallength", "lm_1.png")
lm_plot("sepallength", "sepalwidth", "lm_2.png")
lm_plot("petallength", "petalwidth", "lm_3.png")
lm_plot("sepalwidth", "petallength", "lm_4.png")
lm_plot("sepalwidth", "petalwidth", "lm_5.png")
lm_plot("sepallength", "petalwidth", "lm_6.png")


# function to create a boxplot/swarmplot 
# subplot() is used for multiple plots on the same graphic and takes arguments (row,column,plot no.)
# boxplot() creates the boxplot and takes in species type as x, variable as y, and data = dataset
# swarmplot() creates the swarmplot and like boxplot, takes in species type and variable as x + y,
# data = dataset, size = size of marker and color changes the colour of the marker point 
# close() closes the current data preventing it from "bleeding" into the next file 

def swarm_plt(variable, output):
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 3, color = "m")
    plt.savefig (output)
    plt.close()

swarm_plt("petalwidth", "boxplot_petal_w.png")
swarm_plt("petallength", "boxplot_petal_l.png")
swarm_plt("sepallength", "boxplot_sepal_l.png")
swarm_plt("sepalwidth", "boxplot_sepal_w.png")


# sunction to create a boxplot/swarmplot 
# subplot() is used for multiple plots on the same graphic and takes arguments (row,column)
# boxplot() creates the boxplot and takes in species type as x, variable as y, and data = dataset, axes determine postion on graph
# swarmplot() creates the swarmplot and like boxplot, takes in species type and variable as x + y, and axes
# data = dataset, size = size of marker and color changes the colour of the marker point 

f, axes = plt.subplots (2,2)
sns.boxplot(x = "class", y = "petalwidth", data = iris, ax = axes [0][0])
sns.swarmplot( x = "class", y = "petalwidth", data = iris, size = 1, color = "m", ax = axes [0][0])
sns.boxplot(x = "class", y = "petallength", data = iris, ax = axes [1][0])
sns.swarmplot( x = "class", y = "petallength", data = iris, size = 1, color = "m", ax = axes [1][0])
sns.boxplot(x = "class", y = "sepallength", data = iris, ax = axes [0][1])
sns.swarmplot( x = "class", y = "sepallength", data = iris, size = 1, color = "m", ax = axes [0][1])
sns.boxplot(x = "class", y = "sepalwidth", data = iris, ax = axes [1][1])
sns.swarmplot( x = "class", y = "sepalwidth", data = iris, size = 1, color = "m", ax = axes [1][1])

plt.tight_layout()
plt.savefig("box_swarm_plot.png")


# pairplot takes in the following variables to output the figure
# pairplot() takes in: data = dataset, "kind" sets the output type, "hue" sorts by species
# savefig() saves the output as a .png file   

figurepairplot = sns.pairplot(data = iris, kind = "scatter", hue = "class") 
plt.savefig ("pair-plot.png")
