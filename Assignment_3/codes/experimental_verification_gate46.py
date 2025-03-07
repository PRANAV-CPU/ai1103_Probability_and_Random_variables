# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/143nlROwqAKlDaVDbudI8Nxy1MqXfojS_
"""

from scipy.stats import norm
import numpy as np

sample_size=10000
k=2

#generation of gaussian random variables-U
norm_data_U=norm.rvs(size=sample_size)

#generation of uniform random variables-V
uniform_data_V=np.random.uniform(0,2,size=sample_size)

#generation of uniform random variables-X
rand_data_X=np.add(norm_data_U,2*uniform_data_V)

#calculating the average of X ,U ,V
average_U=sum(norm_data_U)/sample_size
average_V=sum(uniform_data_V)/sample_size
average_X_k=sum(rand_data_X)/sample_size

#comparing theoritical and classical means
print("The Experimental and theoritical mean of U are {} --- {}".format(average_U,0))
print("The Experimental and theoritical mean of V are {} --- {}".format(average_V,1))
print("The Experimental and theoritical mean of X are {} --- {}".format(average_X_k,1*k+0))

#plotting theoritical vs classical means
import matplotlib
import matplotlib.pyplot as plt

labels = ['U','V','X({})'.format(k)]
Experimental= [round(average_U,3),round(average_V,3),round(average_X_k,3)]
Theoritical= [0,1,k]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,Experimental, width, label='Experimental')
rects2 = ax.bar(x + width/2,Theoritical, width, label='Theoritical')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Expectation Values')
ax.set_title('Comparision of Experimental and Theoritical Means')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()