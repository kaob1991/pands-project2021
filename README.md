# PANDS-Project 2021
Project work as part of PANDS module




##  Dataset Information and Context

Fisher's Iris dataset was introduced by the statistician Ronald Fisher in a 1936 paper called "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis. Linear discriminant analysis is the method used in statistics and other fields to find a linear combination of features that characterises or seperates two or more classes of objects or events. Fisher also was responsible for the development of the Analysis of Variance (ANOVA) test.   
The dataset consists of 150 instances, made up of  50 samples each of 3 species of iris. There were 4 features measured from each sample. These were - the length and width of the sepals and the length and width of the petals.
While one class  (or species) is linearly separable from the other 2; the others are NOT.

  

  ![](https://github.com/kaob1991/pands-project2021/blob/9f7a5f75a9bf6b480c4cbeb0c97157f3190e6eca/1_f6KbPXwksAliMIsibFyGJw.png)

Image showing different species included in the data set and items measured in the dataset.

​	(Source:https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)

This dataset is commonly used for machine learning, particularly in statistical classification techniques across multiple disciplines. It is widely considered to be a good option for illustrating problems in the areas of statistical graphics, multivariate statistics and machine learning. The UCI machine learning repository, often considered the source of the "true" dataset, contains well over 200 papers and books referencing the use of the dataset.  It comprises of real, good quality data, in a small but meaningful dataset which offers a simple but challenging task of discriminating between various types. In fact it is so popular that the dataset is readily available through the scikit-learn package, used in machine learning. 



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

- ```seaborn``` is a Python data visualisation library based on matplotlib that offers less-dated choices for plot style and color defaults than matplotlib, defines  simple high-level functions for common statistical plot types, and integrates with the functionality provided by Pandas DataFrames.

- ```matplotlib``` is a module for static, interactive & animated visualisations allowing high levels of customisation and the embedding of plots into applications; and   pyplot provides a MATLAB-like interface within this module. 

All of the above were pre-installed in python using anaconda. 

### Dataset 

 The dataset was retrieved from https://archive.ics.uci.edu/ml/datasets/iris as a csv (comma seperated values) file and imported into the program as follows: 

  ``` python
  
  iris = pd.read ("iris_csv.csv")
  
  ```

  I also created the output file:
   ``` python 
   out = open("summary_file_text_output.txt", "w")
   ```

 At this point I also performed a sanity check to ensure that there was no issues with the import of the libraries and to ensure that the read in of the dataset was problem-free.

 ### Basic Analysis

 I ran ```shape()``` to get the parameters of the data file, important for understanding the scope of the dataframe.

 ``` python
 print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)
print ("",file = out)
print ("", file = out)
 ```

This returned the following output which demonstrates that the datafile is 150 rows and 5 columns wide: 



![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/shape.png)



 I also used ```head()``` to demonstrate the layout of the file, and the various names of the variables 

``` python

print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)
print ("", file = out)
print ("", file = out)
```

Which returns the following details: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/head.png)

We can see from the output it shows that there are 5 variables, and 4 of them are of type float (sepal length, sepal width, petal length, petal width), and one string which is the species type (class). 


Running the data through ```describe()``` returned a basic numerical summary of the data containing the mean, max, standard deviation etc of the data file 
```python
print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)
print ("", file = out)
print ("", file = out)
```

This returned the following: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/describe.png)

Looking at the Standard Deviation we can see that it is relatively low for 3 of the 4 variable types ( petal width, sepal length, sepal width) with a number below 1. However the petal length has a higher standard deviation suggesting that there is more variability in the measurements of this particular variable than the others.


I established 3 different variable types ( 1 for each species of the flower) and also ran a numerical summary of each individual species, again using ```describe()```

```python
iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]


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
```

This returns the output for each individual species types: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/describe%20iris.png)

It gives a nice idea of the average real-life sizes of the flowers. It can be seen that, on average, the Iris Setosa has a large sepal compared to the petal, whereas the Iris Virginica and Versicolor's petals and sepals are closer in size. 


Finally, I completed a correlation on the datafile using ```corr()``` to demonstrate the relationship between the variables. This produces the relationship between them on a scale between 0 and 1, with 0 being no relationship detected, and 1 being a perfect correlation. 

```python
print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 
```

The results are as follows: 

![](https://github.com/kaob1991/pands-project2021/blob/13a5198bb8aaf833a1aa79d435061477ab345a04/correlation.png)


Looking at the data, it shows a high level of correlation between petal length and petal width (.962757) and also, to a lesser extent, between sepal length and petal length (.871754); and sepal length and petal width (.817954). We shall explore the following data further in the plotting investigations below. 
Following some external research I decided to also run a heatmap to better display the levels of correlation in a more visually accessible matter (see reference number 24 below). 
``` python
fig = plt.figure(figsize = (15,9))
sns.heatmap(iris_df.corr(), cmap = "Blues", annot = True)
```

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_correlation.png)

