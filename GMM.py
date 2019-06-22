import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.mixture import GaussianMixture
from sklearn.mixture import BayesianGaussianMixture
from copy import deepcopy

aic = []
bic = []
n_com = 12

data,label = make_blobs(n_samples=400,n_features=2,centers=4)
gmm_without = GaussianMixture(n_components=4).fit_predict(data)
gmm_vbem = BayesianGaussianMixture(n_components=4).fit_predict(data)

plt.scatter(data[:,0],data[:,1],c=label)
plt.show()

low = 99999
for n in range(1,n_com+1):
    gmm = GaussianMixture(n_components=n)
    gmm.fit(data)
    aic.append(gmm.aic(data))
    if aic[-1] < low:
        low = aic[-1]
        model = deepcopy(gmm)

low2 = 99999
for n in range(1,n_com+1):
    gmm = GaussianMixture(n_components=n)
    gmm.fit(data)
    bic.append(gmm.bic(data))
    if bic[-1] < low2:
        low2 = bic[-1]
        model2 = deepcopy(gmm)       
        
gmm_aic = model.predict(data)
gmm_bic = model2.predict(data)
print max(gmm_aic) - min(gmm_aic) + 1
print max(gmm_bic) - min(gmm_bic) + 1
print max(gmm_vbem) - min(gmm_vbem) + 1
plt.scatter(data[:,0],data[:,1],c=gmm_aic)
plt.savefig('gmm_aic6.png')
plt.show()
plt.scatter(data[:,0],data[:,1],c=gmm_bic)
plt.savefig('gmm_bic6.png')
plt.show()
plt.scatter(data[:,0],data[:,1],c=gmm_vbem)
plt.savefig('gmm_vbem6.png')
plt.show()


