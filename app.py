import streamlit as st
from image_classification import classification
from PIL import Image, ImageOps

st.title("Brain Tumor Detection")
st.header("Brain Tumor MRI Classification")
st.text("Upload a brain MRI Image to Detect brain tumors")

uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = classification(image, '/home/mayowa/Documents/streamlit_brain_tumour/brain_tumor_classification.h5')
    if label == 0:
        st.write("The MRI scan has a brain tumor")
    else:
        st.write("The MRI scan is healthy")