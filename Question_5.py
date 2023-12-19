import plotly.graph_objects as go
import pandas as pd
import plotly.figure_factory as ff

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']



df = pd.read_csv('winemag-data-130k-clean.csv')
df.dropna(subset=['price', 'points'], inplace=True)

def update_question_5(nb_quantiles):

    df['quality_quantile'] = pd.qcut(df['points'], nb_quantiles, labels=False, duplicates='drop')

    df['quality_quantile_labels'] = df['quality_quantile'].astype(str)

    for i in range(nb_quantiles):
        quantiles_min = df[df['quality_quantile'] == i]['points'].min()
        quantiles_max = df[df['quality_quantile'] == i]['points'].max()
        df.loc[df['quality_quantile'] == i, 'quality_quantile_labels'] = f'{quantiles_min}-{quantiles_max}'
        
    fig = go.Figure()

    quantiles = df['quality_quantile_labels'].unique()


    fig = go.Figure()

    quantiles = df['quality_quantile_labels'].unique()

    # list of list of prices 
    prices = [df[df['quality_quantile_labels'] == quantile]["price"].tolist() for quantile in quantiles]
            
    fig = ff.create_distplot(prices, quantiles, show_hist=False, colors=colors)

    # Add title
    fig.update_layout(title_text='Distribution of prices by quality quantiles')
    fig.update_xaxes(title_text='Price')

    return fig