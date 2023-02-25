# Assignment 2

### Problem 1
I collected the MNIST dataset, which contains images of handwritten digits written by high school students and the U.S. Census Bureau employees. I installed Keras and loaded the dataset to classify these images using neural networks.

First, I calculated the gradient of the softmax function and implemented a simple one-layered neural network using only NumPy. I experimented with different learning rates and plotted the network's accuracy on test data against the number of iterations. I observed that the accuracy kept rising with the number of iterations.

Next, I used Keras to model and train the same network and compared the results. The Keras implementation was faster and more accurate than the one I built from scratch.

Then, I replaced the sigmoid activation function with ReLU and observed the effects on the network's performance.

After that, I added two hidden layers and used dropout and L2 regularization to create a three-layer deep neural network. I used cross-validation to select the best hyperparameters, which resulted in significant improvement in accuracy.

Finally, I modeled and trained a simple convolutional network with one convolutional layer, one pooling layer, and one fully connected layer. I experimented with different hyperparameters and observed a slight improvement in accuracy.

To conclude, I displayed nine images that were consistently misclassified by all the above models. I used matplotlib.pyplot.imshow() to plot these images and observed that some of them were difficult for me to classify correctly. For each model, I provided the corresponding training and test errors with the metrics of my choice. As a bonus, I used the leaky ReLU activation function for the artisan neural network I built from scratch.

### Problem 2
In this problem, I explored support vector machines for binary and multiclass classification using the sklearn library.

For binary classification, I trained a hard-margin SVM classifier to distinguish between images of ones and sevens from the MNIST dataset. However, the results were not very good, and it was difficult to achieve high accuracy. I then trained a soft-margin SVM classifier using cross-validation to select the best value of C and achieved better results.

Next, I experimented with different kernels for the best-performing soft-margin SVM classifier. I tried polynomial kernels of various degrees, a Gaussian kernel with various values of sigma, and a linear kernel.

Finally, I used the all-vs-all classification trick to train n(n-1) binary classifiers that distinguish between pairs of classes and implemented multiclass classification for all digits at once. I then plotted a confusion matrix to visualize the performance of all n2 classifiers.

For each model, I provided the corresponding training and test errors using metrics of my choice.

### Problem 3
I  downloaded the email dataset from http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron5.tar.gz and extracted the files. The dataset consists of spam and ham emails in separate directories. I represented each message as a bag of words and trained a Naive Bayes classifier using these bags of words to predict if an email is spam or not. I split the data into 70% for training and 30% for testing. I used this classifier to identify spam emails and get rid of those annoying spam texts!
