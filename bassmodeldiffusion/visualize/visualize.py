"""Visualizing module"""


from bassmodeldiffusion.modeling.modeling import *


class Visualize(Modeling):
    """
    Class for visualizing the Bass Model predictions.
    """

    
    def plot_pdf(self):
        """
        PDF visualization of the predicted sales and actual sales.
        """
        self.sales_forecast = self.m * self.__bass_f__(self.p, self.q, self.time)
        plt.plot(self.periods, self.sales, 'o', color='black', label='Actual Sales')
        plt.plot(self.periods, self.sales_forecast, color='red', label='Sales Forecast')
        plt.title("Actual Sales vs Sales Forecast over Periods")
        plt.xlabel('Periods')
        plt.ylabel('Sales')
        plt.legend(loc='upper left')
        plt.show()

        
    def plot_cdf(self):
        """
        CDF visualization of the predicted sales.
        """
        self.cumsales_forecast = np.cumsum(self.sales_forecast)
        plt.plot(self.periods, self.cumsales_forecast, color='black')
        plt.title('Cumulative Sales Over Periods')
        plt.xlabel('Periods')
        plt.ylabel('Cumulative Sales')
        plt.show()

        
    def summary(self):
        """
        A summary of the coefficient of imitation, innovation, and the maximum number of adopters.
        """
        print(self.result.summary())
        print('=' * 78)
        print('\n{:<40}{:<10.5f}'.format('Coefficient of Innovation (p): ', self.p))
        print('{:<40}{:<10.5f}'.format('Coefficient of Imitation (q): ', self.q))
        print('{:<40}{:<10.3f}'.format('Max Adopters (m): ', self.m))
        print('=' * 78)
    
    
    def print_peak_periods(self):
        """
        Printing the actual and predicted periods when the sales will reach to the peak.
        """
        self.predicted_peak_periods = np.log(self.q / self.p) / (self.p + self.q)
        print('=' * 78)
        print('{:<40}{:<10.3f}'.format('Predicted peak sales period: ', self.predicted_peak_periods))
        print('{:<32}{:10.0f}'.format('Actual peak sales period: ', self.peak_periods))
        print('=' * 78)
