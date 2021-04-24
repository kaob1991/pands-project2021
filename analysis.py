# Program to analyse and produce plots from a dataset imported into the program 

# This dataset is fisher's dataset and we will be obtaining a summary of each variable 
# saving it to a text output and then saving a histogram of each variable to a png file 

# Author: Katie O'Brien 


# Importing required libraries for the dataset analysis
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

# reading in the csv iris datafile
iris = pd.read_csv ("iris_csv.csv")

# Outputting the data to a .txt file, the "w" ensures the file will be
# overwritten each time the program is ran 
out = open("summary_file_text_output.txt", "w")



# Sanity check to ensure all libraries and file for reading in is correctly loading

# print ("all okay") 
# Commented out post check as it is not required for the program


# Using shape() to get the size and shape of the datafile, confirming the number of
# rows in the dataset is 150 as expected;
# and printing the header for ease of differentiation between various outputs

print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)
print ("",file = out) # This is for empty rows for formatting
print ("", file = out)


# And demonstrating the layout of the datafile using head() 

print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)
print ("", file = out)
print ("", file = out)


#This provides a numerical summary of the data including mean max std etc using describe()
# and outputs it to the datafile above 


print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)
print ("", file = out)
print ("", file = out)

# After running the initial analysis the data was then divided
# into the corresponding "class", ie species of flower using loc()

iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]


# running a summary of the data sorted by class using describe() 


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


# Demonstrating the correlation between the various variable types using corr()


print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 
print ("", file = out)
print ("", file = out)


# Demonstrating a heatmap for the correlations above using heatmap() 
# cmap determines the colours used and annot writes the data value in each cell


fig = plt.figure(figsize = (8,3))
sns.heatmap(iris.corr(),cmap = "Blues", annot = True)
plt.savefig ("heatmap_correlation.png")


# Demonstrating the correlation within each individual species and creating heatmaps for each


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


#Creating a histogram function that will save to a png file
# subplot() is used for multiple plots on the same graphic and takes arguments (row,column,plot no.)
# hist() takes in a variable, and the colour of the histogram 
# x/ylabel() takes in the axis names
# suptitle() takes in the overall name of all 4 plots
# tight_layout() resizes the fonts of the plots to make them all fit better in the graphic 
# savefig() saves the plots to a .png file name set below 

def hist_var (n, variable, col, x_label,):
    plt.subplot(2,2,n)
    plt.hist(iris[variable], color = col)
    plt.ylabel ("Frequency")
    plt.xlabel (x_label)
    plt.suptitle ("Variable Distribution")
    plt.tight_layout()
    plt.savefig("variable_histograms.png")


# The below 4 lines are generating a histgram plot using the function above
# plot number (x of 4), variable_name, colour, and title for x axis  

hist_var (1, "sepallength", "b", "Sepal Length")
hist_var (2, "petallength", "r", "Petal Length")
hist_var (3, "sepalwidth", "g", "Sepal Width")
hist_var (4, "petalwidth", "m", "Petal Width")


# fuction created for a histogram colour coded by species in order to see spread more clearly
# details similar to above histogram with a few extra additions within hist()
# alpha = denotes the transparancy of the bars, allowing overlapping variables to still be seen
# label = labels the colours allowing a legend to also be displayed
# x/ylabel sets the titles on the axis
# tight_layout() resizes the fonts of the plots to make them all fit better in the graphic 
# savefig() saves output as a .png file

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
'''

# The 4 lines below are creating a histogram for each 
# The variables are as follows: plot number (x of 4), variable, x-axis label

'''
hist_func (1, "petalwidth", "Petal Width (cm's)")
hist_func (2, "petallength", "Petal length (cm's)")
hist_func (3, "sepalwidth", "Sepal Width (cm's)")
hist_func (4, "sepallength", "Sepal Length (cm's)")
'''

# Defining a function for scatterplot analysis with variables
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


# Creating the scatterplots using each variable as required. The variables are as follows 
#  (X and Y axes labels, x and y variables, output_name)


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


# Creating the lmplots using the following variables
# (x and y variables, output name)


lm_plot("sepallength", "petallength", "lm_1.png")
lm_plot("sepallength", "sepalwidth", "lm_2.png")
lm_plot("petallength", "petalwidth", "lm_3.png")
lm_plot("sepalwidth", "petallength", "lm_4.png")
lm_plot("sepalwidth", "petalwidth", "lm_5.png")
lm_ plot("sepallength", "petalwidth", "lm_6.png")


# Function to create a boxplot/swarmplot 
# subplot() is used for multiple plots on the same graphic and takes arguments (row,column,plot no.)
# boxplot() creates the boxplot and takes in species type as x, variable as y, and data = dataset
# swarmplot() creates the swarmplot and like boxplot, takes in species type and variable as x + y,
# data = dataset, size = size of marker and color changes the colour of the marker point 


def swarmbox_plt(n, variable):
    plt. subplot (2,2,n)
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 1, color = "m")


# the following 4 lines create the equivalent plots using the following variables
# (plot number, variable type)


swarmbox_plt(1, "petalwidth")
swarmbox_plt(2, "petallength")
swarmbox_plt(3, "sepallength")
swarmbox_plt(4, "sepalwidth")


# the next 2 lines set the display plot
# tight_layout() resizes the fonts of the plots to make them all fix better in the graphic 
# savefig() saves output as a .png file


plt.tight_layout()
plt.savefig("box_swarm_plot.png")


#swarmplot/boxplot for individual variables 
# boxplot() creates the boxplot and takes in species type as x, variable as y, and data = dataset
# swarmplot() creates the swarmplot and like boxplot, takes in species type and variable as x + y,
# data = dataset, size = size of marker and color changes the colour of the marker point 
# savefig() saves output as a .png file

'''
def swarm_plt(variable, output):
    #plt.figure()
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 3, color = "m")
    plt.savefig (output)
'''

# creating the swarm/box plots using the function above & the following variables
# (variable, output file name)

'''
swarm_plt("petalwidth", "boxplot_petal_w.png")
swarm_plt("petallength", "boxplot_petal_l.png")
swarm_plt("sepallength", "boxplot_sepal_l.png")
swarm_plt("sepalwidth", "boxplot_sepal_w.png")
'''

# pairplot takes in the following variables to output the figure
# pairplot() takes in: data = dataset, "kind" sets the output type, "hue" sorts by species
# savefig() saves the output as a .png file   


figurepairplot = sns.pairplot(data = iris, kind = "scatter", hue = "class") 
plt.savefig ("pair-plot.png")
