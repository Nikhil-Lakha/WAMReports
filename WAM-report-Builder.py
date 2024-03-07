# Import necessary libraries
import streamlit as st
import pandas as pd
import pygwalker as pyg

# Set up Streamlit app
st.title('CSV Upload and Display App')

# Create a function to upload CSV file and display DataFrame
def upload_csv():
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded DataFrame:")
        st.write(df)

        # Use PyGWalk to display DataFrame
        st.write("### PyGWalk Visualization:")
        pyg.show(df)

# Call the function
upload_csv()
