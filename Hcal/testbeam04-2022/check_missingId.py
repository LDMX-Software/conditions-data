import argparse, sys
parser = argparse.ArgumentParser(f'python {sys.argv[0]}')
parser.add_argument('input_file')
parser.add_argument('--value', default=0., type=float, help='Value to replace missing columns')
arg = parser.parse_args()

import pandas as pd

# read all det IDs
df_ref = pd.read_csv(f'hcal_detids_hex.txt',names=['Master'],header=0)
#print(df_ref)

# read input file and replace zeros
df = pd.read_csv(f'{arg.input_file}',comment='#')
df['DetID'] = df['DetID'].astype(str).apply( int, base=0 )
df['DetID'] = df['DetID'].apply( hex )
df.fillna(0, inplace=True)
columns = list(df.columns)

# are there any detIds not in file?
not_in_file = df_ref[~df_ref['Master'].isin(df['DetID'])]
# print how many are not in file
print(df_ref['Master'].isin(df['DetID']).value_counts())

# make a new dataframe with missing IDs
df_not = pd.DataFrame(columns=columns)
df_not['DetID'] = not_in_file
if 'flagged' in columns:
    df_not['flagged'] = df_not['flagged'].fillna(1)
print("df not ",df_not)
df_not = df_not.fillna(arg.value)

# append dataframe to old dataframe
df = df.append(df_not)
#print(df)
df.to_csv(f'{arg.input_file}',index=False)
