
from config import FILE_PATH
from config import COLS_TO_DROP

from preprocessing import read_csv
from preprocessing import check_dtype
from preprocessing import convert_dtype
from preprocessing import check_nulls
from preprocessing import clip_outliers
from preprocessing import plot_boxplot
from preprocessing import show_duplicates
from preprocessing import remove_duplicates
from preprocessing import draw_histogram
from preprocessing import draw_countplot

data = read_csv(FILE_PATH)

check_dtype(data)           # ---> ["sex","smoker","region"] should be converted to category
convert_dtype(data,COLS_TO_DROP,"category")
check_dtype(data)

check_nulls(data)           # ---> There is no nulls

plot_boxplot(data)
clip_outliers(data)
plot_boxplot(data)

show_duplicates(data)
remove_duplicates(data)
show_duplicates(data)

draw_histogram(data)
draw_countplot(data)