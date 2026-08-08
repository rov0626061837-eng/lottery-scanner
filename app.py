import google.genai as genai
from PIL import Image
import streamlit as st

st.title("สแกนตัวเลขลอตเตอรี่ด้วย AI")

# ช่องใส่ API Key บนหน้าแอป
api_key = st.text_input("กรอก Google Gemini API Key", type="password")

uploaded_file = st.file_uploader(
    "เลือกรูปภาพลอตเตอรี่", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="รูปภาพที่อัปโหลด", use_container_width=True)
    
    if st.button("เริ่มอ่านเลขลอตเตอรี่"):
        with st.spinner("กำลังประมวลผล..."):
            try:
                # ตั้งค่า Client ด้วยแพ็กเกจ google-genai ใหม่
                client = genai.Client(api_key=api_key)
                
                # ส่งคำสั่งประมวลผลรูปภาพด้วยรุ่น gemini-2.5-flash
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        image,
                        "จงอ่านภาพลอตเตอรี่นี้ และดึงเฉพาะตัวเลข 6 ตัวตรงกลางออกมาเป็นข้อความตรงๆ เท่านั้น ห้ามมีข้อความอื่น"
                    ]
                )
                
                st.success("อ่านสำเร็จ!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
