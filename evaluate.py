from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from math import sqrt

def calculate_error(real, predicted):
    
    forecast_errors = [real[i]-predicted[i] for i in range(len(real))]
    mfe = sum(forecast_errors) * 1.0/len(real) #mean_forecast_error
    
    mae = mean_absolute_error(real, predicted) 
    
    mse = mean_squared_error(real, predicted) 
    
    rmse = sqrt(mse) #root_mean_square
    
    return {'MFE': mfe, 'MAE': mae,  'MSE': mse, 'RMSE': rmse}

def explained_variance(real, predicted):
    exp_var = explained_variance_score(real, predicted)
    return exp_var

def compute_profit(real, predicted):
    profit = 0.0
    for i in range(1, len(predicted)):
        if predicted[i] > predicted[i-1]:
            profit += real[i] - real[i-1]
    
    return profit