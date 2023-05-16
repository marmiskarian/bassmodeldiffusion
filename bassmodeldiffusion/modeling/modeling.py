"""Modeling module"""


import statsmodels.formula.api as smf
from bassmodeldiffusion.base.base import *


class Modeling(Base):
    """
    Class for fitting and predicting the Bass Model.
    """

    
    def fit(self):
        """
        Fitting the data to the Bass Model OLS regression.
        Returns
        -------
        dict
            Coefficient estimation from the OLS regression.
        """
        df = pd.DataFrame(list(zip(self.sales, self.cumsales, self.cum_sales_squared)), columns=['sales', 'cumsales', 'cum_sales_squared'])
        self.model = smf.ols(formula='sales ~ cumsales + cum_sales_squared', data=df)
        self.result = self.model.fit()
        self.params = self.result.params
        return self.params

    
    def predict(self):
        """
        Getting the maximum number of adopters, coefficient of innovation, and coefficient of imitation.
        Returns
        -------
        tuple
            The maximum number of adopters, coefficient of innovation, and coefficient of imitation.
        """
        m1 = (-self.params['cumsales'] + np.sqrt(self.params['cumsales'] ** 2 - 4 * self.params['Intercept'] * self.params['cum_sales_squared'])) / (2 * self.params['cum_sales_squared'])
        m2 = (-self.params['cumsales'] - np.sqrt(self.params['cumsales'] ** 2 - 4 * self.params['Intercept'] * self.params['cum_sales_squared'])) / (2 * self.params['cum_sales_squared'])
        self.m = max(m1, m2)
        self.p = self.params['Intercept'] / self.m
        self.q = -self.m * self.params['cum_sales_squared']
        return self.m, self.p, self.q