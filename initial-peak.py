import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from subprocess import check_output
import matplotlib.pyplot as plt
print(check_output(["ls", "../input"]).decode("utf8"))
from glob import glob
import seaborn as sns
from scipy import stats

df = pd.read_csv('../input/Train/train.csv')
print("{} training samples total".format(df.shape[0]))
df.head()