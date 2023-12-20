# app.py
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from Question_1 import fig1
from Question_3 import fig3
from Question_4 import fig4
from Question_5 import update_question_5

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Définition du layout de l'application avec la figure importée
app.layout = html.Div([
    # Introduction (HTML)
    html.H1('Wine Reviews', style={'font-family': 'Helvetica', 'fontSize': 40}),
    html.P("Ce projet présente différentes visualisations de données liées au domaine du vin, avec un accent sur la qualité des vins.", style={'font-family': 'Helvetica', 'fontSize': 20}),
    html.Details([
        html.Summary('Comment utiliser les visualisations ?'),
        html.P('Plusieurs interactions sont possibles selon le type de grahiques :'),
        html.Ul([
            html.Li('Zoom (en utilisant la souris directement)'),
            html.Li('Tri (en cliquant sur les carré de couleurs disponible à droite des graphes)'),
            html.Li('Détails (en passant son curseur sur un élément du graphe)'),
        ]),
    ], style={'font-family': 'Helvetica', 'fontSize': 20}),
    html.Details([
        html.Summary('Comment sont notés les vins ?'),
            html.P([
        'Toutes les données et les notes utilisées proviennent du site ',
        html.A('WineEnthusiast', href='https://www.winemag.com/', target='_blank'),
        ' et sont attribuées par des experts en vin. Les notes sont comprises entre 80 et 100 :'
    ]),
        html.Ul([
            html.Li('80-82 : acceptable'),
            html.Li('83-86 : bon'),
            html.Li('87-89 : très bon'),
            html.Li('90-93 : excellent'),
            html.Li('94-97 : superbe'),
            html.Li('98-100 : classique'),
        ]),
        html.P("Sachant que 50% des vins sont notés entre 86 et 90 et que la moyenne est de 88.2.", style={'font-family': 'Helvetica', 'fontSize': 20}),
    ], style={'font-family': 'Helvetica', 'fontSize': 20}),
    html.Br(),

    # Graphes (figures Plotly importées depuis les .py)
    html.P("Commençons par une vue d'ensemble des vins dans le monde. Sans surprise, l'Europe et les États-Unis sont les principaux producteurs de vin de qualité.", style={'font-family': 'Helvetica', 'fontSize': 20}),
    dcc.Graph(
        id='question-1',
        figure=fig1  # Utilisation de la figure importée
    ),

    html.Br(),
    html.Br(),

    html.P("Est-ce qu'un pays qui produit beaucoup de vin le fait au détriment de la qualité ? Ou, au contraire, est-ce qu'un pays qui produit beaucoup de vin à le savoir faire nécessaire pour en produire de bonne qualité ? La réponse semble être non, il n'y aucune corrélation entre les deux.", style={'font-family': 'Helvetica', 'fontSize': 20}),
    dcc.Graph(
        id='question-3',
        figure=fig3  # Utilisation de la figure importée
    ),

    html.Br(),
    html.Br(),

    html.P(
            "Chaque vin se voit attribuer une critique par un expert. Quels sont les mots les plus utilisés dans les critiques positives ? (Sont considérés comme positives les critiques ayant une note supérieure à 90). On remarque que ces mots changent en fonction de la provenance du vin.",
            style={"font-family": "Helvetica", "fontSize": 20},
        ),
    dcc.Graph(id="question-4", figure=fig4),  # Utilisation de la figure importée
    
    html.Br(),
    
    html.P(
        "Un vin cher est-il forcément de bonne qualité ? Il semblerait que oui. Plus un vin est cher, plus ces chances d'appartenir à une catégorie de qualité élevée sont grandes.",
        style={"font-family": "Helvetica", "fontSize": 20},
    ),

    # Question 5 avec champ de saisie pour la limite de prix
    html.Label(
        'Limite de prix ($) : ', 
        style={'font-family': 'Helvetica', 'fontSize': 18}  # Appliquer le style ici
    ),
    dcc.Input(
        id='price-input-5', 
        type='number', 
        value=100, 
        min=0,
        step=1,
        style={'font-family': 'Helvetica', 'fontSize': 15}  # Modifiez la police et la taille ici
    ),
    dcc.Graph(id='question-5-graph'),  # Graphique pour Question 5
   
], style={'margin-left': '50px', 'margin-right': '50px'})

# Callback pour la Question 5
@app.callback(
    Output('question-5-graph', 'figure'),
    [Input('price-input-5', 'value')]
)
def update_graph_5(price_limit):
    return update_question_5(price_limit)

# Main clause pour exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=False)
