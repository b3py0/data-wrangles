## HELLINGER transformation:
'''
to call this function, move workbook to working folder, import transformation as tm
and then call with tm.hellinger(df kwargs= df_type('full' or None), ids = row labels).
'''

def hellinger(df, **kwargs):
    import numpy as np
    import pandas as pd
    '''
    ids --> this is the first column (or columns) with row lables (e.g. sample numbers, depth etc.)
    and is a separate df.

    df --> these columns are the counts (with the column headers) of the cleaned data matrix containing just
    raw count frequencies and zeros (strings need removing first).

    df_type --> if left blnk, this just returns the matrix, if 'full' returns df with row labels.
    '''
    ids = kwargs.get('ids', None)
    df_type = kwargs.get('df_type', None)

    if df_type == 'full':
        tm = df.apply(lambda x: np.sqrt(x / df.sum(axis=1)))
        tm_df = pd.concat([ids, tm], axis=1)
        return tm_df
    else:
        tm = df.apply(lambda x: np.sqrt(x / df.sum(axis=1)))
        return tm
