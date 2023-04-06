reverse = slice(None, None, -1)
reverse = slice.literal[::-1]

all_rows_first_col = slice(None), slice(0)
all_rows_first_col = slice.literal[:, 0]

first_row_all_cols_but_last = slice(0), slice(None, -1)
first_row_all_cols_but_last = slice.literal[0, :-1]