import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="สแกนหวย", page_icon="🎫", layout="centered")

st.title("🎫 สแกนเลขลอตเตอรี่")
st.write("อัปโหลดรูปหรือถ่ายภาพสลากเพื่อดึงเลข 6 หลัก")

api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    api_key = st.text_input("กรอก Gemini API Key:", type="password")

uploaded_file = st.file_uploader("เลือกรูปภาพสลากลอตเตอรี่", type=["jpg", "jpeg", "png"])

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="รูปที่อัปโหลด", use_column_width=True)
    
    if st.button("🔍 สแกนอ่านตัวเลข"):
        with st.spinner("กำลังอ่านตัวเลข..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = "ให้อ่านหมายเลขลอตเตอรี่ 6 หลักจากภาพ ตอบเฉพาะตัวเลข 6 หลักเท่านั้น หากมีหลายใบให้เว้นวรรคหรือขึ้นบรรทัดใหม่"
                response = model.generate_content([prompt, image])
                
                st.success("อ่านตัวเลขสำเร็จ!")
                st.code(response.text, language="text")
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
