import pandas as pd
import plotly.graph_objects as go

def update_question_5(price_limit):
    # Charger votre dataset
    df = pd.read_csv('winemag-data-130k-clean.csv')
    df.dropna(subset=['price', 'points'], inplace=True)

    # Définition des catégories de qualité basées sur les points
    bins = [0, 82, 86, 89, 93, 97, 100]
    labels = ['Acceptable', 'Bon', 'Très Bon', 'Excellent', 'Superbe', 'Classique']
    df['Catégorie de Qualité'] = pd.cut(df['points'], bins=bins, labels=labels, include_lowest=True)

    # Définition des catégories de prix
    df['Catégorie de Prix'] = pd.cut(df['price'], bins=[0, price_limit, float('inf')], labels=['Moins de ' + str(price_limit), 'Plus de ' + str(price_limit)])

    # Création d'un tableau croisé pour compter le nombre de vins
    pivot_count = pd.crosstab(df['Catégorie de Qualité'], df['Catégorie de Prix'])

    # Calculer les pourcentages pour chaque catégorie de prix
    pivot_percent_under = (pivot_count.iloc[:, 0] / df[df['price'] <= price_limit]['price'].count()) * 100
    pivot_percent_over = (pivot_count.iloc[:, 1] / df[df['price'] > price_limit]['price'].count()) * 100

    # Créer le graphique à barres
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Moins de ' + str(price_limit),
        x=pivot_percent_under.index,
        y=pivot_percent_under,
        text=pivot_percent_under.apply(lambda x: f'{x:.1f}%'),  # Ajouter le pourcentage sur les barres
        customdata=pivot_percent_under.index,
        hovertemplate='Un vin à moins de ' + str(price_limit) + '$ à %{text} de chance d\'être %{customdata}.<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        name='Plus de ' + str(price_limit),
        x=pivot_percent_over.index,
        y=pivot_percent_over,
        text=pivot_percent_over.apply(lambda x: f'{x:.1f}%'),  # Ajouter le pourcentage sur les barres
        customdata=pivot_percent_over.index,
        hovertemplate='Un vin à plus de ' + str(price_limit) + '$ à %{text} de chance d\'être %{customdata}.<extra></extra>'
    ))
    fig.update_layout(
        barmode='group',
        title=dict(
            text="Pourcentage de chance qu'un vin appartienne à une catégorie en fonction de son prix",
            font=dict(
                size=20,
                color="Black"
            ),
        ),
        xaxis_title='Catégorie de qualité',
        yaxis_title='Pourcentage (%)',
        legend_title_text='Prix ($)'
    )

    return fig
