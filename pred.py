import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


dfOld = pd.read_csv('Illinois_Population__1991-1999.csv', skiprows=1)
dfNew = pd.read_csv('Illinois_Population__2000-2009.csv', skiprows=1)

dfOld.plot()
