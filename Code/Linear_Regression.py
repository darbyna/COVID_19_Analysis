#  Machine Learning Analysis of COVID-19 Data
#### Import necessary packages for the machine learning analysis: 


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_curve
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.metrics import plot_roc_curve

## Linear Regression: COVID-19 Global Data 
### The dependent variable that will be observed in the scenario of global data is the total deaths in comparison to the independent variables of the total confirmed COVID-19 patients. By using linear regression, the linear relationship between the reported COVID-19 deaths and the number of confirmed cases can be determined. If there is a positive linear relationship, that indicates that the confirmations do promote higher death rates. If there is a negative linear relationship, then the opposite shall hold. 

#### Import COVID-19 data that is compatible with a linear model: 

sample2 = pd.read_csv(r"covid_19_data.csv")
sample2 = pd.DataFrame(sample2)

#### Clean and organize the data: 
data2 = sample2.drop(columns = ['SNo', 'ObservationDate', 'Province/State', 'Country/Region', 'Last Update'])
data2

#### Import the Linear Regression module and instantiate the X and y for the model: 
from sklearn.linear_model import LinearRegression
y = np.array(data2['Deaths'])
X = np.array(data2[['Confirmed']])

np.shape(y)
np.shape(X)

#### Distribution of COVID-19 deaths as confirmations increase: 

sb.boxenplot(x = 'Confirmed', y = 'Deaths', data = data2)
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state= 42)

#### Instantiate the linear regression function and train the data: 

linreg = LinearRegression()
model = linreg.fit(X_train, y_train)


#### Test the data and observe the statistical information: 
y_pred = model.predict(X_test)
print('Accuracy of Linear classifier on test set: {:.2f}'.format(linreg.score(X_test, y_test)))

#### The Coefficient represents:

print('Coefficient: \n', model.coef_)
print('The coefficient of 0.08 shows a rather weak relation between the X and y variables. A score of 0.8 would have been stronger.')

#### The Mean Squared Error (MSE) is rather large thus showing a greater error: 
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))


#### The results yielding an  r^2 of 0.80 represents a large positive linear association between the dependent and independent variable:  
print('r_2 statistic: %.2f' % r2_score(y_test, y_pred))


#### Construct a dataframe to inspect the Actual versus Predicted results:
df = pd.DataFrame({'Actual:': y_test, 'Predicted:': y_pred})
df

##### From examining the dataframe, the actual versus predicted results are rather off from one another. The predicted results are not close in resemblance to the actual results. Let us continue this examination by looking at a few visualizations. 

#### Visualize the data for the train and test sets: 

# Actual vs Predicted Data Fit Visualization 
m, b = np.polyfit(y_test, y_pred, 1)
plt.plot(y_test, y_pred, 'o', color = 'RED')
plt.plot(y_test, m*y_test + b);

# This indicates a positive linea relationship
 # Training Data Visualization

plt.plot(X_train, y_train, 'o');


# Test Data Visualization
plt.plot(X_test, y_test, 'o');


