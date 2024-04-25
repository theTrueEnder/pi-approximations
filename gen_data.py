import pandas as pd
import numpy as np
import json
with open('settings.json', 'r') as f:
    settings = json.load(f)
    
def data_to_csv(df_in, fn):
    print('Writing to file...')
    df_in.to_csv(fn, sep=',', encoding='utf-8', index=False)
    print('File written')
    
    
xmin = settings['xmin']
xmax = settings['xmax']
# generate_plot = True
filter = settings['filter']
fname = settings['path'] + 'data\\' + settings['data_name'] + '.csv'


def f(x):
    try:
        return np.abs(1.0 / np.sin(x))
    except ZeroDivisionError:
        return 0

# gen data into a pandas df
print('Creating data...')
xpoints = np.arange(xmin, xmax)
ypoints = np.apply_along_axis(f, 0, xpoints)
df = pd.DataFrame({'x': xpoints,
                   'y': ypoints})
print('Data created')



# filter out negative values
if 'negative' in filter:
    df = df[df.y > 0]
    print('Data filtered')



# prune unnecessary values
if 'prune' in filter:
    # 1.1 -> 34k removed
    # 1.5 -> 67k removed
    
    num_before = df.shape[0]
    big_condition = (df['y'] > 1.5)
    half_condition = ((df['x'] % 2) == 0)
    
    big = df[big_condition]
    small = df[~big_condition]
    halfsmall = small[half_condition]
    
    df = pd.concat([big, halfsmall])
    print(f'Data pruned ({num_before-df.shape[0]} values removed)')


data_to_csv(df, fname)