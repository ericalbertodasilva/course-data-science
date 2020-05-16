import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

data_set_testament = pd.read_csv('anova.csv', sep=';')

data_set_testament.boxplot(by='Remedio', grid=False)
model_ols_remedy = ols('Horas ~ Remedio', data = data_set_testament).fit()
result_ols_remedy = sm.stats.anova_lm(model_ols_remedy)

model_ols_remedy_gender = ols('Horas ~ Remedio * Sexo', data = data_set_testament).fit()
result_ols_remedy_gender = sm.stats.anova_lm(model_ols_remedy_gender)

mc = MultiComparison(data_set_testament['Horas'], data_set_testament['Remedio'])
result_test_tukey = mc.tukeyhsd()
print(result_test_tukey)
result_test_tukey.plot_simultaneous()

