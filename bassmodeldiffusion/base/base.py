"""Base module"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Base:
    """
    Base class for the Bass model.

    Parameters:
        filename (str): The name of the file containing the data.

    Attributes:
        data (ndarray): Numpy array containing the loaded data.
        periods (ndarray): Numpy array containing periods data.
        sales (ndarray): Numpy array containing sales data.
        time (range): Range representing the time period.
        filename (str): File name (without extension).
        peak_periods (ndarray of ints): Actual peak periods.
        predicted_peak_periods (None or float): Predicted peak periods.
        cumsales (None or ndarray): Numpy array containing cumulative sales data.
        cum_sales_squared (None or ndarray): Numpy array containing squared cumulative sales data.
        sales_forecast (None or ndarray): Numpy array containing sales forecast data.
        cumsales_forecast (None or ndarray): Numpy array containing cumulative sales forecast data.
        model (None or object): Object representing the fitted model.
        result (None or object): Object representing the model results.
        params (None or ndarray): Numpy array containing model parameters.
        m (None or int): Value representing the coefficient m in the Bass model.
        p (None or float): Value representing the coefficient p in the Bass model.
        q (None or float): Value representing the coefficient q in the Bass model.
    """

    
    def __init__(self, filename=None):
        """
        Initialize the BassModel instance.

        Parameters:
            filename (str): The name of the file containing the data.
        """
        # Error Checking
        if filename is None:
            raise ValueError('Missing filename.')
        
        file_extension = filename.split(".")[-1]
        if file_extension not in ['csv', 'txt']:
            raise ValueError(f'Unsupported file format "{file_extension}". Expected csv or txt.')
        
        try:
            self.data = pd.read_csv(filename, delimiter=',' if file_extension == 'csv' else '\t')
            self.periods = self.data.iloc[:, 0].to_numpy()
            self.sales = self.data.iloc[:, 1].to_numpy()
            self.time = range(1, len(self.sales) + 1)
            self.filename = filename[:-4]
        except FileNotFoundError:
            raise FileNotFoundError('File not found.')

        self.peak_periods = np.argmax(self.sales)
        self.predicted_peak_periods = None
        self.cumsales = np.cumsum(self.sales)
        self.cum_sales_squared = self.cumsales ** 2
        self.sales_forecast = None
        self.cumsales_forecast = None
        self.model = None
        self.result = None
        self.params = None
        self.m = None
        self.p = None
        self.q = None  

        
    def __repr__(self):
        """
        Return a string representation of the BassModel instance.
        """
        return f"BassModel(filename='{self.filename}')"

    
    def __str__(self):
        """
        Return a string representation of the BassModel instance.
        """
        return f"BassModel instance for '{self.filename}'"

    
    def __bass_f__(self, p, q, t):
        """
        Calculate the Bass model function value for given parameters.

        Parameters:
            p (float): Innovation rate or coefficient of innovation.
            q (float): Imitation rate or coefficient of imitation.
            t (float): Time value, usually a year.

        Returns:
            float: The Bass model function value.
        """
        return (((p + q) ** 2)/p) * np.exp(-(p + q) * t) / ((1 + (q / p) * np.exp(-(p + q) * t))**2)