import random
import numpy as np
from numpy.random import choice
from sklearn.neighbors import NearestNeighbors

def compute_prob_distr(distances):
    inverse_distances = [1/d for d in distances]
    sum_d = sum(inverse_distances)
    prob_distr = [d/sum_d for d in inverse_distances]
    return prob_distr

def choose_index_with_weight(distances, indices):
    probability_distribution = compute_prob_distr(distances)
    index = choice(indices, 1, p=probability_distribution)[0]
    return index

def choose_index_without_weight(indices):
    index = random.choice(indices)
    return index

def get_predictions(train_data_1d, number_of_neighbors, num_points_to_predict, r, weighted=True):
    """ 
        train_data_1d:  list<float>, training data, assume that train_data[len(train_data) - r:] is the data upon which the next item will be predicted in
        number_of_neighbors: int, the value of k-neirest algorithm
        num_points_to_predict: int, number of points that you want to predict
        r: int, time-delay vector factor
        weighted: bool, if True the probability that certain K-nearest neighbor is going to be chosen will be inversely propotional to the distance from current point
    """
    #Step 1: create r-dimensional train data 
    train_data  = [train_data_1d[i:i+r] for i in range(0, len(train_data_1d)-r, r)]

    #Step 2: train NearestNeighbors using Ball Tree Algorithm and initialize predited prices to the last training_data point that is not used to train NearestNeighbors
    nbrs = NearestNeighbors(n_neighbors=number_of_neighbors, algorithm='ball_tree').fit(train_data[:-1])

    points = [train_data[-1]]
    points = np.array(points)
    new_p = train_data[-1]
    #Step 3: cmpute num_points_to_predict predictions
    while len(points.flatten()) < num_points_to_predict:
        #Step 3.1: get k neighbors
        distances, indices = nbrs.kneighbors([new_p])
        #Step 3.2: choose single neighbor based on whether it  is weighted or not
        if weighted:
            index = choose_index_with_weight(distances[0], indices[0])
        else:
            index = choose_index_without_weight(indices[0])
        #Step 3.3: compute gradient
        gradient = [train_data[index + 1][i] - train_data[index][i] for i in range(r)]
        #Step 3.4 append new point
        new_p = [train_data[-1][i] + gradient[i] for i in range(r)]  #go through each index
        points = np.append(points, [new_p], axis=0)

    return points.flatten()[:num_points_to_predict]