import google.generativeai as genai
from PIL import Image
import streamlit as st

st.title("สแกนตัวเลขลอตเตอรี่ด้วย AI")

# ช่องใส่ API Key บนหน้าแอป
api_key = st.text_input("กรอก Google Gemini API Key ของคุณ:", type="password")

uploaded_file = st.file_uploader(
    "เลือกรูปภาพลอตเตอรี่", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None and api_key:
  image = Image.open(uploaded_file)
  st.image(image, caption="รูปภาพที่อัปโหลด", use_column_width=True)

  if st.button("เริ่มอ่านเลขลอตเตอรี่"):
    with st.spinner("กำลังประมวลผล..."):
      try:
        genai.configure(api_key=api_key)
        # เปลี่ยนมาใช้ gemini-2.5-flash ตามที่คุณต้องการ
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content([
            image,
            "จงอ่านภาพลอตเตอรี่นี้ และดึงเฉพาะตัวเลข 6"
            " ตัวตรงกลางออกมาเป็นข้อความตรงๆ เท่านั้น ไม่อธิบายเพิ่ม",
        ])
        st.success("อ่านสำเร็จ!")
        st.write("### เลขที่อ่านได้:")
        st.write(response.text)
      except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
elif uploaded_file is not None and not api_key:
  st.warning("กรุณากรอก API Key ก่อนกดอ่านภาพ")
