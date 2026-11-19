import pandas as pd
import functools
import numpy as np
import math
import matplotlib.pyplot as plt
from src.config import HIST
from src.config import BAR_CHART


def top_10(table):
#    average_ratings_bymoviestopdown = (
#        average_ratings_bymovies
#        .sort_values('rating', ascending=False)
#)
    top = table.sort_values('Price', ascending=False)
    return top_ten.head(10)



def graph(top_10table):
#plot histogram
#    df_data3.hist(column="rating", figsize=(15, 10), bins=10)
#    plt.savefig('../img/show_histogram')
    table.plot(kind="hist", y="Price", figsize=(12, 8), bins=10)
    plt.savefig(HIST)
    table.plot(kind="barh", y="Price", figsize=(12, 8), x="Book title")
    plt.savefig(BAR_CHART)
    return



