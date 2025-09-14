import pandas as pd
def detect_column_types(df: pd.DataFrame, threshold: int = 20) -> dict:
    categorical_cols = []
    numerical_cols = []
    text_cols = []
    for column in df.columns:
        series = df[column]
        dtype = series.dtype
        if dtype == "object" or pd.api.types.is_string_dtype(series):
            avg_length = series.dropna().astype(str).str.len().mean()
            unique_ratio = series.nunique() / max(len(series), 1)
            if avg_length > 30 or unique_ratio > 0.5:
                text_cols.append(column)
            else:
                categorical_cols.append(column)
        elif pd.api.types.is_numeric_dtype(series):
            unique_values = series.nunique()
            if unique_values < threshold:
                categorical_cols.append(column)
            else:
                numerical_cols.append(column)
        else:
            categorical_cols.append(column)
    return {
        "categorical": categorical_cols,
        "numerical": numerical_cols,
        "text": text_cols,
    }
