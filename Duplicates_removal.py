import streamlit as st
import pandas as pd
from datetime import datetime

# Title of the app
st.title('Duplicate Removal Tool')

# File upload section
st.header('Upload CSV Files')
uploaded_file1 = st.file_uploader("Choose a CSV file (1)", type='csv')
uploaded_file2 = st.file_uploader("Choose a CSV file (2)", type='csv')

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Read the uploaded files
    df1 = pd.read_csv(uploaded_file1,header=0,index_col=False)
    df2 = pd.read_csv(uploaded_file2,header=0,index_col=False)

    # Merging the dataframes
    frames = [df1, df2]
    df = pd.concat(frames)

    # Showing shape before removing duplicates
    st.write('Shape before removing duplicates:', df.shape)

    # Button to show duplicate values
    if st.button('Show Duplicate Values'):
        # Finding duplicate values
        duplicates = df[df.duplicated(subset=['Phone', 'Email'], keep=False)]
        st.write('Duplicate Values based on Phone and Email:')
        st.dataframe(duplicates)

    # Removing duplicates
    df.drop_duplicates(subset=['Phone', 'Email'], inplace=True)

    # Showing shape after removing duplicates
    st.write('Shape after removing duplicates:', df.shape)

     # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Download button with timestamp in filename
    st.download_button(
        label="Download Processed CSV",
        data=df.to_csv(index=False),
        file_name=f'merged_cleaned_{timestamp}.csv',
        mime='text/csv',
    )
