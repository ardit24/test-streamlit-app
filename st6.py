import streamlit as st
import pandas as pd
from PIL import Image
import os
import altair as alt

# Define folder paths for images and CSVs for each page
page_data = {
    "Page 1": {
        "image_folder": "C:\\Users\\35569\\Documents\\Developments\\St\\images1",
        "csv_folder": "C:\\Users\\35569\\Documents\\Developments\\St\\csv1"
    },
    "Page 2": {
        "image_folder": "C:\\Users\\35569\\Documents\\Developments\\St\\images2",
        "csv_folder": "C:\\Users\\35569\\Documents\\Developments\\St\\csv2"
    }
}

# Sidebar with radio buttons for selecting pages
selected_page = st.sidebar.radio("Select Page", list(page_data.keys()))

# Page content based on selected page
st.title(f"{selected_page} - Dashboard")

# Load and display image based on selected page
image_folder = page_data[selected_page]["image_folder"]
images = os.listdir(image_folder)
images.sort()
selected_index_images = st.slider("Select Image", 0, len(images) - 1, 0)
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Add a description below the image
image_description = {
    "Page 1": "Description for Image on Page 1.",
    "Page 2": "Description for Image on Page 2."
}
st.write(image_description[selected_page])

# Chart section for the selected city
st.header(f"Chart - Precipitation ({selected_page})")
st.write("Select a city:")

# Dropdown list of cities
cities = ["City 1", "City 2", "City 3"]  # Add more cities as needed
selected_city = st.selectbox("Select City", cities)

# Load CSV data for the selected city and page
csv_folder = page_data[selected_page]["csv_folder"]
csv_file_path = os.path.join(csv_folder, f"{selected_city.lower().replace(' ', '_')}.csv")
csv_data = pd.read_csv(csv_file_path, parse_dates=['Date'], dayfirst=True)

# Create a bar chart using Altair
thresholds = [10, 20, 30]  # Add your threshold values here

color_condition = alt.condition(
    alt.datum.Precipitation > thresholds[-1], alt.value('red'),
    alt.condition(alt.datum.Precipitation > thresholds[-2], alt.value('yellow'), alt.value('green'))
)

chart = alt.Chart(csv_data).mark_bar().encode(
    x=alt.X('Date:T', title='Date'),
    y=alt.Y('Precipitation:Q', title='Precipitation'),
    color=color_condition,
    tooltip=[alt.Tooltip('Date:T', title='Date'), alt.Tooltip('Precipitation:Q', title='Precipitation')]
).properties(
    width=800,  # Increase chart width
    height=400,
    title=f"Precipitation Data for {selected_city}"
).configure_axis(
    labelFontSize=12,  # Increase font size of axis labels
    titleFontSize=14  # Increase font size of axis titles
).configure_mark(
    opacity=0.7  # Adjust bar opacity
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)

# Add legend for the color scale
st.write("Legend:")
st.markdown("Red: Above Highest Threshold | Yellow: Above Middle Threshold | Green: Below Middle Threshold")

# Add a description below the chart
chart_description = {
    "Page 1": "Description for Chart on Page 1.",
    "Page 2": "Description for Chart on Page 2."
}
st.write(chart_description[selected_page])

# Add a custom footer aligned to the right side of the sidebar
st.sidebar.markdown(
    "<p style='text-align: right;'>Made with Streamlit by Alban Doko (a.doko@igeo.edu.al)</p>",
    unsafe_allow_html=True
)
