import streamlit as st
from PIL import Image
import pandas as pd
import plost
import os



# Path to the directories containing your PNG images for each page
image_folder_page1 = "C:\\Users\\35569\\Documents\\Developments\\St\\images1"
image_folder_page2 = "C:\\Users\\35569\\Documents\\Developments\\St\\images2"

def main():
    st.title("Imazhet & Paraqitjet Grafikore")
import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard')    
    # Create a sidebar for navigation
st.sidebar.title("Paneli ballor")
# Sidebar page selection
page = st.sidebar.radio("Select Page", ["Page 1", "Page 2"])

if page == "Page 1":
    # Page 1 content
    st.title("Page 1")
    images_page1 = os.listdir(image_folder_page1)
    images_page1.sort()
    selected_index = st.slider("Select Image", 0, len(images_page1) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page1, images_page1[selected_index])), caption=f"Image {selected_index}", use_column_width=True)
    time_hist_color = st.sidebar.selectbox('Zgjidhni qytetin:', ('Burrel', 'Belsh', 'Berat', 'Cërrik', 'Devoll', 'Dibër', 'Divjakë', 'Dropull', 'Elbasan', 'Fier', 'Finiq', 'Fushë-Arrëz', 'Gjirokastër', 'Gramsh', 'Has', 'Himarë', 'Kamëz', 'Kavajë', 'Këlcyrë', 'Klos', 'Kolonjë', 'Konispol', 'Korçë', 'Krujë', 'Kuçovë', 'Kukës', 'Kurbin', 'Lezhë', 'Libohovë', 'Librazhd', 'Lushnjë', 'Malësi e Madhe', 'Maliq', 'Mallakastër', 'Mat', 'Memaliaj', 'Mirditë', 'Patos', 'Peqin', 'Përmet', 'Pogradec', 'Poliçan', 'Prrenjas', 'Pustec', 'Roskovec', 'Rrogozhinë', 'Sarandë', 'Selenicë', 'Shijak', 'Shkodër', 'Skrapar', 'Tepelenë', 'Tropojë', 'Ura Vajgurore', 'Bulqize', 'Tiranë', 'Durrës', 'Vau i Dejës', 'Vlorë', 'Vorë')) 

else:
    # Page 2 content
    st.title("Page 2")
    images_page2 = os.listdir(image_folder_page2)
    images_page2.sort()
    selected_index = st.slider("Select Image", 0, len(images_page2) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page2, images_page2[selected_index])), caption=f"Image {selected_index}", use_column_width=True)

st.sidebar.subheader('Bashkitë e Republikës së Shqipërisë')
  
# time_hist_color = st.sidebar.selectbox('Zgjidhni qytetin:', ('Burrel', 'Belsh', 'Berat', 'Cërrik', 'Devoll', 'Dibër', 'Divjakë', 'Dropull', 'Elbasan', 'Fier', 'Finiq', 'Fushë-Arrëz', 'Gjirokastër', 'Gramsh', 'Has', 'Himarë', 'Kamëz', 'Kavajë', 'Këlcyrë', 'Klos', 'Kolonjë', 'Konispol', 'Korçë', 'Krujë', 'Kuçovë', 'Kukës', 'Kurbin', 'Lezhë', 'Libohovë', 'Librazhd', 'Lushnjë', 'Malësi e Madhe', 'Maliq', 'Mallakastër', 'Mat', 'Memaliaj', 'Mirditë', 'Patos', 'Peqin', 'Përmet', 'Pogradec', 'Poliçan', 'Prrenjas', 'Pustec', 'Roskovec', 'Rrogozhinë', 'Sarandë', 'Selenicë', 'Shijak', 'Shkodër', 'Skrapar', 'Tepelenë', 'Tropojë', 'Ura Vajgurore', 'Bulqize', 'Tiranë', 'Durrës', 'Vau i Dejës', 'Vlorë', 'Vorë')) 

st.sidebar.markdown('''
---
Designed by Institute of GeoSciences, Tiranë
''')


# c1, c2 = st.columns((20,3))
# with c1:
#     st.markdown('### Imazhet me TimeSlider')
#     plost.time_hist(
#     data=stocks,
#     date='date',
#     x_unit='week',
#     y_unit='day',
#     color=time_hist_color,
#     aggregate='median',
#     legend=None,
#     height=400,
#     use_container_width=True
#     )
# with c2:
#     st.markdown('### Donut chart')
#     plost.donut_chart(
#         data=stocks,
#         theta=stocks,
#         color='company',
#         legend='bottom', 
#        use_container_width=True)

# Row C
# st.markdown('### Grafiket')
# st.line_chart(stocks, x = 'date', y = plot_data, height = plot_height)
