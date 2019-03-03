import numpy as np
W_1 = np.array([[ 2.01372112e-03,  5.72821905e-03,  7.76421593e-04,
         9.47574910e-03,  5.47614334e-03,  3.52957760e-03,
         8.50787509e-03,  6.88346961e-03,  7.08631871e-03,
         7.43206970e-03],
       [ 2.98704162e-03,  8.66663522e-03,  5.16046014e-03,
         4.58909140e-03,  4.55800755e-03,  5.82898318e-03,
         6.49281659e-03,  4.34480183e-03,  4.72359890e-03,
         4.93861700e-03],
       [ 1.17710177e-02,  1.49718588e-01,  2.22619263e-02,
         7.09952414e-02,  2.90681505e-02,  4.83370364e-03,
         1.21070014e-01,  2.78490001e-02,  2.06429502e-02,
         5.00200245e-02],
       [-3.53809901e-03,  2.19595421e-01, -9.38713694e-03,
        -3.14124006e-02, -1.25114949e-02, -8.70983505e-04,
         1.83662547e-01, -1.16501045e-02, -1.00036248e-02,
        -2.20977013e-02],
       [ 1.45734420e-02,  9.87107623e-02,  2.80051954e-02,
         9.02494043e-02,  3.71128717e-02,  5.45457050e-03,
         8.07464236e-02,  3.54429364e-02,  2.68396646e-02,
         6.39596608e-02],
       [ 1.15154581e-02,  1.04720805e-01,  2.25218154e-02,
         7.20821193e-02,  2.94673660e-02,  4.70321732e-03,
         9.17554500e-02,  2.82822549e-02,  2.16722886e-02,
         5.12762784e-02],
       [-1.29902632e-04,  1.72559610e-01, -2.48139515e-03,
        -9.55208851e-03, -3.43260469e-03,  8.81074690e-04,
         1.37875382e-01, -3.12150077e-03, -3.23922190e-03,
        -6.72096587e-03],
       [ 2.95914671e-03,  1.44666622e-01,  5.18841140e-03,
         1.51342519e-02,  6.16602613e-03,  6.05476058e-04,
         1.17637678e-01,  6.58501112e-03,  4.21374754e-03,
         1.09437919e-02],
       [ 2.35745400e-03,  1.79200081e-01,  3.42462024e-03,
         1.06057225e-02,  4.20330534e-03, -5.60596853e-05,
         1.42900272e-01,  4.88514479e-03,  2.20766329e-03,
         7.85383868e-03],
       [ 8.78139230e-03,  1.30710892e-01,  1.60062180e-02,
         5.12151330e-02,  2.02595902e-02,  3.62953387e-03,
         1.08879672e-01,  2.06657711e-02,  1.47916127e-02,
         3.56929833e-02],
       [ 6.86436633e-03,  1.17644230e-01,  1.31859333e-02,
         4.12932627e-02,  1.80704398e-02,  4.23044430e-03,
         1.00605807e-01,  1.68979975e-02,  1.31613401e-02,
         2.90608071e-02],
       [ 1.87225884e-02,  4.53798223e-02,  3.67731294e-02,
         1.18793084e-01,  4.86529466e-02,  8.92006212e-03,
         3.92065043e-02,  4.64900656e-02,  3.56860066e-02,
         8.34970719e-02],
       [ 1.57431952e-02,  9.22388329e-02,  2.90190579e-02,
         9.33632833e-02,  3.80712874e-02,  6.69925249e-03,
         8.14168033e-02,  3.67691187e-02,  2.66672397e-02,
         6.55402728e-02],
       [ 8.17237449e-03,  1.24183180e-01,  1.60375755e-02,
         4.99655932e-02,  2.02008463e-02,  4.15045539e-03,
         1.06841929e-01,  1.97170716e-02,  1.48414463e-02,
         3.56097923e-02],
       [ 1.17394862e-02,  1.23174723e-01,  2.15754914e-02,
         6.87228152e-02,  2.81812711e-02,  4.81160928e-03,
         9.83686598e-02,  2.73586489e-02,  2.02335825e-02,
         4.83246164e-02],
       [ 2.03224551e-01, -4.45326974e-01,  3.90084622e-01,
         1.27788616e+00,  5.01728810e-01,  7.74895609e-02,
        -3.71637437e-01,  4.95040433e-01,  3.56108076e-01,
         8.96701494e-01]])
b_1 = np.array([-0.04898782,  0.54281244, -0.0911682 , -0.29001589, -0.11883265,
       -0.02115118,  0.44916652, -0.11566775, -0.08456035, -0.20466726])
W_2 = np.array([[ 0.14556506, -0.13101177],
       [-0.5643325 ,  0.58007841],
       [ 0.26933785, -0.26198515],
       [ 0.87697011, -0.8614763 ],
       [ 0.34851539, -0.33590722],
       [ 0.05518857, -0.04852069],
       [-0.4678296 ,  0.48043857],
       [ 0.34145839, -0.33292402],
       [ 0.24938134, -0.23655529],
       [ 0.61514693, -0.6050945 ]])
b_2 = np.array([-0.98916345,  0.98916345])