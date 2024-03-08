# Import necessary libraries
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

# Set Streamlit to be wide by default
st.set_page_config(layout="wide", page_title="Vodapay Dashboard", initial_sidebar_state="collapsed")

# Set up Streamlit app
st.title('CSV Upload and Display App')

# Create a function to upload CSV file and display DataFrame
def upload_csv():
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=';')
        st.write("### Uploaded DataFrame:")
        st.write(df)
        return df  # Return the DataFrame for caching

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache
def get_pyg_html(df: pd.DataFrame) -> str:
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    # If you want to use feature of saving chart config, set `debug=True`
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html

# Main function to run the app
def main():
    df = upload_csv()  # Call the upload_csv function to get the DataFrame
    if df is not None:
        html_content = get_pyg_html(df)  # Get the PygWalker HTML content
        # Render the HTML content using components.html
        components.html(html_content, width=1300, height=1000, scrolling=True)

if __name__ == "__main__":
    main()
