import numpy as np

def wipe_off(dataArray1, dataArray2):
    dataArray1Temp = np.array(dataArray1)
    dataArray2Temp = np.array(dataArray2)

    return np.array(dataArray1Temp) * np.array(dataArray2Temp)