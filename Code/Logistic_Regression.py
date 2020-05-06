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


## Logistic Regression: COVID-19 Global Data 
### The dependent variable that will be observed in the scenario of global data is the total deaths in comparison to the independent variables of the total recovered and  COVID-19 patients that have or have not visited Wuhan, China. By using logistic regression, the relationship between the reported binary death rates of COVID-19 and the reported binary visitations to Wuhan, China can be scrutinized. 
### The data was procured from Kaggle via the following link: 

https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#covid_19_data.csv
    
#### Import binary COVID-19 data
sample = pd.read_csv(r"COVID19_line_list_data.csv")
sample = pd.DataFrame(sample)

#### Preview the head of the data set:
sample.head()

#### Show what countries are represented in the dataset:
sample['country'].unique()


#### The COVID-19 dataset being examined for Logistic Regression only analyzes data from early January 2020 to late February 2020:
sample['hosp_visit_date'].unique()
sample['exposure_end'].unique()

#### Clean and organize the data
data = sample.drop(columns = ['summary', 'location', 'id', 'case_in_country', 'reporting date', 'Unnamed: 3', 'country', 'gender', 'age', 'symptom_onset', 'If_onset_approximated', 'hosp_visit_date', 'exposure_start', 'exposure_end', 'link', 'source', 'from Wuhan', 'symptom'])
data = data.reset_index().drop(columns = ['index'])
data = data[data.death != '2/1/2020']
data = data[data.death != '2/13/2020']
data = data[data.death != '2/14/2020']
data = data[data.death != '2/19/2020']
data = data[data.death != '02/01/20']
data = data[data.death != '2/21/2020']
data = data[data.death != '2/22/2020']
data = data[data.death != '2/23/2020']
data = data[data.death != '2/24/2020']
data = data[data.death != '2/25/2020']
data = data[data.death != '2/26/2020']
data = data[data.death != '2/27/2020']
data = data[data.death != '2/28/2020']
data.death.unique()
data = data[data.recovered != '2/12/2020']
data = data[data.recovered != '1/15/2020']
data = data[data.recovered != '12/30/1899']
data = data[data.recovered != '2/8/2020']
data = data[data.recovered != '2/14/2020']
data = data[data.recovered != '2/4/2020']
data = data[data.recovered != '2/18/2020']
data = data[data.recovered != '2/5/2020']
data = data[data.recovered != '2/17/2020']
data = data[data.recovered != '2/9/2020']
data = data[data.recovered != '2/15/2020']
data = data[data.recovered != '2/27/2020']
data = data[data.recovered != '2/19/2020']
data = data[data.recovered != '2/20/2020']
data = data[data.recovered != '1/17/2020']
data = data[data.recovered != '2/7/2020']
data = data[data.recovered != '2/21/2020']
data = data[data.recovered != '2/23/2020']
data = data[data.recovered != '2/11/2020']
data = data[data.recovered != '2/22/2020']
data = data[data.recovered != '2/16/2020']
data = data[data.recovered != '2/24/2020']
data = data[data.recovered != '2/26/2020']
data = data[data.recovered != '2/25/2020']
data = data[data.recovered != '2/6/2020']
data = data[data.recovered != '2/28/2020']
data = data[data.recovered != '1/30/2020']
data = data[data.recovered != '2/13/2020']
data = data[data.recovered != '2/2/2020']
data = data[data.recovered != '1/31/2020']
data = data[data.recovered != '02/12/20']
data = data[data.recovered != '02/08/20']
data = data[data.recovered != '02/04/20']
data = data[data.recovered != '02/05/20']
data = data[data.recovered != '02/09/20']
data = data[data.recovered != '02/07/20']
data = data[data.recovered != '02/11/20']
data = data[data.recovered != '02/06/20']
data = data[data.recovered != '02/02/20']
data.recovered.unique()

#### After cleaning and organizing the data, instantiate the X and y for the machine learning predictive model.

y = np.array(data[['death']])
X = np.array(data[['recovered','visiting Wuhan']])
X.shape, y.shape

#### Visualize the variables:

sb.countplot(x='death', data= data, palette= 'hls')
plt.show()


#### Instantiate the test and train sets:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state= 42)


#### Instantiate the Logistic Regression and train the data.

lreg = LogisticRegression()
model = lreg.fit(X_train, y_train)

#### Run a test on the data and predict the score: 

y_pred = model.predict(X_test)
print('Accuracy of Logistic classifier on test set: {:.2f}'.format(lreg.score(X_test, y_test)))
fr


#### The confusion matrix below shows: 

#- A true positive of 260 
#- A false positive of 14 
#- A false negative of 0
#- A true negative of 0


print(confusion_matrix(y_test, y_pred))

#### Observe the classification report: 

print(classification_report(y_test, y_pred))

#### Visualize the data using a ROC curve:

svc = SVC(random_state=42)
svc.fit(X_train, y_train)

svc_disp = plot_roc_curve(svc, X_test, y_test)

#### SVC (AUC= 0.58) shows that the predictive model on COVID-19 deaths has no discriminatory ability.

print("https://www.sciencedirect.com/science/article/pii/S1556086415306043")







































































