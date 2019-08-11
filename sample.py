import numpy as np
import plotly.express as px
import pandas as pd
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv", encoding="iso-8859-1"
)
df.head()

fig = px.histogram(df, x="Country").update_xaxes(categoryorder="total descending")
fig.show()