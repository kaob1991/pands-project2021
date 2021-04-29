# PANDS-Project 2021


Project work as part of the Programming and Scripting module in partial fulfillment of a H.Dip in Data Analytics in Computing. 
Student number G00398250 (Katie O'Brien)

See "issues" within this repository for a to-do list which provides evidence of planning and workflow for this project. 

##  Dataset Information and Context

Fisher's Iris dataset was introduced by the statistician Ronald Fisher in a 1936 paper called "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis. Linear discriminant analysis is the method used in statistics and other fields to find a linear combination of features that characterises or separates two or more classes of objects or events. Fisher was also responsible for the development of the Analysis of Variance (ANOVA) test.   
The dataset consists of 150 instances, made up of  50 samples each of 3 species of iris. There were 4 features measured from each sample. These were - the length and width of the sepals and the length and width of the petals.
While one class  (or species) is linearly separable from the other 2; the others are NOT.

  

  ![](https://github.com/kaob1991/pands-project2021/blob/9f7a5f75a9bf6b480c4cbeb0c97157f3190e6eca/1_f6KbPXwksAliMIsibFyGJw.png)

Image showing different species included in the data set and items measured in the dataset.

​	(Source:https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)

This dataset is commonly used for machine learning, particularly in statistical classification techniques across multiple disciplines. It is widely considered to be a good option for illustrating problems in the areas of statistical graphics, multivariate statistics. The UCI repository, often considered the source of the "true" dataset, contains well over 200 papers and books referencing the use of the dataset.  It comprises of real, good quality data, in a small but meaningful dataset. This offers a simple but challenging task of discriminating between various types. In fact it is so popular that the dataset is readily available through the scikit-learn package, used in machine learning and statistical modelling. 



### The attributes of the dataset is as follows: 

1. Sepal length in cm's

2. Sepal width in cm's

3. Petal length in cm's 

4. Petal width in cm's 

5. Class:

   -Iris Setosa

   -Iris Versicolour

   -Iris Virginica 
   
## Dataset Analysis

### Libraries Used
- ```NumPy``` imported as ```np``` 
- ```pandas``` imported as ```pd```
- ```seaborn``` imported as ```sns```
- ```matplotlib.pyplot``` imported as ```plt```

- ```NumPy``` is a module which  supports large, multi-dimensional arrays and provides large collection of high-level mathematical functions which can be used on these arrays

- ```pandas``` is a high-level, powerful module used for real-world data analysis and data manipulation. It provides fast, flexible and expressive data structures          designed to make working with data both easy and intuitive 

- ```seaborn``` is a Python data visualisation library based on matplotlib that offers less-dated choices for plot style and colour defaults than matplotlib, defines  simple high-level functions for common statistical plot types, and integrates with the functionality provided by Pandas DataFrames.

- ```matplotlib``` is a module for static, interactive & animated visualisations allowing high levels of customisation and the embedding of plots into applications; and pyplot provides a MATLAB-like interface within this module. 

All of the above were pre-installed in python using anaconda 3, and the code was written using VSCode. 

### Dataset 

 The dataset was retrieved from https://archive.ics.uci.edu/ml/datasets/iris as a csv (comma separated values) file and imported into the program as follows: 

  ``` python
  
  iris = pd.read_csv ("iris_csv.csv")
  
  ```

  The output file was also created, which is set to overwrite each time the program is run:

   ``` python 
   out = open("summary_file_text_output.txt", "w")
   ```

 At this point a sanity check was also performed to ensure that there was no issues with the import of the libraries and to ensure that the read in of the dataset was problem-free.

 ### Basic Analysis
 
 #### Shape()

```shape()``` was ran to get the parameters of the data file, important for understanding the scope of the data frame. It's also important to ensure that the correct dataset is in use as there are many variants of the dataset available on the internet; and using a different version will produce incorrect outputs.

 ``` python
 print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)

 ```

This returned the following output which demonstrates that the datafile is 150 rows and 5 columns wide: 



![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/shape.png)

#### Head()

```head()``` was also used to demonstrate the layout of the file, and the various names of the variables 

``` python

print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)

```

Which returns the following details: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/head.png)

We can see from the output it shows that there are 5 variables, and 4 of them are of type float (sepal length, sepal width, petal length, petal width), and one string which is the species type (class). 


#### Describe()


Running the data through ```describe()``` returned a basic numerical summary of the data containing the mean, max, standard deviation etc. of the data file 
```python
print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)

```

This returned the following: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/describe.png)

