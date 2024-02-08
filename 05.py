import time
import streamlit as st
from PIL import Image
st.title('File Uploading')

#1,Image
st.subheader('1, Uploading an Image')
img_file = st.file_uploader('Upload Image', type = ['png','jpeg','jpg'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))
#2, Audio
st.subheader('1, Uploading an Audio')
img_file = st.file_uploader('Upload Audio', type = ['wav','mp3'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(img_file)
    st.audio(img_file)
#3, Video
st.subheader('1, Uploading an Video')
img_file = st.file_uploader('Upload Video', type = ['mov','mp4'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(img_file)
    st.video(img_file)
#4, csv
st.subheader('1, Uploading an CSV')
img_file = st.file_uploader('Upload DataFrame', type = ['mov','mp4'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(img_file)
    st.dataframe(img_file)
