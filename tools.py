import pandas as pd
import plotly.express as px

def quantiles_data(df:pd.DataFrame, nb_quantiles:int = 2) -> pd.DataFrame:
    """
    This function takes a dataframe and return a dataframe with the quantiles of the dataframe
    """
    df['quality_quantile'] = pd.qcut(df['quality'], nb_quantiles, labels=False, duplicates='drop')

    df['quality_quantile_labels'] = df['quality_quantile'].astype(str)

    for i in range(nb_quantiles):
        quantiles_min = df[df['quality_quantile'] == i]['quality'].min()
        quantiles_max = df[df['quality_quantile'] == i]['quality'].max()
        df.loc[df['quality_quantile'] == i, 'quality_quantile_labels'] = f'{quantiles_min}-{quantiles_max}'
    
    return df

def plot_dist_price_quantiles_quality(df,nb_quantiles:int = 2):
    """
    This function takes a dataframe and return a plot with the distribution of price for each quantile of quality
    """
    
    # retrive labels of quantiles as "over .."
    
    
    df = quantiles_data(df, nb_quantiles)
    
    # color = quality_quantile to have the same color for each quantile of quality and the labels are the labels of the quantiles
    return px.histogram(df, x="price", color="quality_quantile_labels", nbins=1000,
                        log_y=True,  # Set log scale on the y-axis
                        opacity=0.7,  # Adjust opacity for overlapping distributions
                        title="Distribution of Prices Across Quality Quantiles",
                        labels={"price": "Price", "quality_quantile_labels": "Quality Quantile"})