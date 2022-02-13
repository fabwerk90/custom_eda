def column_splitter(df):
    import pandas as pd
    
    dtypes = list(df.dtypes)
    
    list_of_dfs = []
    name_of_df = []
    
    if "object" in dtypes:
        df_strings = df.select_dtypes(include='object')
        list_of_dfs.append(df_strings)
        name_of_df.append("df_strings")
    
    if "int64" or "float64" in dtypes:
        df_numericals = df.select_dtypes(include=['int64', 'float64'])
        list_of_dfs.append(df_numericals)
        name_of_df.append("df_numericals")
    
    if "bool" in dtypes:
        df_bools = df.select_dtypes(include='bool')
        list_of_dfs.append(df_bools)
        name_of_df.append("df_bools")
    
    if "datetime64" in dtypes:
        df_datetimes = df.select_dtypes(include='datetime64')
        list_of_dfs.append(df_datetimes)
        name_of_df.append("df_datetimes")
    
    
    print(f"Found {len(list_of_dfs)} different column types.")
    print(f"Created following dfs with corresponding index:")
    print("------------------------------------------------")
    for index, name in enumerate(name_of_df):
        print(f"{index}: {name}")
    return list_of_dfs
