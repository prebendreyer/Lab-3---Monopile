import catmanreader as cr
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


inputfiles = ['decay_1.bin', 'iw1_1.bin', 'rw3_1.bin', 'rw3_2.bin']

# Creating a dictionary of dataframes for each run
df = {}


# Looping through and decoding each binary file, creating dataframes and storing them in dictionary, d.
for i in inputfiles:
    binary = cr.import_catman_binary(i)
    data, keys = binary.get_data()
    data = pd.DataFrame(data)
    data.columns = keys
    data.columns.values[0] = 't'
    data.columns.map(str)
    df[i[:-4]] = data

decay = df['decay_1']

print(decay.columns)

print('Test commit')