Looking at the Standard Deviation we can see that it is relatively low for 3 of the 4 variable types ( petal width, sepal length, sepal width) with a number below 1. However the petal length has a higher standard deviation suggesting that there is more variability in the measurements of this particular variable than the others.


3 different variable types were then established (1 for each species of the flower) and a numerical summary of each individual species was run, again using 
```describe()```:

```python
iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]


print ("Numerical summary of the Iris Setosa", file = out)
print (iris_set.describe(), file = out)

print ("Numerical summary of the Iris Versicolor", file = out)
print (iris_ver.describe(), file = out)

print ("Numerical summary of the Iris Virginica", file = out)
print (iris_vir.describe(), file = out)

```

This returns the output for each individual species types: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/describe%20iris.png)

It gives an accurate idea of the average real-life sizes of the flowers. It can be seen that, on average, the Iris Setosa has a large sepal compared to the petal, whereas the Iris Virginica and Versicolor's petals and sepals are closer in size. 


#### Correlation & Heatmaps


Finally, a correlation was run on the datafile using ```corr()```, to demonstrate the relationship between the variables. This produces the relationship between them on a scale between 0 and 1, with 0 being no relationship detected, and 1 being a perfect correlation. 

```python
print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 

```

The results are as follows: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/correlation.png)


Looking at the data, it shows a high level of correlation between petal length and petal width (.962757) and also, to a lesser extent, between sepal length and petal length (.871754); and sepal length and petal width (.817954). We shall explore the following data further in the plotting investigations below. 

Following some external research it was decided to also run a heatmap to better display the levels of correlation in a more visually accessible matter (see reference number 24 below). 

``` python
fig = plt.figure(figsize = (8,3))
sns.heatmap(iris.corr(), cmap = "Blues", annot = True)
```

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_correlation.png)

A correlation was also run on the individual species' variables to explore the levels of correlation within, and again, heatmaps were added for for ease of visibility. 

```python

print ("Correlation table within the Iris Setosa species", file = out)
print (iris_set.corr(), file = out)

print ("Correlation table within the Iris Versicolor species", file = out)
print (iris_ver.corr(), file = out)

print ("Correlation table within the Iris Virginica species", file = out)
print (iris_vir.corr(), file = out)

```

![](https://github.com/kaob1991/pands-project2021/blob/6da0bdda0f840ea5d1822a0d7f661993d4b0421c/species%20correlation.png)

Iris Setosa Heatmap:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_setosa.png)

Iris Versicolor Heatmap:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_versicolor.png)

Iris Virginica Heatmap:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_virginica.png)


The results show the following:

- Low/Moderate levels of correlation in Iris Setosa between the variables with the exception of the sepal width and length (.746780)
- High level of correlation in Iris versicolor between the petal length and petal width (.786668) and petal length and sepal length (.754049)
- Low/ Moderate levels of correlation in Irish Virginica between the variables with the exception of petal length and sepal length (.864225)



### Plotting Analysis

#### Histograms


Following the summary analysis the variables were then plotted using a histogram. This will display the variables in an easy-to-read graphic that shows the frequency that individual variables appear in the data frame. 

The following sample code was used, making changes to colour and labels as appropriate to adequately differentiate the variables. 

```python
f, axes = plt.subplots (2,2)
sns.histplot(iris, x = "sepallength", label = "small", color = "green", kde = True, ax = axes [0][0]	
plt.savefig("variable_histograms.png")


```

This was the result of the histograms. 

