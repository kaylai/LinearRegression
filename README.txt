LinearRegression_excel.py

WHAT IS LINEARREGRESSION_EXCEL.PY?
This is a script to run a least squares multiple linear regresion. It was developed for use in geologic samples in order to model the generation of a daughter rock from a parent magma + crystals via fractional crystallization. The test.xlsx file is laid out for this purpose.

THE TEST.XLSX FILE
SM = "Starting Material". Put the composition of the parent rock here.
All other columns = Compositions measured in the daughter rock (plus compositions of crystals found in the parent rock, if applicable)

OUTPUTS OF THE SCRIPT
The script performs an OLS Regression using pandas and statsmodels.api. See the statsmodels documentation for specific detailed explanations of the output. For the geologic example, the outputs of interest are the coefficients and standard errors. 

Coefficiens (coef) represent phase proportions of each phase that, when added together, make up the components of the parent rock. For example, a coef value of 0.85 for Glass indicates that the daughter liquid is a 85% residual liquid from a parent magma.

Standard Errors (std) tell you how good of a job the script did at finding the correct phase proportions (coefficients). You want this number to be small. A smaller std means a more robust model.

INSTALLATION AND USE
To run this script requires some dependencies:
	1. Python 2.7
	2. pandas - use > sudo easy_install pandas
	3. statsmodels.api - use > sudo easy_install -U statsmodels
	4. xlrd - use > sudo easy_install xlrd

KNOWN ISSUES
Do not use spaces in header row of test.xlsx file, or it will throw an error.