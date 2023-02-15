import argparse, sys

parser = argparse.ArgumentParser(f"python {sys.argv[0]}")
parser.add_argument("input_file")
parser.add_argument(
    "--value", default=0.0, type=float, help="Value to replace missing columns"
)
arg = parser.parse_args()

import pandas as pd

# read input file and duplicate to account for both ends of a bar
df_0 = pd.read_csv(
    f"{arg.input_file}", comment="#", usecols=["Det_id_0", "bx_shift", "mean_shift"]
)
df_0.rename(columns={"Det_id_0": "DetID"}, inplace=True)

# second digi ID
df_1 = pd.read_csv(
    f"{arg.input_file}", comment="#", usecols=["Det_id_1", "bx_shift", "mean_shift"]
)
df_1.rename(columns={"Det_id_1": "DetID"}, inplace=True)
# has a mean shift of 0
df_1["mean_shift"].values[:] = 0

# append dataframe to old dataframe
df = pd.concat([df_0, df_1])
df.sort_values(by=['DetID'], inplace=True)
print(df[df.DetID.duplicated(keep='first')])

df_nonduplicate = df[df.DetID.duplicated(keep='first')]

new_file = (arg.input_file).replace(".csv", "_expand.csv")
df['DetID'].apply(lambda x: str(hex(x)))
df.to_csv(new_file, index=False)
