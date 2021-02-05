# Assignment 1 | Machine, Data and Learning

## Task 1

The function `LinearRegression().fit()` is a combination of two statements:  
- `LinearRegression()` creates an instance of the class LinearRegression which is used as our Regression model.  
        Usage: `model = LinearRegression()`  
- `fit()` is used to fit the model to the given dataset  
        Usage: `model.fit(input, output)`  

So `model = LinearRegression().fit(input, output)` creates a linear regression model and fits it to a given input and output dataset.  

`LinearRegression().fit()` fits a linear model with coefficents w = (w1, ..., wp) to minimize the residual sum of squares between the observed targets and the targets predicted by the linear approximation, i.e. Minimise the Sum of Squared Errors.

## Task 2

As functional classes change, with incresing degree we observe:
- Bias trend-
    - For degree *3*, the bias graph takes deep dive, then gradually reduces till degree *9*.
    - After that the bias unevenly increases till degree *14*.
    - Then it keeps increasing from there.
    - **Note that** just the general trend of bias falling till approximately degree *10* and then increasing is common, while the other details are case dependent.
- Variance trend:
    - It keeps increasing monotonically till degree *11*.
    - Then it oscillates in a range of *5000*.
    - Then it again increases monotonicalls.
    - **Note that** just the general trend of variance rising till approximately degree *14*, not varying for another *3-4* degrees and then increasing is common, while the other details are case dependent.

## Task 4

