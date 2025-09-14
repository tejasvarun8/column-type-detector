import pandas as pd
from ds_helper.column_detector import detect_column_types

data = {
    "Age": [18, 20, 21, 19, 22],
    "Gender": ["M", "F", "M", "M", "F"],
    "ZIP": [560001, 560002, 560003, 560001, 560002],
    "Review": [
        "Great product!",
        "Not good",
        "Okay",
        "Loved it",
        "Terrible experience, never buying again"
    ]
}
df = pd.DataFrame(data)
print("Detected column types:")
print(detect_column_types(df))
