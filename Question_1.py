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
fig1 = go.Figure()

# Trace pour la qualité des vins
fig1.add_trace(
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
fig1.add_trace(
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

# Suppression de l'annotation statique et mise à jour dynamique du titre
fig1.update_layout(
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
                dict(label="Qualité des vins",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Qualité des vins par pays"}]),
                dict(label="Production de vins",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Production de vins par pays"}]),
            ]),
        )
    ]
)

# Mise à jour du layout pour afficher correctement la première trace
fig1.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    title=dict(
        text="Qualité des vins par pays",  # Texte du titre
        font=dict(
            size=20,  # Taille de la police du titre
            color="Black"  # Couleur du titre
        ),
        # x=0.5,  # Centrer le titre
        # y=0.95  # Ajuster la position verticale du titre
    ),
    margin=dict(l=0, r=0, t=50, b=0)  # Ajustez les marges si nécessaire
)