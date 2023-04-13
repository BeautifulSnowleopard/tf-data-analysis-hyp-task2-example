import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1897874711 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    D, p = ks_2samp(x, y)
    if p < 0.04:
        return True
    else:
        return False
