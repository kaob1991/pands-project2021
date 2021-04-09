# PANDS-Project 2021
Project work as part of PANDS module



##  Dataset Information and Context

Fisher's Iris dataset was introduced by the statistician Ronald Fisher in a 1936 paper called "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis. Linear discriminant analysis is the method used in statistics and other fields to find a linear combination of features that characterises or seperates two or more classes of objects or events. Fisher also was responsible for the development of the Analysis of Variance (ANOVA) test.   
The dataset consists of 150 instances, made up of  50 samples each of 3 species of iris. There were 4 features measured from each sample. These were - the length and width of the sepals and the length and width of the petals.
While one class  (or species) is linearly separable from the other 2; the others are NOT.

  

  ![](https://github.com/kaob1991/pands-project2021/blob/9f7a5f75a9bf6b480c4cbeb0c97157f3190e6eca/1_f6KbPXwksAliMIsibFyGJw.png)

Image showing different species included in the data set and items measured in the dataset.

​	(Source:https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)

This dataset is commonly used for machine learning, particularly in statistical classification techniques. It is widely considered to be a good option for illustrating problems in the areas of statistical graphics, multivariate statistics and machine learning. It comprises of real, good quality data, in a small but meaningful dataset which offers a simple but challenging tast of discriminating between various types. In fact it is so popular that the dataset is readily available through the scikit-learn package, used in machine learning. 



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
- NumPy imported as np 
- pandas imported as pd
- seaborn imported as sns
- matplotlib.pyplot imported as plt

- NumPy is a module which  supports large, multi-dimensional arrays and provides large collection of high-level mathematical functions which can be used on these arrays

- pandas is a high-level, powerful module used for real-world data analysis and data manipulation. It provides fast, flexible and expressive data structures designed to   make working with data both easy and intuitive 

- seaborn is a Python data visualisation library based on matplotlib that offers less-dated choices for plot style and color defaults than matplotlib, defines simple       high-level functions for common statistical plot types, and integrates with the functionality provided by Pandas DataFrames.

- matplotlib is a module for static, interactive & animated visualisations allowing high levels of customisation and the embedding of plots into applications; and pyplot   provides a MATLAB-like interface within this module. 

All of the above were pre-installed in python using anaconda. 

### Dataset 

 The dataset was retrieved from https://archive.ics.uci.edu/ml/datasets/iris as a csv file and imported into the program as follows: 
 
  ``` python
  
  iris = pd.read ("iris_csv.csv")
  
  ```

  I also created the output file:
   ``` python 
   out = open("summary_file_text_output.txt", "w")
   ```
  
 At this point I also performed a sanity check to ensure that there was no issues with the import of the libraries and to ensure that the read in of the dataset was problem-free.

 I ran ```shape()``` to get the parameters of the data file, important for understanding the scope of the dataframe
 ``` python
 print ("This is the shape of the datafile:\n(first number denotes the number of rows, the second the number of columns)", file = out)
print (iris.shape, file = out)
print ("",file = out)
print ("", file = out)
```

 I also used ```head()``` to demonstrate the layout of the file, and the various names of the variables 
``` python

print("General layout of Fisher's Iris datafile:", file = out)
print(iris.head(5), file = out)
print ("", file = out)
print ("", file = out)
```
      

### Basic analysis 

Running the data through ```describe()``` returned a basic numerical summary of the data containing the mean, max, std etc of the data file 
```python
print("Numerical summary of the datatypes:", file = out)
print(iris.describe(), file = out)
print ("", file = out)
print ("", file = out)
```


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

Finally, I completed a correlation on the datafile using ```corr()``` to demonstrate the relationship between the variables. This produces the relationship between them on a scale between 0 and 1, with 0 being no retaionship detected, and 1 being a perfect correlation. 
```python
print ("Correlation table between the various data types:", file = out)
print (iris.corr(), file = out) 
```

I then split the data by class using the following code 

``` python

iris_set = iris.loc [iris ["class"] == "Iris-setosa"]
iris_ver = iris.loc [iris ["class"] == "Iris-versicolor"]
iris_vir = iris.loc [iris ["class"] == "Iris-virginica" ]
 ```

and ran the ``` describe ``` function again to demonstrate a summary of the individual data types  

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
