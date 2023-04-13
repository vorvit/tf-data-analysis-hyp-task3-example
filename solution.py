import pandas as pd
import numpy as np
import scipy.stats as stat

chat_id = 1056349463 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
#     p_value = stat.permutation_test((x, y), lambda x, y, \
#                  axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
#                  vectorized=True, 
#                  n_resamples=5000,
#                  alternative='greater').pvalue 
    return stat.ttest_ind(x, y)[1] < 0.07
