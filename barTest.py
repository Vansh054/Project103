import pandas as pd
import plotly.express as pe

df = pd.read_csv("data.csv")
graph = pe.bar(df,x="date",y="cases",color="country")
graph.show()
