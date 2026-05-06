import streamlit as st
import qrvode
from PIL import image
# page title
st.title("qr code generator")
data=st.text_input("enter url")
if st.button("generate qr"):
  if data:
    qr=qrcode.make(data)
    qr.save("qr.png")
    img=image.open("qr.png")
    st.iamge(img,caption="generated qr code")
  with open("qr.png","rb")as f:
    st.download_button("download qr",f,file_name=="qr.png")
else:
  st.warning("please enter some text")
