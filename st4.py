import streamlit as st
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the directories containing your PNG images for each page
image_folder_page1 = "C:\\Users\\35569\\Documents\\Developments\\St\\images1"
image_folder_page2 = "C:\\Users\\35569\\Documents\\Developments\\St\\images2"
image_folder_page3 = "C:\\Users\\35569\\Documents\\Developments\\St\\images3"

def main():
    st.title("Imazhet & Paraqitjet Grafikore")
import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard')    
    # Create a sidebar for navigation
st.sidebar.title("Paneli ballor")
# Sidebar page selection

page = st.sidebar.radio("Select Page", ["Reshjet","Temperaturat","Zjarret"])
if page == "Reshjet":
    # Faqja Reshjet
    st.title("Reshjet")
    images_page1 = os.listdir(image_folder_page1)
    images_page1.sort()
    selected_index = st.slider("Select Image", 0, len(images_page1) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page1, images_page1[selected_index])), caption=f"Image {selected_index}", use_column_width=True)
    # time_hist_color = st.sidebar.selectbox('Zgjidhni qytetin:', ('Burrel', 'Belsh', 'Berat', 'Cërrik', 'Devoll', 'Dibër', 'Divjakë', 'Dropull', 'Elbasan', 'Fier', 'Finiq', 'Fushë-Arrëz', 'Gjirokastër', 'Gramsh', 'Has', 'Himarë', 'Kamëz', 'Kavajë', 'Këlcyrë', 'Klos', 'Kolonjë', 'Konispol', 'Korçë', 'Krujë', 'Kuçovë', 'Kukës', 'Kurbin', 'Lezhë', 'Libohovë', 'Librazhd', 'Lushnjë', 'Malësi e Madhe', 'Maliq', 'Mallakastër', 'Mat', 'Memaliaj', 'Mirditë', 'Patos', 'Peqin', 'Përmet', 'Pogradec', 'Poliçan', 'Prrenjas', 'Pustec', 'Roskovec', 'Rrogozhinë', 'Sarandë', 'Selenicë', 'Shijak', 'Shkodër', 'Skrapar', 'Tepelenë', 'Tropojë', 'Ura Vajgurore', 'Bulqize', 'Tiranë', 'Durrës', 'Vau i Dejës', 'Vlorë', 'Vorë')) 

if page == "Temperaturat":
    # Faqja Temperaturat
    st.title("Temperaturat")
    images_page2 = os.listdir(image_folder_page2)
    images_page2.sort()
    selected_index = st.slider("Select Image", 0, len(images_page2) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page1, images_page2[selected_index])), caption=f"Image {selected_index}", use_column_width=True)
 
else:
    # Faqja Zjarret
    st.title("Zjarret")
    images_page3 = os.listdir(image_folder_page3)
    images_page3.sort()
    selected_index = st.slider("Select Image", 0, len(images_page3) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page3, images_page3[selected_index])), caption=f"Image {selected_index}", use_column_width=True)
st.sidebar.markdown('''
---
Designed by Institute of GeoSciences, Tiranë
''')

# Path to the directory containing your PNG images
image_folder = "C:\\Users\\35569\\Documents\\Developments\\St\\images1"
images = os.listdir(image_folder)
images.sort()  # Ensure images are in the correct order

# Title
st.title("Dashboard - Precipitation and Images")

# Initialize the selected image index
selected_index_images = 0

# Images section with arrow buttons
st.header("Images with Navigation")

# Navigation buttons with arrows
col1, col2, col3, col4, col5 = st.columns(5)
if col2.button("←", key="prev_image", disabled=selected_index_images == 0):
    selected_index_images -= 1
if col4.button("→", key="next_image", disabled=selected_index_images == len(images) - 1):
    selected_index_images += 1

# Display the selected image
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Chart section for the selected city
st.header("Chart - Precipitation")
st.write("Select a city:")

# Dropdown list of cities
cities = ["Bulqize","Durres","Tirane"]  # Add more cities as needed
selected_city = st.selectbox("Select City", cities)

# Load CSV data for the selected city
csv_file_path = f"C:\\Users\\35569\\Documents\\Developments\\St\\csv1/{selected_city.lower().replace(' ', '_')}.csv"
csv_data = pd.read_csv(csv_file_path)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(csv_data['Date'], csv_data['Precipitation'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Precipitation")
ax.set_title(f"Precipitation Data for {selected_city}")
st.pyplot(fig)
