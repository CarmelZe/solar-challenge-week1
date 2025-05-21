import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

# Configure page
st.set_page_config(
    page_title="Solar Potential Dashboard",
    layout="wide",
    page_icon="🌞"
)

# Title
st.title("MoonLight Energy Solutions - Solar Potential Analysis")

# Sidebar controls
st.sidebar.header("Data Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

try:
    # Load data with error handling
    df = load_data(selected_countries)
    
    # Metrics overview
    st.header("Key Solar Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average GHI", f"{df['GHI'].mean():.1f} W/m²")
    col2.metric("Average DNI", f"{df['DNI'].mean():.1f} W/m²")
    col3.metric("Countries Loaded", len(selected_countries))

    # Interactive visualization
    st.header("Solar Radiation Comparison")
    metric = st.selectbox(
        "Select Metric",
        options=['GHI', 'DNI', 'DHI'],
        index=0
    )
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Country', y=metric, palette='viridis')
    plt.title(f"{metric} Distribution by Country")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Raw data preview
    st.header("Data Preview")
    st.dataframe(df.head(), hide_index=True)

except FileNotFoundError as e:
    st.error(f"Data loading failed: {str(e)}")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")