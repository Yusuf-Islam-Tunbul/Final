import numpy as np
import pandas as pd

distances=np.array(pd.read_excel (r'C:\Users\ytunb\.spyder-py3\Yeni klasör\distancematrix.xls',skiprows=2,usecols=list(np.linspace(2,83,82))))
coordinates=np.array(pd.read_excel (r'C:\Users\ytunb\.spyder-py3\Yeni klasör\Coordinates.xlsx',usecols=[2,3]))