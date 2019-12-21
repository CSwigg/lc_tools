import lcTools as lc
import numpy as np
import matplotlib.pyplot as plt

large = lc.photoTable('data_files/DR14_large.csv')
lg = large.group_things()
our_key = 77759292
q = lg['77759292']
q_median_i = np.median(q['modelMag_i'])
list_similar = []
q_n_detections = len(q['modelMag_i'])


for key, thing in lg.items():

    if (len(thing['modelMag_i']) == q_n_detections) and np.isclose(np.median(thing['modelMag_i']), q_median_i, 0.01):
        list_similar.append(thing)
        
our_quasar = list_similar.pop(3)

def plot_sim(list_sim):
    for l in list_sim:
        plt.figure()
        plt.scatter(l['mjd_i'], l['modelMag_i'])
        plt.errorbar(l['mjd_i'], l['modelMag_i'], l['modelMagErr_i'], ls = 'None')

        plt.show()

def get_comparison_medians(list_sim):
        