![](https://github.com/kaob1991/pands-project2021/blob/5589bee8938fe2b37d7be2469a78dba091667937/variable_histograms.png)


Looking at the distribution of the curves:

- In 'petal length' it can be seen that the curve is multimodal (i.e. it has 2 peaks) and the data is predominantly skewed to the left. 

- The data of the variables in 'petal width' follows no clear distribution curve

- The data for 'sepal length' follows a very weak normal distribution. 

- The curve for the 'sepal width' follows a normal distribution. 

Following some research into this distribution it was discovered that the multimodal distribution was possibly a indication that the data needed to be further split into the relative species in order to fully determine the relationship (see reference no 28).
Therefore a histogram of each variable was then run, split by species to check the distribution at this point (see reference no. 27), using the sample code below: 

```python

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

```



This produced the following histogram, showing the variables split by species: 

![](https://github.com/kaob1991/pands-project2021/blob/c9db70603eeefeb7a5ac18a33bca46be1250870b/variable_species_histograms.png)



This gives a much clearer idea of what is going on with the individual species; and looking at the image we can see that there is a normal distribution pattern amongst a number of species when looking at the variables. Looking at the relationship between the 3 variables it is very clear that, as mentioned at the beginning, the Iris Setosa is linearly separable from the others when looking at the Petals. The Sepals are also normally distributed in both width and length. 
The other 2 species are both normally distributed as well, but there are significant amounts of overlap, particularly in the Sepal. The petal's appear to be less so with the Virginica species clearly averaging a slightly larger size. 


While histogram's give a great overview of the data itself, they do not plot the individual data points, so for that we need to use a scatterplot to see the relationship between the variables. 


### Further Detailed Analysis 

#### Scatterplots

Scatterplots are a quick and simple way to look at the relationship between the variables, and easier for the inexperienced user to interpret the data. 

We will run a scatterplot between each variable and set the code to output a .png file for convenience. Following research on whether to use ```plt.plot``` or ```plt.scatter``` it was decided that as we are going to be running all 3 varieties of Iris in the dataset we will be using ```plt.scatter```, as it offers the added colour customisation that we need to clearly demonstrate the data (see reference no. 31). A sample of code used is below: 

``` python

def scatter_func (x_name,y_name,x_variable,y_variable,output_name):
   plt.figure()
   plt.xlabel (x_name)
   plt.ylabel (y_name)
   sns.scatterplot (x_variable, y_variable , data = iris, hue = "class")
   plt.savefig(output_name)
scatter_func ("Sepal Length", "Petal Length", "sepallength", "petallength", "SlengthPlength.png")

```
This resulted in the following scatterplots: 


Sepal width + Sepal length: 

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/SWidthSLength.png)



Sepal length + Petal length:

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/SlengthPlength.png)



Sepal length + Petal width:

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/SlengthPwidth.png)


Sepal width + Petal length:

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/SwidthPlength.png)



Sepal width and Petal width:

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/SwidthPwidth.png)


Petal width and Petal length:

![](https://github.com/kaob1991/pands-project2021/blob/f7b14c092f5a3eb72ddfc7f58704ec8a05c55174/PwidthPlength.png)


Looking at the above it is easy to see whether a relationship exists between the variables depending on how close the individual dots come to form an imaginary diagonal line that runs on the graph. If the line starts in the bottom left to top right it can be said to have a positive linear correlation; and if it starts in the bottom right to top left then it can be said to have a negative  linear correlation. The more spread out the dots from this line, the weaker the correlation. 

When we look at the scatterplots from our data there are a number of relationships shown. A summary of the results is below :

  1) Sepal Width and Sepal Length:
      There appears to be no clear relationship when looking at the variables as an overall. Iris Setosa and Versicolor have a weak positive relationship between the 2         variables

  2) Sepal length and Petal length:
      There appears to be a positive linear relationship between the variables overall. However, looking at the data for each species shows that Iris Setosa has no             relationship between the variables (the data is in a relatively straight line across the graph). Versicolor and Virginica have a strong positive correlation             between the variables. 

  3) Sepal length and Petal width:
      There is a weak positive correlation with the variables in this dataset overall. The individual species all appear to have a weak positive relationship but again,       the Iris Setosa has the weakest with the data only slightly showing a positive correlation. 

  4) Sepal width and Petal length:
      There is a weak positive correlation between these 2 data variables, only in Versicolor and Virginica. The data points are rather spread out suggesting a wide           range of variation in the data. Iris Setosa again have no correlation between the variables.

  5) Sepal width and petal width:
      There is a weak positive correlation between these 2 data variables, but like the scatterplot above, only with Versicolor and Virginica. The data points are spread       out suggesting a wide range of data variation. Iris Setosa appears to have no correlation between the variables, as above. 

  6) Petal width and Petal length:
      There is a strong positive correlation between the data in this scatterplot. The data points for Iris Setosa and Versicolor are tightly packed around the diagonal,       while Virginica is slightly less densely packed, suggesting a greater variation in the data gathered for that particular species. 
      

#### Linear Model Plots

While Scatterplots are a great way to see the data clearly presented there a number of other ways to present the data. For example ```sns.lmplot``` offers a linear regression model which plots the data as the scatterplots above, but overlays a overplot line on the data to make the linear regression clearer. An example of this data is shown below and is a helpful way of visualising the data further. The other 5 plots relevant to the data are available in the repository for viewing if required. The sample code is below: 

``` python 
def lm_plot( x_value, y_value,output_file):
    sns.lmplot (x = x_value, y = y_value, data = iris,height = 8,  hue = "class", scatter_kws = {"s": 50})
    plt.savefig (output_file)
lm_plot("sepallength", "petallength", "lm_1.png")
```

