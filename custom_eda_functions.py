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

def numerical_distributions(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_palette('rocket')
    
    fig, axes = plt.subplots(2, 1, figsize=(10,12))

    sns.boxenplot(ax=axes[0], data=df_num)
    sns.ecdfplot(ax=axes[1], data=df_num)


def relationships(df):
    import seaborn as sns
    sns.set_palette('rocket')
    
    pairplot = sns.PairGrid(data=df, height=3)

    pairplot = pairplot.map_lower(sns.regplot)
    pairplot = pairplot.map_diag(sns.boxenplot)

    
    
    
    