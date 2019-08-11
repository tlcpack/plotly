import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv", encoding="iso-8859-1"
)
df.head()

labels=df.Status.unique()
values=df['Status'].value_counts()
# fig = px.histogram(df, x="Country").update_xaxes(categoryorder="total descending")
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()