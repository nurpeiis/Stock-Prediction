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
        train_data:  list<float>, training data, assume that train_data[len(train_data) - r:] is the data upon which the next item will be predicted in
        number_of_neighbors: int, the value of k-neirest algorithm
        num_points_to_predict: int, number of points that you want to predict
        r: int, time-delay vector factor
    """
    #Step 1: create train data and train NearestNeighbors using Ball Tree Algorithm
    train_data  = [train_data_1d[i:i+r] for i in range(0, len(train_data_1d)-r, r)]
    nbrs = NearestNeighbors(n_neighbors=number_of_neighbors, algorithm='ball_tree').fit(train_data[:-1])
    
    #Step 2: Compute initial prediction, which is the last training data and is not used in nearest neighbor training step
    distances, indices = nbrs.kneighbors([train_data[-1]])
    if weighted:
        index = choose_index_with_weight(distances[0], indices[0])
    else:
        index = choose_index_without_weight(indices[0])
    gradient = [train_data[index + 1][i] - train_data[index][i] for i in range(r)]
    new_p = [train_data[-1][i] + gradient[i] for i in range(r)]  #go through each index
    points = []
    points.append(new_p)
    points = np.array(points)
    
    #Step 3: Compute num_points_to_predict predictions
    while len(points.flatten()) < num_points_to_predict:
        distances, indices = nbrs.kneighbors([new_p])
        if weighted:
            index = choose_index_with_weight(distances[0], indices[0])
        else:
            index = choose_index_without_weight(indices[0])
        gradient = [train_data[index + 1][i] - train_data[index][i] for i in range(r)]
        new_p = [train_data[-1][i] + gradient[i] for i in range(r)]  #go through each index
        points = np.append(points, [new_p], axis=0)

    return points.flatten()[:num_points_to_predict]