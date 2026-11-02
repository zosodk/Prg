import plotly.graph_objects as go

#fig = go.Figure(data=go.Table(header=dict(values=["Navn", "Alder"]),cells=dict(values=[["Alice", "Bob"],[25, 30]])))

#fig.show()

labels=["A", "B", "C"]
values=[12, 23, 32]


fig = go.Figure(data=go.Bar(x=labels, y=values, marker_color=["black", "grey", "white"]))
fig.show()
