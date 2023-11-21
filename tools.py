import pandas as pd
import plotly.express as px

def quantiles_data(df:pd.DataFrame, nb_quantiles:int = 2) -> pd.DataFrame:
    """
    This function takes a dataframe and return a dataframe with the quantiles of the dataframe
    """
    df['quality_quantile'] = pd.qcut(df['quality'], nb_quantiles, labels=False, duplicates='drop')
    
    # replace each quality_quantile by the min of the quality in the quantile
    for i in range(nb_quantiles):
        df.loc[df['quality_quantile'] == i, 'quality_quantile'] = f"over {df[df['quality_quantile'] == i]['quality'].min()}"
    
    return df

def plot_dist_price_quantiles_quality(df,nb_quantiles:int = 2):
    """
    This function takes a dataframe and return a plot with the distribution of price for each quantile of quality
    """
    
    # retrive labels of quantiles as "over .."
    
    
    df = quantiles_data(df, nb_quantiles)
    prices = df['price']
    
    # color = quality_quantile to have the same color for each quantile of quality and the labels are the labels of the quantiles
    fig = px.histogram(df, x=prices, color="quality_quantile")
    fig.show() 