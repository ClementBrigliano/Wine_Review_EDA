import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_csv('winemag-data-130k-clean.csv')

df_winery = df.groupby(['country', 'province', 'winery', "continent"]).agg({'points': 'median', 'variety': 'nunique'}).reset_index()

df_winery_grouped_continent  = df_winery.groupby(['variety', 'continent']).agg({'points': 'mean', 'winery': 'nunique'}).reset_index()
df_winery_grouped = df_winery.groupby(['variety']).agg({'points': 'mean', 'winery': 'nunique'}).reset_index()

# rename variety to number of varieties and winery to number of wineries
df_winery_grouped_continent.rename(columns={'variety': 'number of varieties', 'winery': 'number of wineries'}, inplace=True)
df_winery_grouped.rename(columns={'variety': 'number of varieties', 'winery': 'number of wineries'}, inplace=True)

# assign a friendly  color to each continent
color_palette = {
    "Asia": "#4477AA",  # Tol's Bright Blue
    "Europe": "#66CCEE",  # Tol's Cyan
    "Africa": "#228833",  # Tol's Green
    "North America": "#CCBB44",  # Tol's Yellow
    "South America": "#EE6677",  # Tol's Red
    "Oceania": "#AA3377",  # Tol's Purple
}

# create a new column with the color for each continent
df_winery_grouped_continent['color'] = df_winery_grouped_continent['continent'].apply(lambda x: color_palette[x])


fig6 = go.Figure()



fig6.add_trace(go.Scatter(
    x=df_winery_grouped['number of varieties'], 
    y=df_winery_grouped['points'],
    marker = dict(
        size=16,
        line = dict(width=2, color='DarkSlateGrey'),
        color='blue'),
    mode='markers',
    name='All')
)

fig6.add_trace(go.Scatter(
    visible=False,
    x=df_winery_grouped_continent['number of varieties'], 
    y=df_winery_grouped_continent['points'],
    marker=dict(
        size=16,
        line = dict(width=2, color='DarkSlateGrey'),
        color=df_winery_grouped_continent['color']),
    hoverinfo='text',
    hovertext=df_winery_grouped_continent['continent'],
    mode='markers',
    name='Continent')
)

fig6.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            showactive=True,
            x=0.4,  # Position horizontale ajustée
            y=1.1,  # Position verticale ajustée
            xanchor='left',
            yanchor='top',
            buttons=list([
                dict(label="non groupé",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Points vs nombre de variétés"}]),
                dict(label="continent",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Points vs nombre de variétés par continent"}]),
            ]),
        )
    ]
)

fig6.update_layout(
    title=dict(
        text="Points vs nombre de variétés",  # Texte du titre
        font=dict(
            size=20,  # Taille de la police du titre
            color="Black"  # Couleur du titre
        ),
        # x=0.5,  # Centrer le titre
        # y=0.95  # Ajuster la position verticale du titre
    ),
    margin=dict(l=0, r=0, t=50, b=0)  # Ajustez les marges si nécessaire
)
