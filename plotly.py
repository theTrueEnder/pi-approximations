# Libraries
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import webbrowser
import json
with open('settings.json', 'r') as f:
    settings = json.load(f)
    
    
fp = settings['path']
import os
os.chdir(fp)

xmin = settings['xmin']
xmax = settings['xmax']
generate_plot = True
filter = settings['filter']
fname = settings['plot_name']


def f(x):
    try:
        return np.abs(1.0 / np.sin(x))
    except ZeroDivisionError:
        return 0

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


if __name__ == 'main':
    print('Creating plot...')
    fig = go.Figure()

    # Add the scatter trace
    fig.add_trace(go.Scatter( 
        x=df['x'], # Variable in the x-axis
        y=df['y'], # Variable in the y-axis
        mode='markers', # This explicitly states that we want our observations to be represented by points
        
        # Properties associated with points 
        marker=dict(
            size=2, # Size
            color='red', # Color
            opacity=0.8, # Point transparency 
            line=dict(width=1, color='black') # Properties of the edges
        ),
    ))

    # Customize the layout
    fig.update_layout(
        title='Integer Approximations of Pi', # Title
        xaxis_title='Value', # x-axis name
        yaxis_title='Quality of Approximation', # y-axis name
        width=1400,  # Set the width of the figure
        height=800,  # Set the height of the figure
    )

    fig.write_html(settings['data_path'] + fname)
    print('Plot created')

    # fig.show()
    # filename = 'file:///'+"D:/Users/ender/OneDrive/Documents/Coding Workspaces/Python Workspace/" + fname
    # webbrowser.open_new_tab(filename) 
    # print('Plot created\n')