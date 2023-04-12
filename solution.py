import pandas as pd
import numpy as np


chat_id = 1897874711 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    pvalue = kstest(x, y)
    return pvalue < alpha
