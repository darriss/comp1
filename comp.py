import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')

# Reduce decimal points to 2
#pd.options.display.float_format = '{:,.2f}'.format

compare = pd.read_csv("mardata.csv")
#print(compare.head())  # Show first 5 rows)
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

#Line graphs
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
plt.legend()
plt.show()
