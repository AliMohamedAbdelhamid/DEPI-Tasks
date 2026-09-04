
import pandas as pd
from config import FILE_PATH
from config import COLS_TO_DROP

import preprocessing as fn

df = fn.Read_Data_File(FILE_PATH)
fn.Drop_unnecessary_features(df, COLS_TO_DROP)
print(df)

fn.Check_data_type(df)