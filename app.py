# app.py
import dash
from dash import html, dcc
from Question_1 import fig  # Importez la figure depuis le fichier Question_1.py

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Définition du layout de l'application avec la figure importée
app.layout = html.Div([
    html.H1('Wine Reviews', style={'font-family': 'Helvetica', 'fontSize': 40}),
    html.P("Ce projet présente différentes visualisations de données liées au domaine du vin, avec un accent sur la qualité des vins.", style={'font-family': 'Helvetica', 'fontSize': 20}),
    html.Details([
        html.Summary('Comment utiliser les visualisations ?'),
        html.P('Plusieurs interactions sont possibles avec chaque graphe :'),
        html.Ul([
            html.Li('Zoom (en utilisant la souris directement)'),
            html.Li('Tri (en cliquant sur les carré de couleurs disponible à droite des graphes)'),
            html.Li('Détails (en passant son curseur sur un élément du graphe)'),
        ]),
    ], style={'font-family': 'Helvetica', 'fontSize': 20}),
    html.Details([
        html.Summary('Comment sont notés les vins ?'),
        html.P('Les notes proviennent du site WineEnthusiast '),
    ], style={'font-family': 'Helvetica', 'fontSize': 20}),

    dcc.Graph(
        id='question-1',
        figure=fig  # Utilisation de la figure importée
    )
])

# Main clause pour exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