I also ran a correlation on the individual species' variables to explore the levels of correlation within, and again added heatmaps for ease of visibility. 

```python

print ("Correlation table within the Iris Setosa species", file = out)
print (iris_set.corr(), file = out)
print ("", file = out)
print ("Correlation table within the Iris Versicolor species", file = out)
print (iris_ver.corr(), file = out)
print ("", file = out)
print ("Correlation table within the Iris Virginica species", file = out)
print (iris_vir.corr(), file = out)
print ("", file = out)
```

![](https://github.com/kaob1991/pands-project2021/blob/6da0bdda0f840ea5d1822a0d7f661993d4b0421c/species%20correlation.png)

Iris Setosa:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_setosa.png)

Iris Versicolor:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_versicolor.png)

Iris Virginica:

![](https://github.com/kaob1991/pands-project2021/blob/ad0507feffa779bbc51e5fa42189a926e07067ae/heatmap_virginica.png)


The results show the following:
- Low/Moderate levels of correlation in Iris Setosa between the variables with the exception of the sepal width and length (.746780)
- High level of correlation in Iris versicolor between the petal length and petal width (.786668) and petal length and sepal length (.754049)
- Low/ Moderate levels of correlation in Irish Virginica between the variables with the exception of petal length and sepal length (.864225)



### Plotting Analysis

Following the summary analysis I then moved onto plotting the variables using a histogram. This will display the variables in a plot that shows the frequency that individual variables appear in the dataframe. 
I used the following sample code, making changes to color and labels as appropriate to adequately differentiate the variables. 

```python

plt.showplt.subplot(2,4,4)
plt.hist(iris["petalwidth"], color = "m")
plt.ylabel ("Frequency")
plt.xlabel ("Petal width (cm's)")
#plt.show()
plt.suptitle ("Histogram of the variables")
plt.savefig("variable_histograms.png")

```

This was the result of the histograms. 

![](https://github.com/kaob1991/pands-project2021/blob/31b1f8a58f3d973048cb5650bd59db76c317b0ac/variable_histograms.png)


Looking at the distribution of the curve in the first variable (The petal length) it can be seen that the curve is multimodal (i.e. it has 2 peaks) and the data is predominantly skewed to the right. The data of the variables in petal width follow no distribution curve and the data for the sepal length follows a very weak normal distribution. However the curve for the sepal width follows a normal distribution. 

Following some research into this distribution I discovered that the multimodal distribution was possibly a indication that the data needed to be further split into the relative species in order to fully determine the relationship see reference no 28). Therefore I then ran a histogram of each variable split by species to check the distribution at this point (see reference no. 27), using the sample code below: 

```python
plt.subplot(2,2,4)
plt.hist(iris_set["sepallength"], alpha = 0.75, label = "Iris Setosa", color = "m")
plt.hist(iris_ver["sepallength"], alpha = 0.5, label = "Iris Versicolour", color = "b")
plt.hist(iris_vir ["sepallength"], alpha = 0.5, label = "Iris Virginica", color = "g")
plt.xlabel ("Sepal Length (cm's)")
plt.ylabel ("Frequency")
plt.tight_layout()
plt.savefig ("variable_species_histograms.png")

```



This produced the following histogram, showing the variables split by species: 

![](https://github.com/kaob1991/pands-project2021/blob/c9db70603eeefeb7a5ac18a33bca46be1250870b/variable_species_histograms.png)



This gives a much clearer idea of what is going on with the individual species and looking at the image we can see that there is a normal distribution pattern amongst a number of species when looking at the variables. 



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
     
 22. Janert, PK 2010, Data Analysis with Open Source Tools : A Hands-On Guide for Programmers and Data Scientists, O'Reilly Media, Incorporated, Sebastopol. Available        from: ProQuest Ebook Central. [10 April 2021].

 23. https://methods.sagepub.com/base/download/DatasetHowToGuide/partial-correlation-in-fishers-iris-1936
        (retrieved 10/04/21 @ 14.38)
    
 24. https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
        (retrieved 10/04/21 @ 18.16)
     
 25. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
        (retieved 10/04/21 @ 20.39)
     
 26. https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
        (retrieved 10/04/21 @ 20.40)
     
 27. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
        (retrieved 15/04/21 @ 13.37) 
     
 28. https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/graphs/histogram/interpret-the-results/key-results/
        (retrieved 15/04/91 @ 13.54)  
     
 29. https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/demo_tight_layout.html   
       (retrieved 17/04/821 @ 17.37)
 30. 
