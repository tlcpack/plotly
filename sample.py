import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_v = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv", encoding="iso-8859-1"
)
df.head()

labels=df.Status.unique()
values=df['Status'].value_counts()

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# fig = px.histogram(df, x="Country", color="Status").update_xaxes(categoryorder="total descending")
# fig = px.bar(df, x='Volcano Name', y='Elev', color='Type', height=400)

# Making a globe
# fig = go.Figure(data=go.Scattergeo(
#     lon = df['Longitude'],
#     lat = df['Latitude'],
#     mode = 'markers',
#     showlegend=False,
#     marker=dict(color="crimson", size=4, opacity=0.8)
# ))

# fig.update_geos(
#     projection_type="orthographic",
#     landcolor="white",
#     oceancolor="MidnightBlue",
#     showocean=True,
#     lakecolor="LightBlue"
# )
fig = go.Figure(data=[go.Surface(z=df_v.values)])

fig.update_layout(title='Volcano', autosize=False,width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))

fig.show()