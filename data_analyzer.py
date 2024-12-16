#%%
from glob import glob
import numpy as np
from ml_dtypes import bfloat16
import matplotlib.pyplot as plt

datas = []
for i in glob("somewhere/td/*.npy"):
    datas.append(np.load(i))
data = np.concatenate(datas)
data.shape
#%%
# norm histogram
plt.hist(np.linalg.norm(data, axis=1), bins=100, label="norm")
# norm away from mean histogram
plt.hist(np.linalg.norm(data - np.mean(data, axis=0), axis=1), bins=100, label="norm away from mean")
plt.legend()
plt.show()
#%%
# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(data)
data_pca = pca.transform(data)
plt.scatter(data_pca[:, 0], data_pca[:, 1])
#%%
# Variance explained by PCA
pca = PCA()
pca.fit(data)
#%%
plt.plot(pca.explained_variance_ratio_)
plt.xscale("log")
plt.yscale("log")
# data is very low-rank!
# %%
# for comparison, let's look at data from an LM
llama_data = np.load("somewhere/llama.npz")["arr_0"]
pca = PCA()
pca.fit(llama_data)
#%%
plt.plot(pca.explained_variance_ratio_[1:])
plt.xscale("log")
# plt.yscale("log")
# %%
