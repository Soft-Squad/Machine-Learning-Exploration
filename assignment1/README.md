# Assignment 1

 ### Problem 1
In Problem 1, I worked with a messy dataset containing 78 features related to the US Presidential Elections. The goal was to clean up the dataset and perform various aggregations and transformations on the data. Firstly, I identified and replaced nonsensical data with zero values, then split the FIPS feature into two discrete features: STATE and COUNTY. Next, I aggregated and categorized features related to education, religion, age, and ethnicity into new categorical or numerical features. Some features were removed, and canonical feature and category naming was applied using snake case naming. The dataset was then normalized using z-score normalization, and the new names, means, and standard deviations of population-related, income-related, and area-related features were reported. I also produced various visualizations including histograms, scatter plot, and box plot. I checked for conflicting and nonsensical samples, and identified the label vector. The final result was saved as "elections clean.csv", containing roughly 3145 rows and 23 columns.

### Problem 2
I implemented the ID3 decision-tree inference algorithm from scratch and used it to infer a decision tree from the cleaned-up US elections dataset (elections_clean.csv) that I generated in Problem 1. I used an entropy-based split criteria and only split on categorical features, avoiding the use of continuous features for splitting.

In addition, I calculated the impurity of a split using the Gini coefficient and compared the results to those obtained using entropy. I observed some differences in the two approaches, which I described in my report.

For evaluation purposes, I shuffled the dataset and used 70% of it for training and the remaining 30% for validation. I reported both the training and validation errors for all subproblems where applicable, as well as the maximum tree depth and the number of features that were repeated in decision stumps.

### Problem 4
So in Problem 2, I need to do something similar to what I did before, but this time I will use scikit-learn to create a decision tree instead of implementing ID3 on my own. Once I have both decision trees, I will compare them to see if they are similar or not and why that might be the case. I will also compare the error metrics to see if they are similar or different. I am allowed to use continuous features if I prefer.

### Problem 6
So far, I've been using decision trees primarily for binary classification. However, I learned that decision trees can also be used for regression. In order to try this out, I completed the following tasks:

I used the same setup as in Problem 2 and introduced two continuous features, per capita inc and deep pov all, to my decision tree implementation in addition to the existing categorical features. My goal was to predict deep pov all given other features (not the original label vector). I used mean to predict the poverty level for a leaf node, and I also used scikit-learn to get some extra points. As with Problem 2, I provided relevant metrics and plots to evaluate my results.

I rolled out my own 5-fold cross-validation to select the best regression tree. I was able to use any decision tree implementation, including my own or scikit-learn. The goal was to find the best tree to use for regression, based on the performance of the different models.

### Problem 7
In this problem, I used scikit-learn to implement a random forest consisting of 50 pre-pruned decision trees of depth 3. The dataset and features used were the same as in Problem 2, and I included the continuous features as well.

After training the random forest model, I generated standard training and test error plots and statistics to evaluate its performance. These metrics showed that the random forest model had a lower test error compared to the single decision tree model from Problem 2, indicating that the ensemble approach of random forests can help improve model accuracy.

Overall, implementing a random forest using scikit-learn allowed me to quickly and easily train and evaluate an ensemble of decision trees, and showed promising results for predicting poverty levels in the given dataset.

### Problem 8 
For this problem, I worked with a dataset containing movie scores from Rotten Tomatoes and IMDB. Here are the tasks I completed:

I used NumPy and pandas to perform closed matrix linear regression and predict the Rotten Tomatoes score given by critics based on the score given by users. I plotted a scatterplot of the data points and the linear fit (straight line).

I used scikit-learn to perform the same linear regression as in task 1.

I used scikit-learn to perform polynomial regression with quadratic and cubic polynomials instead of a simple linear regression. I plotted the fitted polynomials and the error bars.

I added an extra feature (IMDB) to predict the Rotten Tomatoes score and used scikit-learn to predict the regression parameters using simple linear features. I plotted the points in 3D space and the regression hyperplane.

I applied regression on all features to predict RottenTomatoes using ridge regression with different values for the regularization parameter lambda. We experimented with values of lambda = {0.1, 1, 2} and analyzed which one was the best. We also looked for features that were useless for predicting the Rotten Tomato score. We used a 70/30 split for testing and validation.

Overall, I explored different regression techniques and used them to predict the Rotten Tomatoes score based on user and critic ratings, as well as other features such as IMDB score. I also experimented with different regularization techniques to improve my predictions.

### Problem 9
Given a set of points from Github (https://gist.github.com/inumanag/ebb1566746aba800899e406f03c799c1), I am asked to use linear regression to fit a line (x-axis is the line number). If the fit is not perfect, I need to determine the best feature transformation to achieve a perfect fit, and prove it with a plot.
