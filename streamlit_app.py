import streamlit as st
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig

selection = "<not selected>"
selection = st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))
'You choose ', selection, '.'

x = 10
'x: ', x 
