import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy import stats
from IPython.display import display, HTML
plt.style.use('bmh')
from pandas.plotting import scatter_matrix
compare = pd.read_csv("newmardata.csv")
meeting = pd.read_csv("meetingstats.csv")

#This part is defining all the variables for each indicator in education data
x = compare['Years']
y1 = compare['School enrollment, tertiary, male (% gross)']
x1 = compare['School enrollment, tertiary, female (% gross)']
y2 = compare['Lower secondary completion rate, male (% of relevant age group)']
x2 = compare['Lower secondary completion rate, female (% of relevant age group)']
md = compare['Number of maternal deaths']
sepsis = compare['Death by sepsis and other infections for children under 5 %']
anomaly = compare['Death by congenital anomalies under 5 years old %']
laborx = compare['Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)']
labory = compare['Labor force participation rate for ages 15-24, male (%) (national estimate)']
tvy = compare['% married M [15-19]']
tvx = compare['% married F [15-19]']
tvy1 = compare['% married M [20-24]']
tvx1 = compare['% married F [20-24]']
tvy2 = compare['% married M [25-29]']
tvx2 = compare['% married F [25-29]']
space =' ';

#Bar Graph section

labels = ['Family Meeting', 'Relationship with Neighbors', 'Blind Engagement', 'Public Place', 'School', 'Workplace']
casa_means = [13.9, 17.2, 5.9, 22.6, 6.6, 16]
tan_means = [23.2, 5.8, 1.2, 22.2, 8.3, 7.5]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, casa_means, width, label='Casablanca')
rects2 = ax.bar(x + width/2, tan_means, width, label='Tangier')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Meeting Place')
ax.set_ylabel('Percentage (%)')
ax.set_title('Circumstance of Meeting in 2011')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.show()

#Line graph section
#This labels the axix's and the graph
plt.title('Congenital Anomaly Death Rate of Children Ages (0-4) in Morocco')
plt.xlabel('Years', fontsize=10)
plt.ylabel('Percentage %', fontsize=10)
#These are each of the plots llalong the x axis
plt.plot(x, x1, marker='o', label='female college enrollment rate')
plt.plot(x, y1, marker='o', label='male college enrollment rate')
plt.plot(x, tvy1, marker='o', label='male marriage rate 20-24')
plt.plot(x, tvx1, marker='o', label='female marriage rate 20-24')
plt.plot(x, tvy2, marker='o', label='male marriage rate')
plt.plot(x, tvx2, marker='o', label='female marriage rate')
plt.plot(x, laborx, marker='o', label='female labor participation rate (ages 15+)')
plt.plot(x, labory, marker='o', label='male labor participation rate (ages 15-24)')
plt.plot(x, anomaly, marker='o')
plt.plot(x, y2, marker='o', label='male middle completion school')
plt.plot(x, x2, marker='o', label='female middle completion school')
plt.plot(x, tvy, marker='o', label='male marriage rate (15-19)')
plt.plot(x, tvx, marker='o', label='female marriage rate (15-19)')
plt.legend(loc='best')
plt.show()

#These are the mean, standard deviation, covariance,and correlation calculations
print('Mean and Standard Deviation of Variables')
print(space);
print('male college enrollment rate mean:', np.mean(y1))
print('male college enrollment rate standard deviation:', np.std(y1))
print('male marriage rate mean (20-24):', np.mean(tvy1))
print('male marriage rate standard deviation (20-24):', np.std(tvy1))
print('male marriage rate mean (25-29):', np.mean(tvy2))
print('male marriage rate standard deviation (25-29):', np.std(tvy2))
print(space);
print('female college enrollment rate mean:', np.mean(x1))
print('female college enrollment rate standard deviation:', np.std(x1))
print('female marriage rate mean (20-24):', np.mean(tvx1))
print('female marriage rate standard deviation (20-24):', np.std(tvx1))
print('female marriage rate mean (25-29):', np.mean(tvx2))
print('female marriage rate standard deviation (25-29):', np.std(tvx2))
print('female labor participation rate mean (15+):', np.mean(laborx))
print('female labor participation rate standard deviation (15+):', np.std(laborx))
print(space);
print('sepsis death rate mean (0-4):', np.mean(sepsis))
print('sepsis death rate standard deviation (0-4):', np.std(sepsis))
print('congenital anomaly death rate mean (0-4):', np.mean(anomaly))
print('congenital anomaly death rate standard deviation (0-4):', np.std(anomaly))
print('maternal death rate mean:', np.mean(md))
print('maternal death rate standard deviation:', np.std(md))
print(space);
print('Covariance and Correlation of Labor and Education')
print(space)
print('female college enrollment and labor participation rate covariance', np.cov(x1, laborx))
print('Pearsons correlation of female college enrollment and labor participation rate', scipy.stats.pearsonr(x1, laborx))
