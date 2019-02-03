# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
list_a = df.loc[df['fico'] > 700]
p_a = len(list_a) / len(df)
list_b = df.loc[df['purpose'] == 'debt_consolidation']
p_b = len(list_b) / len(df)
df1 = df.loc[df['purpose'] == 'debt_consolidation']
list_a_b = df1.loc[df1['fico'] > 700]
p_a_b = len(list_a_b) / len(df1)
r = lambda a,b: True if a == b else False
result = r(p_a, p_a_b)
print(result)

# code ends here


# --------------
# code starts here
list_lp = df.loc[df['paid.back.loan'] == 'Yes']
prob_lp = len(list_lp) / len(df)

list_cs = df.loc[df['credit.policy'] == 'Yes']
prob_cs = len(list_cs) / len(df)

new_df = df.loc[df['paid.back.loan'] == 'Yes']
list_pd_cs = new_df.loc[new_df['credit.policy'] == 'Yes']
prob_pd_cs = len(list_pd_cs) / len(new_df)

bayes = (prob_pd_cs * prob_lp) / prob_cs
print(bayes)




# code ends here


# --------------
# code starts here
lbar = df.purpose.unique()
plt.bar(lbar, df.purpose.value_counts(), width=0.2)
df1 = df.loc[df['paid.back.loan'] == 'No']

plt.bar(lbar, df1.purpose.value_counts())


# code ends here


# --------------
# code starts here
inst_median = df.loc[:,"installment"].median()
inst_mean = df.loc[:,"installment"].mean()


plt.hist(df['installment'])
plt.show()
plt.hist(df['log.annual.inc'])
plt.show()

# code ends here


