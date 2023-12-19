import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go

# Chargement des données
df = pd.read_csv('winemag-data-130k-clean.csv')
df.dropna(subset=['country', 'points'], inplace=True)

# Calcul de la moyenne de la qualité pour chaque pays et du nombre de vins produits
country_stats = df.groupby('country')['points'].agg(['mean', 'count']).reset_index()
country_stats.rename(columns={'mean': 'Points moyens', 'count': 'Nombre de vins'}, inplace=True)

# Chargement des données géographiques des pays
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Fusion des données géographiques et des données sur le vin
merged_data = world.merge(country_stats, left_on='name', right_on='country', how='left')

# Création des traces pour la figure
fig = go.Figure()

# Trace pour la qualité des vins
fig.add_trace(
    go.Choropleth(
        locations=merged_data['iso_a3'],
        z=merged_data['Points moyens'],
        text=merged_data['name'],
        hoverinfo='text+z',
        colorscale='RdYlGn',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Qualité',
    )
)

# Trace pour le nombre de vins produits, invisible par défaut
fig.add_trace(
    go.Choropleth(
        visible=False,
        locations=merged_data['iso_a3'],
        z=merged_data['Nombre de vins'],
        text=merged_data['name'],
        hoverinfo='text+z',
        colorscale='RdYlGn',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Production',
    )
)

# Mise à jour du layout pour le titre global
# fig.update_layout(
#     title_text='Analyse des vins dans le monde',  # Titre global
# )

# Modification de l'emplacement des boutons pour être horizontaux et à droite du titre
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            showactive=True,
            x=0.4,  # Position horizontale à ajuster selon la longueur du titre
            y=1.25,  # Position verticale juste au-dessus de la carte
            xanchor='left',
            yanchor='top',
            buttons=list([
                dict(label="Qualité des vins",
                     method="update",
                     args=[{"visible": [True, False]}]),
                dict(label="Production de vins",
                     method="update",
                     args=[{"visible": [False, True]}]),
            ]),
        )
    ]
)

# Mise à jour du layout pour afficher correctement la première trace et pour fixer les titres
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations=[
        dict(
            text='Analyse des vins dans le monde',  # Titre global
            showarrow=False,
            xref='paper',
            yref='paper',
            x=0.05,
            y=1.2,
            xanchor='left',
            yanchor='bottom',
            font=dict(
                size=20,
                color='black'
            ),
        )
    ],
    margin={"r":0,"t":100,"l":0,"b":0}  # Ajuster si nécessaire pour l'espace du titre
)

# # Affichage de la carte
# fig.show()
