# creates a linear regression model (a line of best fit in the form y = mx + b)
# from a dataset

import numpy as np

# every x value should have a corresponding y value
def best_fit(xdata, ydata):
	# turn lists into nparrays if they are not already
	if len(xdata) != len(ydata):
		print(len(xdata), " x data points and", len(ydata), 
		      "y data points; please ensure your xdata and ydata 
		      correspond.\n Your results will be skewed.")
	m = (np.mean(xdata) * np.mean(ydata) - np.mean(xdata * ydata)) 
	    / (np.mean(xdata)**2 - np.mean(xdata**2))
	b = np.mean(ydata) - m * np.mean(xdata)
	return m, b
