# linear algebra
import numpy as np
# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd
from subprocess import check_output
import matplotlib.pyplot as plt
print(check_output(["ls", "./input"]).decode("utf8"))
from glob import glob
import seaborn as sns
from scipy import stats

# pd.set_option(max_columns=10)

df = pd.read_csv('./input/Train/train.csv')
print("{} training samples total".format(df.shape[0]))
df.head()

# Prepare a graph of the data.
df[['adult_males', 'subadult_males', 'adult_females', 'juveniles', 'pups']]\
    .sum(axis=0)\
    .plot\
    .barh()

# Actually show the graph.
plt.show()