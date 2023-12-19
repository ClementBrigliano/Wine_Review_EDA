import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('winemag-data-130k-clean.csv')
df.dropna(subset=['continent', 'points', 'price'], inplace=True)

fig3 = make_subplots(1, 1)
continents = df["continent"].unique()

trace_continents = []
color_palette = {
    "Asia": "#4477AA",
    "Europe": "#66CCEE",
    "Africa": "#228833",
    "North America": "#CCBB44",
    "South America": "#EE6677",
    "Oceania": "#AA3377",
}
max_production = 0
for continent in continents:
    df_continent = df[df["continent"] == continent]
    countries = df_continent["country"].unique()
    for country in countries:
        df_country = df_continent[df_continent["country"] == country]
        if max_production < len(df_country):
            max_production = len(df_country)
        hover_text = [
            f"{country}<br>Points médians : {df_country['points'].median(axis=0)}<br>Nombre de vins différents produits : {len(df_country)}"
            for _ in range(len(df_country))
        ]
        fig3.add_trace(
            go.Scatter(
                x=[len(df_country)],
                y=[df_country["points"].median(axis=0)],
                mode="markers",
                name=country,
                marker=dict(
                    size=15,
                    line=dict(width=2),
                    color=color_palette.get(continent, "#17becf"),
                ),
                text=hover_text,
                hoverinfo="text",
                visible=True,
            )
        )
        trace_continents.append(continent)

buttons = []

buttons.append(
    dict(
        label="Tous",
        method="update",
        args=[
            {"visible": [True] * len(trace_continents)},
            {"title": "Distribution de la qualité par rapport à la quantité dans le monde"},
        ],
    )
)

for continent in continents:
    label_continent = {
        "Asia": "Asie",
        "Europe": "Europe",
        "Africa": "Afrique",
        "North America": "Amérique du Nord",
        "South America": "Amérique du Sud",
        "Oceania": "Océanie"
    }.get(continent, continent)
    
    buttons.append(
        dict(
            label=label_continent,
            method="update",
            args=[
                {"visible": [continent == trace_continent for trace_continent in trace_continents]},
                {"title": f"Distribution de la qualité par rapport à la quantité en {label_continent}"},
            ],
        )
    )

fig3.update_layout(
    showlegend=True,
    updatemenus=[
        {
            "buttons": buttons,
            "direction": "down",
            "pad": {"r": 10, "t": 10},  # Ajustez si nécessaire pour l'espacement
            "showactive": True,
            # Les valeurs suivantes positionnent les boutons en haut à droite
            "x": 0.7,
            "xanchor": "right",
            "y": 1.25,
            "yanchor": "top",
        }
    ],
    xaxis_title="Nombre de vins différents produits",
    yaxis_title="Points médians",
    title=dict(
    text="Distribution de la qualité par rapport à la quantité dans le monde",  # Texte du titre
    font=dict(
        size=20,  # Taille de la police du titre
        color="Black"  # Couleur du titre
    ),
    # x=0.5,  # Centrer le titre
    # y=0.95  # Ajuster la position verticale du titre
    ),  
    xaxis=dict(rangeslider=dict(visible=True), type="linear"),
    xaxis_range=[-1000, max_production + 1000],
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0)
)