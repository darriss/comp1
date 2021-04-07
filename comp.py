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
print(compare.head())  # Show first 5 rows)
#print(compare.columns)

#This part is defining all the variables for each indicator
x = compare['Years']
y1 = compare['Lower secondary completion rate, male (% of relevant age group)']
y2 = compare['Lower secondary completion rate, female (% of relevant age group)']
tvx = compare['% married M [15-19]']
tvy = compare['% married F [15-19]']
#Bar graph
#plt.xlabel('2010', fontsize=4)
#plt.ylabel('Indicators', fontsize=16)
#plt.bar(x, y1)

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
'''
plt.tight_layout()
plt.legend()
plt.show()
'''
pd.plotting.scatter_matrix(compare.loc[:, "School enrollment, tertiary, female (% gross)":"% married F [15-19]"], diagonal="kde")
plt.tight_layout()
plt.show()
