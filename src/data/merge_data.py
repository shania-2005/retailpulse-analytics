import pandas as pd


def merge_data(df_2009, df_2010):
    """
    Merge both yearly datasets.
    """

    merged_df = pd.concat(
        [df_2009, df_2010],
        ignore_index=True
    )

    return merged_df