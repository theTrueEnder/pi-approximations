import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import json
with open('settings.json', 'r') as f:
    settings = json.load(f)
    

fp = settings['path']
import os
os.chdir(fp)

datatype = 'float32'
shape = [settings['xmax'],2]
filename = settings['plot_name']

def main():
    xmin, xmax = settings['xmin'], settings['xmax']
    # xmax/=2 if 'negative' in settings['filter'] else xmin
    
    print('Reading csv...')
    df = pd.read_csv(settings['path']+'data\\' +settings['data_name']+'.csv')
    print('Read complete')
    print('Filter beginning...')
    df = df[(df.x > xmin) & (df.x < xmax)]
    plt.plot(df['x'], df['y'], 'r,')
    plt.grid(True)
    plt.title("Pi Plot")
    plt.xlabel("Value")
    plt.ylabel("Approximation Accuracy")
    plt.minorticks_on()
    if settings['interactive']:
        plt.ion()
    if settings['log_y']:
        plt.yscale('log')
    
    print('Plot configured')
    plt.savefig(fp+filename+'.png')
    print('Plot saved\n')
    print('Range: ', f'[{xmin}, {xmax}]')
    print('Number of points: ', df.shape[0])
    print()
    print('Top 5 points:')
    pts = df.nlargest(5, 'y')
    print(pts.to_string(index=False, justify='left'))

if __name__ == "__main__":
    main()  