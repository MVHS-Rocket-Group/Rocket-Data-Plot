import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import yaml
fig = go.Figure()
df=pd.read_csv("example.csv")

with open("settings.yml", 'r') as stream:
    #Handle possible YAML errors
    try:
        data = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
#Add a line to the graph for each object specified in the YAML file
for items in data["rows-excluded"].split(" "):
    print(items[1:])
    fig.add_trace(go.Scatter(x=df["time (s)"], y=df[items[1:]],
                        mode=data["graph-type"],
                        name=items[1:]))
fig.show()