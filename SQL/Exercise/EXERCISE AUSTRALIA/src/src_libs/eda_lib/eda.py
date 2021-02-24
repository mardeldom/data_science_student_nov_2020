

def choose_x_y(df, col_name, col_name2, col_name3, col_name4, col_name5, col_name6, target_col=None):
    x_data= df.drop(columns=[col_name,col_name2, col_name3, col_name4, col_name5, col_name6])
    if target_col:
        y_data = df[target_col]
        return x_data, y_data
    else:
        return x_data