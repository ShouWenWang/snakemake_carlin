import pandas as pd
from scipy.io import loadmat
import seaborn as sns
import numpy as np
sns.set_style("whitegrid")


import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_dir",
    type=str,
    default=".",
)
input_dir = parser.parse_args().input_dir

data=loadmat(f'{input_dir}/indel_freq_vs_length.mat')

x1=[0]+list(np.cumsum(data['del_freq'][0][0].flatten()))
y1=[0]+list(np.cumsum(data['ins_freq'][0][0].flatten()))
df=pd.DataFrame({'Deletion':x1,'Insertion':y1,'Size': np.arange(len(x1))})
df1=df.melt(id_vars='Size',value_name='Cumulative distribution', var_name='Mutation type')
g=sns.relplot(data=df1,x='Size',y='Cumulative distribution',hue='Mutation type',kind='line')
g.figure.savefig(f'{input_dir}/cumulative_indel_freq.pdf')