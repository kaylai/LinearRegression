import stats_csv_reader
import numpy as np
import statsmodels.api as sm

y, x_vals, Glass, cpx, fspar, qtz, amph, olivine, mag, ilm, chev, ap, fl, po = stats_csv_reader.opencsv("/Users/kiacovino/Desktop/test.csv")

def reg_m(y, x_vals):
    ones = np.ones(len(x_vals[0]))
    X = sm.add_constant(np.column_stack((x_vals[0], ones)))
    for ele in x_vals[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results
    
print reg_m(y, x_vals).summary()