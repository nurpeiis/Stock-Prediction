# Stock Prediction

The main goal of this repository is to test various models for stock market prediction. We employ Yahoo! Finance's live data using `yfinance` python library

## Table of contents:
 - [Requirements](#requirements)
 - [Get Started](#get-started)
 - [Modules Description](#modules-description)
 - [References](#references)
 - [Future Work](#future-work)
## Requirements

- `Python 3.8+`
- `Miniconda`

## Get Started

First create environment from `environment.yml` file running following command:

`conda env create -f environment.yml`


In order to activate the virtual environment, run following command:

`conda activate stock_prediction`

In order to test the general framework, run following command:

`jupyter notebook`

Then navigate to `visualization.ipynb` notebook and press play button for all the containers of the notebook.

In this notebook you can decide on changing following options:

- `stock_name` - name of the stock that you would like to predict the price and determine the profit generated 
- `num_points_to_predict` - number of next days that you would like to predict
- `number_of_neighbors` - this is number of neighbors that K-nearest neighbors module will return
- `weighted` - set to True if you want the neighbor to be chosen with weighted probability distribution, as in the closer the point the higher the probability that it will be chosen. Otherwise if set to False, the neighbor will be chosen randomly.


## Modules Description

- `get_data.py`:
    - Input: 
      - `stock_name` - string stock symbol, you can find list of stock's symbols listed on the New York Stock Exchange (NYSE) [here](https://www.nyse.com/listings_directory/stock)
      - `period` - from which day to which day you would like to  get the data, the default is `max`, which  is the whole history available at Yahoo Finance
      - `interval` - interval at which you want the data to be retrieved
    - Output:
      - `history` - `pandas.DataFrame` that contains over 40 columns per unit data. Unit data's index is timestamp

- `evaluate.py`: There are three metrics available to evaluate the performance of predicted closing price prediction
    1. `calculate_error` - given array of real and predicted closing price, it will return following error metrics: Mean Forecast Error (MFE), Mean Absolute Error (MAE), Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).
    2. `explained_variance` - given array of real and predicted closing price, it will return explained variance score
    3. `compute_profit` -  given array of real and predicted closing price, it will return maximum profit generated from predicted price using Peak Valley Approach

- `rap.py` - this is the module that implements Local Random Analogue Prediction (RAP)
 - `get_predictions` - main function that has  implementation of RAP for predicting stock prices with following parameters:
   - `train_data_1d:  list<float>`, training data, assume that train_data[len(train_data) - r:] is the data upon which the next item will be predicted in
   - `number_of_neighbors: int`, the value of k-neirest algorithm
   - `num_points_to_predict: int`, number of points that you want to predict
   - `r: int`, time-delay vector factor
   - `weighted: bool`, if True the probability that certain K-nearest neighbor is going to be chosen will be inversely propotional to the distance from current point
    

## References

```bash
@article{paparella1997rap,
title = "Local random analogue prediction of nonlinear processes",
journal = "Physics Letters A",
volume = "235",
number = "3",
pages = "233 - 240",
year = "1997",
issn = "0375-9601",
doi = "https://doi.org/10.1016/S0375-9601(97)00607-5",
url = "http://www.sciencedirect.com/science/article/pii/S0375960197006075",
author = "F. Paparella and A. Provenzale and L.A. Smith and C. Taricco and R. Vio",
keywords = "Time series analysis, Nonlinear prediction, Dynamical reconstruction, Variability of astrophysical and geophysical systems, Stochastic systems, Deterministic systems",
abstract = "Given that is not possible to predict the precise evolution of either stochastic processes or chaotic processes from observations, a data-based algorithm with minimal model-structure constraints is presented for generating stochastic series which are realistic, in that their long-term statistics reflect those of a process consistent with the observations. This approach employs random analogues, and complements that of deterministic nonlinear prediction which estimates an expected value. Contrasting these approaches clarifies the distinction between Lorenz's predictions of the first and second kind. Output from several nonlinear stochastic processes and observations of quasar 3C 345 are analysed; the synthetic time series have power spectra, amplitude distributions and intermittency properties similar to those of the observations."
}
```

## Future Work

- Employ technical indicators that are available from python library [ta](https://github.com/bukosabino/ta). For now the only dimension per unit data is closing price, however in the future it will be interesting to see on how increeasing the dimension will improve performance, as in the profit generate from the data.
- Test with various Machine Learning models, such as this [work](https://github.com/VivekPa/AIAlpha)
- Build baseline model that will be used to compare with other models
