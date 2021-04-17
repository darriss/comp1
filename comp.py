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
compare = pd.read_csv("mardata.csv")
meeting = pd.read_csv("meetingstats.csv")
print(meeting.head())  # Show first 5 rows)
#print(compare.columns)

#This part is defining all the variables for each indicator in education data
x = compare['Years']
y1 = compare['Lower secondary completion rate, male (% of relevant age group)']
y2 = compare['Lower secondary completion rate, female (% of relevant age group)']
tvx = compare['% married M [15-19]']
tvy = compare['% married F [15-19]']
#This part is defining all the variables for each indicator in meeting in marriage data
xm = meeting['Circumstance of Meeting']
casa = meeting['Casablanca']
tan = meeting['Tangier']
'''
#Bar graph
plt.title('Circumstance of Meeting')
plt.xlabel('How they Met', fontsize=4)
plt.ylabel('Percentage', fontsize=16)
plt.bar(xm, casa)
plt.bar(xm, tan)
'''
labels = ['Family Meeting', 'Blind Engagement', 'Place of Study', 'Workplace']
casa_means = [13.9, 5.9, 6.6, 16]
tan_means = [23.2, 1.2, 8.3, 7.5]
'''
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, casa_means, width, label='Casablanca')
rects2 = ax.bar(x + width/2, tan_means, width, label='Tangier')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage (%)')
ax.set_title('Circumstance of Meeting in 2011')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()
'''
#Line graph
#This labels the axix's and the graph
plt.title('Compare')
plt.xlabel('2010', fontsize=10)
plt.ylabel('Indicators', fontsize=10)
#These are each of the plots llalong the x axis
plt.plot(x, y1, marker='o', label='male completion')
plt.plot(x, y2, marker='o', label='female completion')
plt.plot(x, tvx, marker='o', label='male marriage rate')
plt.plot(x, tvy, marker='o', label='female marriage rate')
#This shows what each line represents
#pd.tools.plotting.scatter_matrix(data.loc[:, y2:tvy], diagonal="kde")


pd.plotting.scatter_matrix(compare.loc[:, "School enrollment, tertiary, female (% gross)":"% married F [15-19]"], diagonal="kde")
plt.tight_layout()
plt.show()

print('y1 mean:', np.mean(y1))
print('y1 standard deviation:', np.std(y1))

print('covariance y1 and tvx', np.cov(y1, tvx))

# use pearson correlation if there is a linear relationship between variables
# use spearman correlation if the relationship is non-linear
print('correlation y1 and tvx', scipy.stats.spearmanr(y1, tvx))