We can see with this graph it gives a linear regression model allowing the relationship with the data to be clearly shown: 
![](https://github.com/kaob1991/pands-project2021/blob/816989d460976bee9092167c9b946230b4a2ed54/lm_1.png)


#### Boxplot/Swarmplot

Another way is to present the data as a boxplot overlaid with a swarm plot and this allows the data to be displayed in a clear and concise matter. The visualisation draws attention to the data in the following manner. The sample code used is below for each variable, modifying the variable and plot position: 

```python 
f, axes = plt.subplots (2,2)
sns.boxplot(x = "class", y = "petalwidth", data = iris, ax = axes [0][0])
sns,swarmplot(x = "class", y = "petalwidth", data = iris, size = 1, color = "m", ax = axes [0][0])


plt.tight_layout()
plt.savefig("box_swarm_box.png)

```

The following modifications were made to the code for the individual plots to prevent the variables from carrying over into the next:

```python

def swarmbox_plt(variable, output):
    sns.boxplot(x = "class", y = variable, data = iris)
    sns.swarmplot( x = "class", y = variable, data = iris, size = 3, color = "m")
    plt.savefig(output)
    plt.close()
swarmbox_plt("petalwidth", "boxplot_petal_w")
```

The images below demonstrate the data from petal length; and an overview plot. The overview plot is difficult to see and as a result I have included the other 3 plots in the repository for analysis. 

![](https://github.com/kaob1991/pands-project2021/blob/9628aad3deac12fa662b2e2e4bc670f1261f6a96/boxplot_petal_l.png)

![](https://github.com/kaob1991/pands-project2021/blob/9628aad3deac12fa662b2e2e4bc670f1261f6a96/box_swarm_plot.png)

Boxplots give a good indication of how the data values are spread out. It uses the box to demonstrate the IQR (Interquartile range) between the 25th and 75th percentile, with the vertical lines ("whiskers") representing the data to the "maximum" and "minimum" horizontal lines on both sides. 

Swarm plots (also called bee swarm plots, as they can sometimes resemble swarming bees),are useful to show all data points with some representation of underlying distribution. They are similar to strip-plots but the points are adjusted so that they don't overlap. 

#### Pair Plot


Finally the presentation of the data as a pair plot graph is both concise and visually striking. The use of seaborn allows the data to be presented in a easy to read manner and is equally straightforward in its display of the scatterplot and histogram data. It produces a matrix of relationships between each variable in the dataset for an instant examination of the data and even allows the data to be split by species type. The code used is equally straightforward and is demonstrated below: 

```python 
figurepairplot = sns.pairplot(data = iris, kind = "scatter", hue = "class") 
plt.savefig ("pair-plot")
```

![](https://github.com/kaob1991/pands-project2021/blob/9628aad3deac12fa662b2e2e4bc670f1261f6a96/pair-plot.png)


### Conclusion 

There are many reasons to use Python over other software and coding packages that are available. Compared, for example to program's such as IBM's SPSS (Statistical Package for Social Sciences), Python provides a far greater level of customisation for data analysis. 

Python provides a huge range of extremely powerful packages such as NumPy, pandas, seaborn, and matplotlib that make it incredibly simple to code complex data analytics problems. It's relatively easy to use and understand, particularly when compared to other lower level programming languages such as C # or java , which require a greater level of knowledge and understanding to perform the same tasks. Programs can be processed relatively quickly, which is another benefit of using the likes of python over other languages or software packages.

Another advantage of using Python over something like Microsoft Excel or SPSS is reproducibility. This both saves time, and ensures consistency. As the programmer has control over the code being written, reproducing the same data is easier, be that with the same dataset, an updated one, or even different sets when looking for the same analysis to be run. The downside to using something like Excel is that to receive the same data output the data analyst has to manually remember complete the sequence of steps taken when originally performing the analysis. 

The above project shows how easy it is to quickly and concisely display a dataset in a graphical display which allows for analysis of the data with minimal effort. It also allows the presentation of the information to others in an easily-understandable manner. There is plenty of anal available on the Iris dataset and research (including the references listed below) provided some interesting inspiration for the analysis of this dataset in this project. 


## REFERENCES:

1. Https://en.wikipedia.org/wiki/Iris_flower_data_set 
    (retrieved 17/03/2021 @ 18.00)
    
2. https://archive.ics.uci.edu/ml/datasets/iris

    (retrieved 17/03/2021 @18.30)

3. https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 
     (retrieved 1/04/21 @ 18.43)
     
4. https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x 
     (retrieved 1/04/21 @ 18.56)
     
5. https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
     (retrieved 1/04/21 @ 19.00)

6. https://datahub.io/machine-learning/iris#data
     (retrieved 02/04/21 @ 18.51) 

7. https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching
     (retrieved 06/04/21 @ 16.34)
     
8. https://www.nature.com/articles/s41586-020-2649-2.pdf
     (retrieved 06/04/21 @ 16.50)
     
9. https://pypi.org/project/pandas/ 
     (retrieved 06/04/21 @ 16.58)
     
10. https://seaborn.pydata.org/
      (retrieved 06/04/21 @ 17.00)

11. https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
      (retrieved 06/04/21 @ 17.03)

12. https://matplotlib.org/
      (retrieved 06/04/21 @ 17.09)

13. https://blog.bitsrc.io/how-to-write-beautiful-and-meaningful-readme-md-for-your-next-project-897045e3f991
      (retrieved 06/04/21 @ 18.09)
    
14. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d 
      (retrieved 06/04/21 @ 18.41)

15. https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b
      (retrieved 06/04/21 @ 18.41)
    
16. https://www.researchgate.net/post/What-do-you-consider-a-good-standard-deviation
      (retrieved 9/04/21 @ 18.45)

17. https://www.statisticshowto.com/probability-and-statistics/correlation-analysis/
      (retrieved 9/04/21 @ 19.07)
    
18. https://www.statisticssolutions.com/pearsons-correlation-coefficient/#:~:text=High%20degree%3A%20If%20the%20coefficient,When%20the%20value%20lies%20below%20%2B%20.&text=No%20correlation%3A%20When%20the%20value%20is%20zero.
      (retrieved 9/04/21 @ 20.02) 

 19. https://github.com/TracyRenee61/Misc-Predictions/blob/main/Iris_sklearn.ipynb
       (retrieved 10/04/21 @ 13.51)
     
 20. https://blog.revolutionanalytics.com/2014/08/the-iris-data-set-for-big-data.html
        (retrieved 10/04/21 @ 13.54)
     
 21. Pearson, E. (1951). Biometrika, 38(1/2), 257-259. doi:10.2307/2332332
        (retrieved 10/04/21 @ 14.03)
     
 22. Janert, PK 2010, Data Analysis with Open Source Tools : A Hands-On Guide for Programmers and Data Scientists, O'Reilly Media, Incorporated, Sebastopol. Available        from: ProQuest Ebook Central. (retrieved 10/04/21 @ 14.16)

 23. https://methods.sagepub.com/base/download/DatasetHowToGuide/partial-correlation-in-fishers-iris-1936
        (retrieved 10/04/21 @ 14.38)
    
 24. https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
        (retrieved 10/04/21 @ 18.16)
     
 25. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
        (retrieved 10/04/21 @ 20.39)
     
 26. https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
        (retrieved 10/04/21 @ 20.40)
     
 27. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
        (retrieved 15/04/21 @ 13.37) 
     
 28. https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/graphs/histogram/interpret-the-results/key-results/
        (retrieved 15/04/91 @ 13.54)  
     
 29. https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/demo_tight_layout.html   
       (retrieved 17/04/821 @ 17.37)
     
 30. https://datavizpyr.com/overlapping-histograms-with-matplotlib-in-python/
       (retrieved 17/04/21 @ 20.18)

 31. https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
       (retrieved 17/04/21 @ 20.47)
     
 32. https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
        (retrieved 17/04/21 @ 21.04)

 33. https://www.ck12.org/book/ck-12-probability-and-statistics-concepts/section/4.6/
        (retrieved 18/04/21 @ 17.40)
     
 34. https://stackoverflow.com/questions/34796451/changing-the-marker-size-in-python-seaborn-lmplot
	(retrieved 19/04/21 @ 18.00)

 35. https://www.geeksforgeeks.org/python-seaborn-swarmplot-method/
	(retrieved 19/04/21 @ 18.25)

 36. https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
	(retrieved 24/04/21 @ 14.20)

 37. https://www.kite.com/python/docs/seaborn.swarmplot
	(retrieved 24/04/21 @ 14.21) 

 38. https://www.reddit.com/r/datascience/comments/8ggvx4/why_python_over_excel/
	(retrieved 24/04/21 @ 19.28)
	
 39. https://stackoverflow.com/questions/50294951/python-boxplot-on-single-variables
	(retrieved 27/04/21 @ 20.10)
	
 40. https://www.kaggle.com/residentmario/subplots
 	(retrieved 27/04/21 @ 22.08)
