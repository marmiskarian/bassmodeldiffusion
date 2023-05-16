# Bass Model Diffusions
This package, bassmodeldiffusion, is designed to provide a set of tools and functions for analyzing and modeling diffusion processes using the Bass Model. The Bass Model is a widely used framework for studying the adoption and spread of innovations or products in a population over time. By employing this package, users can gain insights into the diffusion patterns, make predictions, and visualize the diffusion process.

## Problem Definition
The diffusion of innovations or products refers to the process by which an item, idea, or technology spreads through a population over time. Understanding and predicting the diffusion patterns can be crucial for businesses, policymakers, and researchers. The Bass Model, proposed by Frank Bass, is a well-known mathematical model that provides a mathematical description of the diffusion process. The model takes into account the cumulative number of adopters, the coefficient of innovation, and the coefficient of imitation to forecast the future adoption curve.

## Detailed Description of the Package
The bassmodeldiffusion package consists of three subpackages, each serving a specific purpose:

### **Base**
The base subpackage provides fundamental functionality for working with the Bass Model. It includes the following modules:

- `__init__`: Initializes the package and imports the necessary dependencies.
- `__repr__`: Defines a detailed representation of the Bass Model object.
- `__str__`: Defines a string representation of the Bass Model object.
- `__bass_f__`: Implements the Bass Model function, which calculates the adoption rate at a given time.

### **Modeling**
The modeling subpackage focuses on the modeling aspect of the Bass Model. It offers the following modules:

- `fit`: Fits the Bass Model to the given adoption data, estimating the parameters that best describe the diffusion process.
- `predict`: Predicts the future adoption curve based on the fitted Bass Model parameters.

### **Visualize**
The visualize subpackage provides various visualization tools to help understand and analyze diffusion patterns. It includes the following modules:

- `plot_pdf`: Plots the Actual Sales vs Sales Forecast over Periods
- `plot_cdf`: Plots the Cumulative Sales Over Periods.
- `summary`: Generates a summary of the fitted Bass Model parameters and key metrics.
- `plot_peak_periods`: Prints the actual and predicted periods when the sales will reach to the peak.

## Installation
To install the bassmodeldiffusion package, you can use pip:

```
pip install bassmodeldiffusion
```

## Usage
Once the package is installed, you can import the necessary subpackages and modules and use the functions and modules to analyze diffusion data, fit the Bass Model, make predictions, and visualize the diffusion process.

For detailed information on how to use each function and module, please refer to the package documentation or the source code.

The `inference.ipynb` Notebook contains an example usage of the package on an example data.

## Contribution
Contributions to the bassmodeldiffusion package are welcome! If you encounter any issues, have suggestions, or would like to contribute to the project, please feel free to submit a pull request or open an issue on the GitHub repository.

## License
This package is distributed under the MIT License. See the LICENSE file for more information.