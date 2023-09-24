

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from string import punctuation
from utils import *

df_sandra = pd.read_csv('data/sandraTorres.csv')
df_sandra = df_sandra.drop(df_sandra.columns[0], axis=1)	# Primera columna no es necesaria
df_sandra = df_sandra.apply(lambda x: x.astype(str).str.lower())	# convertir todo a minúscula
if 'id' in df_sandra.columns:
    df_sandra = df_sandra.drop(['id'], axis=1)
df_sandra = df_sandra.drop(['id_str'], axis=1)
df_sandra = df_sandra.drop(['url'], axis=1)

# Eliminar signos de puntuacion
df_sandra['rawContent'] = df_sandra['rawContent'].apply(lambda x: ''.join([i for i in x if i not in punctuation]))

# Eliminar @
df_sandra['rawContent'] = df_sandra['rawContent'].str.replace('@', '')
df_sandra['rawContent'] = df_sandra['rawContent'].str.replace('#', '')

# Eliminar emoji
df_sandra['rawContent'] = df_sandra['rawContent'].apply(lambda x: emoji_pattern.sub(r'', x))
df_sandra['rawContent'] = df_sandra['rawContent'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

df_sandra = df_sandra[df_sandra['lang'] == 'es']

import ast

single_entry = df_sandra['user'].iloc[0]
print(single_entry)