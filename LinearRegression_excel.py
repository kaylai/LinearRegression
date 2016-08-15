import pandas
import statsmodels.api as sm
import statsmodels.formula.api as smf
from patsy import dmatrices

data = pandas.read_excel('test.xlsx') #import excel file 'test.xlsx'
data = data.dropna(axis=1, how='all') #drop all columns that contain no data
data = data.loc[:, (data != 0).any(axis=0)] #drop all columns that contain all zeroes

formula = '{} ~ {} -1'.format(data.columns[0], ' + '.join(data.columns[1:])) #defines the formula needed to put into the dmatrices call without knowing how many X variables there will be but assuming the y variable is always the first column

y, X = dmatrices(formula, data=data, return_type='dataframe') #needed to align matrices

model = sm.OLS(y, X)
res = model.fit()

print res.summary()