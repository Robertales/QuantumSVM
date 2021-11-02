#!C:\Users\Gennaro\Miniconda3\envs\python\python.exe
#print("Content-Type: text/html\n")
#Import packages

import numpy as np
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler
import csv
import numpy
import os


filename = 'Iris.csv'
number=2
def featurextraction(filename,number):

    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    dataOfFile = numpy.array(x).astype('float')
    print(dataOfFile)

    print("--FEATURE EXTRACTION-")

    # dataset = datasets.load_iris()
    dataset = dataOfFile

    # Load the features
    X = dataset

    # View the shape of the dataset
    X.shape

    # View the data
    print(X.shape)

    # STANDARDIZE FUTURES
    # Create a scaler object
    sc = StandardScaler()

    # Fit the scaler to the features and transform
    X_std = sc.fit_transform(X)

    # Create a pca object with the 2 components as a parameter
    pca = decomposition.PCA(n_components=number)

    # Fit the PCA and transform the data
    X_std_pca = pca.fit_transform(X_std)

    # View the new feature data's shape
    X_std_pca.shape

    # write csv data
    if not os.path.exists('C:/xampp/htdocs/quantumKNN/python/yourPCA.csv'): numpy.savetxt('C:/xampp/htdocs/quantumKNN/python/yourPCA.csv', X_std_pca, delimiter=",", fmt='%s')
    else: np.savetxt('C:/xampp/htdocs/quantumKNN/python/yourPCA1.csv', X_std_pca, delimiter=",", fmt='%s')
    X
    # View the new feature data
    print("RESULTS:")
    print(X_std_pca)
    return X_std_pca


#print(featurextraction(filename,number))




