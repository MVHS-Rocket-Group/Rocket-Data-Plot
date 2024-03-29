import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import yaml

with open("settings.yml", 'r') as stream:
    #Handle possible YAML errors
    try:
        data = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)


fig = go.Figure()
#Read the primary file.. change the name here, if you seek to use a different sample.
df=pd.read_csv(data["file-name"])

        
#Add a line to the graph for each object specified in the YAML file
# Row Excluded Code-- depreciated, but still supported through YAML tag
if (data["mode"]== "include"):
    for items in data["rows-modified"].split(" "):
        print(items[1:])
        fig.add_trace(go.Scatter(x=df["elapsed time (s)"], y=df[items[1:]],
                            mode=data["graph-type"],
                            name=items[1:]))
if (data["mode"]== "exclude"): # If an item is in rows modified, next iteration. Else, plot it.
    for item in df.columns.values:
        if (item in data["rows-modified"] or item == "elapsed time (s)" or item== "Unnamed: 0"):
            pass
        else:
            fig.add_trace(go.Scatter(x=df["elapsed time (s)"], y=df[item],
                            mode=data["graph-type"],
                            name=item))
fig.update_layout(
    title=go.layout.Title(
        text="Rocket Data",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Time",
            font=dict(
                family="Times New Roman",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Value",
            font=dict(
                family="Times New Roman",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)

fig.show()