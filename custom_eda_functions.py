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

    sns.boxenplot(ax=axes[0], data=df)
    sns.ecdfplot(ax=axes[1], data=df)
    
    return fig


def relationships(df):
    import seaborn as sns
    sns.set_palette('rocket')
    
    pairplot = sns.PairGrid(data=df, height=3)

    pairplot = pairplot.map_lower(sns.regplot)
    pairplot = pairplot.map_diag(sns.boxenplot)
    
    return pairplot

    
def correlations(df):
    import matplotlib.pyplot as plt
    from heatmap import heatmap, corrplot
    import phik

    df_list = []
    
    pearson_df = df.corr()
    df_list.append(pearson_df)
    corrplot(pearson_df)
    print("Pearson Correlation:")
    plt.show()
    
    kendall_df = df.corr(method='kendall')
    df_list.append(kendall_df)
    corrplot(kendall_df)
    print("Kendall Correlation:")
    plt.show()
    
    spearman_df = df.corr(method='spearman')
    df_list.append(spearman_df)
    corrplot(spearman_df)
    print("Spearman Correlation:")
    plt.show()
    
    phi_k_df = df.phik_matrix()
    df_list.append(phi_k_df)
    corrplot(phi_k_df)
    print("Phi k Correlation:")
    plt.show()
    
    return df_list


def categories(df, category, numerical):
    import seaborn as sns
    sns.catplot(x=category, y=numerical, kind="boxen",data=df)
    
    
def text_eda(df, string_column):
    import re
    import string
    import matplotlib.pyplot as plt
    import seaborn as sns
    from wordcloud import WordCloud
    
    custom_punctuation = string.punctuation.replace("-","")
    
    
    text_list = df[f"{string_column}"].to_list()
    
    text_len = [len(text) for text in text_list]
    word_count = [len(text.split()) for text in text_list]
    
    fig, axes = plt.subplots(1, 2, figsize=(8,10))
    
    sns.boxenplot(ax=axes[0], data=text_len)
    plt.title("Text Length Distribution")
    plt.show()
    
    sns.boxenplot(ax=axes[1], data=word_count)
    plt.title("Word Count Distribution")
    plt.show()
    
    text_lower = [text.lower() for text in text_list]
    text_no_digits = [re.sub('\w*\d\w*','', text) for text in text_lower]
    text_no_punctuation = [re.sub('[%s]' % re.escape(custom_punctuation), '', text) for text in text_no_digits]
    text_no_whitespaces = [re.sub(' +',' ', text) for text in text_no_punctuation]
    cleaned_text = text_no_whitespaces
    text_corpus = " ".join(cleaned_text)
    
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text_corpus)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Occurences")
    plt.show()
    
    df.loc[:,"len_text"] = text_len
    df.loc[:,"word_count"] = word_count
    df.loc[:,"cleaned_text"] = cleaned_text
    
    return fig

    
    
    
    