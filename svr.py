# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x= dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x = sc_X.fit_transform(x)

sc_y = StandardScaler()
y=np.array(y).reshape(-1,1)
y = sc_y.fit_transform(y)

# Fitting the Regression Model to the dataset
# Create your regressor here
from sklearn.svm import SVR
regg=SVR(kernel='rbf')
regg.fit(x,y)
# Predicting a new result
y_pred = sc_y.inverse_transform(regg.predict(sc_X.transform(np.array([[6.5]]))))

# Visualising the svr results
plt.scatter(x, y, color = 'red')
plt.plot(x,regg.predict(x), color = 'blue')
plt.title('Truth or Bluff (svr)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(x), max(x), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(X_grid, regg.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (svr)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()