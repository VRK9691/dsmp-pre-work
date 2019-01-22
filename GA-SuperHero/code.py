# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-', 'Agender')
gender_count = data['Gender'].value_counts()
plt.bar(gender_count, align = 'center', height = 25)



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment, labels = ["Good", "Bad", "Neutral"])



# --------------
import math
data['Gender'].replace('-', 'Agender')
gender_count = data['Gender'].value_counts()
# plot.bar(gender_count, align = 'center', height = '100')
sc_df = data[['Strength', 'Combat']].copy()
sc_df_2 = sc_df.copy()
sc_n = len(sc_df_2)
sc_covariance = round(sc_df.Strength.cov(sc_df.Combat),2)
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sd_sc_strength = sc_df.Strength.std()
sd_sc_combat = sc_df.Combat.std()
sc_df_2['sc_strength_2'] = sc_df['Strength'] ** 2
sc_df_2['sc_combat_2'] = sc_df['Combat'] ** 2
sc_sum_strength_2 = sum(sc_df_2['sc_strength_2'])
sc_sum_combat_2 = sum(sc_df_2['sc_combat_2'])
sc_sum_strength = sum(sc_df['Strength'])
sc_sum_combat = sum(sc_df['Combat'])
sc_df_2['sc_xy'] = sc_df['Strength'] * sc_df['Combat']
sc_sum_xy = sum(sc_df_2['sc_xy'])
# print(sc_df)

sc_pearson = ((sc_n * sc_sum_xy) - (sc_sum_strength * sc_sum_combat)) / (math.sqrt((sc_n * sc_sum_strength_2) - (sc_sum_strength ** 2)) * math.sqrt((sc_n * sc_sum_combat_2) -  (sc_sum_combat ** 2)))
print(sc_pearson)
ic_df = data[['Intelligence', 'Combat']].copy()
ic_df_2 = ic_df.copy()
ic_n = len(ic_df)
ic_covariance = round(ic_df.Intelligence.cov(ic_df.Combat),2)
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
sd_ic_intelligence = ic_df.Intelligence.std()
sd_ic_combat = ic_df.Combat.std()
ic_df_2['ic_intelligence_2'] = ic_df['Intelligence'] ** 2
ic_df_2['ic_combat_2'] = ic_df['Combat'] ** 2
ic_sum_intelligence_2 = sum(ic_df_2['ic_intelligence_2'])
ic_sum_combat_2 = sum(ic_df_2['ic_combat_2'])
ic_sum_intelligence = sum(ic_df['Intelligence'])
ic_sum_combat = sum(ic_df['Combat'])
ic_df_2['ic_xy'] = ic_df['Intelligence'] * ic_df['Combat']
ic_sum_xy = sum(ic_df_2['ic_xy'])
# print(sc_df)

ic_pearson = ((ic_n * ic_sum_xy) - (ic_sum_intelligence * ic_sum_combat)) / (math.sqrt((ic_n * ic_sum_intelligence_2) - (ic_sum_intelligence ** 2)) * math.sqrt((ic_n * ic_sum_combat_2) -  (ic_sum_combat ** 2)))
print(ic_pearson)
print(ic_covariance)
print(sc_covariance)



# --------------
#Code starts here
total_high = data.Total.quantile(q = 0.99)
super_best = data.loc[data['Total'] > total_high]
super_best_names = [i for i in super_best['Name']]
print(super_best_names)


# --------------
fig, ax_1 = plt.subplots(2, 2, sharex=True, sharey=True)
ax_1[0, 0].plot(data.Intelligence)
fig, ax_2 = plt.subplots(2, 2, sharex=True, sharey=True)
ax_2[0, 0].plot(data.Speed)
fig, ax_3 = plt.subplots(2, 2, sharex=True, sharey=True)
ax_3[0, 0].plot(data.Power)

plt.show()


