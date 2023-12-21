import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_csv('winemag-data-130k-clean.csv')

df_winery = df.groupby(['country', 'province', 'winery', "continent"]).agg({'points': 'median', 'variety': 'nunique'}).reset_index()

df_winery_grouped = df_winery.groupby(['variety']).agg({'points': 'median', 'winery': 'nunique'}).reset_index()

# rename variety to number of varieties and winery to number of wineries
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


fig6 = go.Figure()

fig6.add_trace(go.Scatter(
    x=df_winery_grouped['number of varieties'], 
    y=df_winery_grouped['points'],
    marker = dict(
        size=16,
        line = dict(width=2, color='DarkSlateGrey'),
        color='blue'),
    mode='markers',
    name='All',
    hovertemplate='Un vigneron qui produit %{x} vins obtient %{y} points médians sur ces vins.')
)

fig6.update_xaxes(title_text='Nombre de variétés (tout producteurs confondus)')
fig6.update_yaxes(title_text='Points médians')

fig6.update_layout(
    title=dict(
        text="Points obtenus en fonction du nombre de variétés produites",  # Texte du titre
        font=dict(
            size=20,  # Taille de la police du titre
            color="Black"  # Couleur du titre
        ),
        # x=0.5,  # Centrer le titre
        # y=0.95  # Ajuster la position verticale du titre
    ),
    margin=dict(l=0, r=0, t=50, b=0)  # Ajustez les marges si nécessaire
)