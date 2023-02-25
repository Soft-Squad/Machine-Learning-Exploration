# Assignment 3

### Problem 1
The dataset was obtained from the GitHub repository and downsampled to 5,000 elements, with each class containing 500 items.

I ran PCA on the dataset and plotted the top 4 components. The components didn't seem to stand for anything in particular. To explain 75% of the variance, I needed 29 components. I randomly selected 3 examples and showed the difference between their projection to the 29-dimensional space and the original image.

I then selected the two topmost principal components and used them to plot the dataset as a 2D scatterplot. The scatterplot showed that different classes were well separated from each other, and I could distinguish classes without knowing the colours in advance.

Next, I ran t-SNE with parameters of my choice on this dataset. I plotted the result of t-SNE as a scatterplot and used the label vectors to colour different classes. This plot was more informative than the PCA-based one, as classes were even better separated in the t-SNE plot. I could easily distinguish classes based on their positions on the plot.

Overall, the Fashion-MNIST dataset was an interesting replacement for the old MNIST dataset, and both PCA and t-SNE helped me visualize the dataset and better understand the relationships between the different classes.

### Problem 2
I have implemented Lloyd's algorithm and hierarchical agglomerative clustering on the d-dimensional PCA projections of Fashion-MNIST images obtained in the previous problem.

For Lloyd's algorithm, I implemented two initialization techniques - random initialization and k-means++ initialization. I tried different values of k from 2 to 15 and ran the clustering multiple times for each value of k, picking the best result. I made a plot of the cost as k increased and used it to decide how many clusters to use. Based on the plot and the elbow method, I decided to use 10 clusters. The best clustering did not correspond perfectly to the true labels, and some classes did not entirely fall within a single cluster when k was less than or equal to 10.

For hierarchical agglomerative clustering, I used Euclidean distance for the dissimilarity measure between the examples and single linkage and average linkage for the dissimilarity measure between clusters. I used sklearn for this task. The clusters did not correspond perfectly to the true labels, and some classes were split across multiple clusters. I plotted the dendrogram and decided to make a cut at a certain point, based on the height of the branches and the resulting number of clusters. I chose the number of clusters that seemed to correspond most closely to the true labels.

Overall, clustering the d-dimensional PCA projections of the Fashion-MNIST images was a challenging task, and the resulting clusters did not correspond perfectly to the true labels. However, using both Lloyd's algorithm and hierarchical agglomerative clustering helped me better understand the relationships between the different classes in the dataset
