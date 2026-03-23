# Grid Search and Why Do it

Every ML model has settings called hyperparameters that we choose before training. 
They control how the model learns. For example our logistic regression model has:

- `C`: controls how strictly the model fits the data
- `max_iter`: how many attempts it gets to find the best solution
- `solver`: the algorithm it uses internally to optimize

Since there is no way to know upfront which combination of settings will produce 
the best model, we need to try them. Many of them.

## Why Grid Search

A single model trains in seconds even on a local machine, making a cluster unnecessary. But a grid search across four algorithms (Logistic Regression, Naive Bayes, SVM, Random Forest) with 5-fold cross validation produces upwards of 1,000 model trainings. A local machine would do this sequentialy taking upwards of hours to complete so we'd run this on the cluster.

To further demonstrate HPC necessity, we can also try 10-fold cross validation doubling the compute load to 2000+ model trainings. This makes the local vs HPC benchmark comparison more dramatic for the presentation. Also, I'm just curious 👉👈



