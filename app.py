import streamlit as st
import qrcode
from PIL import Image
# page title
st.title("qr code generator")
data=st.text_input("enter url")
if st.button("generate qr"):
  if data:
    qr=qrcode.make(data)
    qr.save("qr.png")
    img=Image.open("qr.png")
    st.iamge(img,caption="Generated Qr code")
  with open("qr.png","rb")as f:
    st.download_button("Download Qr",f,file_name="qr.png")
else:
  st.warning("please enter some text")
