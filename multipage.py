# joins multipage records and their measurements into new, pipe-separated cells and writes to new csv

import pandas as pd

df = pd.read_csv('multi.csv')

condense = df.groupby('record', as_index=False)['file','physical_description_size'].agg('|'.join)

meas = condense['physical_description_size'].str.split('|').apply(set).str.join('|')

condense['meas'] = meas

export_csv = condense.to_csv (r'condensedfiles.csv', index = None, header=True)

