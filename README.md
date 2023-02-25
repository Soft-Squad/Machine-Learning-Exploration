# Machine-Learning-Exploration
 ## Coursework for SENG474 - Data Mining
 
 ## Assignment 1
 Here are some of the main goals from my first assignment. Each Assignment will have its own README that explains in depth my assignments.
 
 #### Data cleaning:
The main learning goal was to understand the importance of data cleaning and preparation before conducting any analysis or modeling.
The specific task was to clean and preprocess a dataset containing information about Airbnb listings in New York City.
The cleaning process involved dealing with missing values, handling categorical variables, and scaling numerical variables.

#### Decision trees:
The main learning goal was to understand the basics of decision trees and their implementation from scratch using Python.
The specific task was to implement the ID3 algorithm for building a decision tree classifier and apply it to a dataset containing information about breast cancer tumors.
The evaluation metrics used to assess the performance of the decision tree included accuracy, precision, recall, F1-score, and confusion matrix.
The scikit-learn library was also introduced as an alternative method for building decision trees.

 #### Random forests:
The main learning goal was to understand the concept and implementation of random forests as an ensemble learning technique.
The specific task was to implement a random forest on a dataset containing information about poverty rates in the Philippines and compare its performance with a single decision tree.
The evaluation metrics used to assess the performance of the random forest included training and test error plots, as well as statistics such as mean squared error and R-squared.

 #### Linear regression:
The main learning goal was to understand the concept and implementation of linear regression, including the closed-form solution and using scikit-learn for implementation.
The specific task was to apply linear regression to a dataset containing information about movie ratings, using the user rating to predict the critic's rating.
Other tasks included experimenting with polynomial regression and multiple regression, as well as applying ridge regression to all features in the dataset to predict the critic's rating.

#### Cross-validation:
The main learning goal was to understand the concept and implementation of cross-validation for model selection and validation.
The specific task was to implement 5-fold cross-validation to select the best regression tree from a decision tree implementation on a poverty rate dataset.

#### Feature transformation:
The main learning goal was to understand the importance of feature transformation in linear regression and how it can improve the accuracy of the model.
The specific task was to fit a line to a set of points using linear regression and then use feature transformation to achieve a perfect fit.
        
## Assignment 2

#### Neural Nets:
In terms of neural networks, I discussed the basic architecture of feedforward neural networks and how they can be trained using backpropagation. I also talked about the importance of hyperparameters like the number of hidden layers, the number of neurons per layer, and the learning rate. Additionally, I covered regularization techniques like L1 and L2 regularization, and dropout. The main learning goals for this topic were to understand the basic architecture of feedforward neural networks and how to train them using backpropagation, as well as the importance of hyperparameters and regularization in neural network training.

#### Suport Vector Machines:
For support vector machines, I discussed how they can be used for binary classification tasks and how to train both hard and soft-margin SVM classifiers. I also explored different kernels such as polynomial, Gaussian, and linear kernels, and how to use them to improve the classification accuracy. Finally, I looked at how to use the all-vs-all (AVA) classification trick to extend SVMs to multiclass classification problems. The main learning goals for this topic were to understand the basic concepts behind SVMs, how to train them for binary classification tasks, how to use different kernels to improve classification accuracy, and how to extend SVMs to multiclass classification problems using the all-vs-all classification trick.

#### Naive Bayes:
Regarding Naive Bayes, I focused on its application to text classification tasks, specifically spam detection. I discussed how to represent each email as a bag of words and how to use this representation to train a Naive Bayes classifier. I also talked about the importance of splitting the data into training and test sets to evaluate the performance of the classifier. The main learning goals for this topic were to understand how to represent text data using the bag-of-words model, how to train a Naive Bayes classifier for text classification, and how to evaluate the performance of the classifier using a test set.

## Assignment 3

#### PCA & t-SNE Decompositon:
The first task was to perform PCA on the dataset and plot the top 4 components. The number of components needed to explain 75% of the variance was determined by the elbow method, which resulted in 39 components. The dataset was then projected to 2D using the top two components and plotted as a scatterplot with classes colored according to their labels. Both PCA and t-SNE were used to visualize the dataset, and it was found that t-SNE provided a more informative plot than PCA.

#### Lloyd's Algorithm (KMeans):
The second task was to implement Lloyd's algorithm and hierarchical agglomerative clustering on the d-dimensional PCA projections of Fashion-MNIST images. Two initialization techniques for Lloyd's algorithm were implemented, and the algorithm was run for different values of k from 2 to 15. The cost was plotted against k to determine the optimal number of clusters to use. Hierarchical agglomerative clustering was also performed, and the dendrogram was plotted to decide the final clustering.
