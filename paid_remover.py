import streamlit as st
import pandas as pd
from io import StringIO

def remove_rows_and_save(df_large, df_small, key_column):
    df_modified = df_large.merge(df_small[key_column], on=key_column, how='left', indicator=True)
    df_new = df_modified[df_modified['_merge'] == 'left_only'].drop(columns=['_merge'])
    return df_new


st.title('Paid Remover Tool')

# File uploaders
file1 = st.file_uploader("Upload paid sheet CSV file", type=["csv"])
file2 = st.file_uploader("Upload lead sheet CSV file", type=["csv"])
# key_column = st.text_input("Enter the key column name for matching rows")
key_column=['Email']


if st.button('Process Files'):
    if file1 is not None and file2 is not None and key_column:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        result_df = remove_rows_and_save(df2, df1, [key_column])

        # Convert DataFrame to CSV for download
        csv = result_df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="processed_file.csv">Download Processed CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("Please upload both CSV files and specify the key column.")
