

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from os import listdir
from os.path import isfile, join

from glob import glob

import librosa as lr
import librosa.display
import IPython.display as ipd

from itertools import cycle

# Setting some appearance 
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])


# setting music's base dir
data_dir = './SoundFiles'
audio_files = glob(f'{data_dir}/*.wav')
file_names = [f for f in listdir('SoundFiles') if isfile(join('SoundFiles', f))]

# loading the music (1st)
ipd.Audio(audio_files[0])
y, sr = librosa.load(audio_files[0])

# to uncomment if seeing plot data is needed
# print(f'y: {y[:10]}')
# print(f'shape y: {y.shape}')
# print(f'sr: {sr}')



pd.Series(y).plot(figsize=(10, 5),
                  lw=1,
                  title='Waveform',
                 color=color_pal[0])
plt.savefig("./Plots/"f'{file_names[0]}_WF.png')



