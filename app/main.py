import streamlit as st
import os
from classifier import classify_image_topic

# Set the the header for website
st.set_page_config(page_title="Gemini Chatbot - AP Calculus BC", layout="centered")
# Set the title
st.title("📘 Phân Loại Chủ Đề Bài Toán AP Calculus BC ")

# Save the image into 'data' folder to handle the uploaded image
uploaded_image = st.file_uploader("📤 Upload ảnh bài toán", type=["png", "jpg", "jpeg"])

# Check if the image is uploaded
if uploaded_image is not None:
    # Save the uploaded image to a temporary path
    temp_path = os.path.join("data", uploaded_image.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_image.read())
    # Display the the the process of uploading
    with st.spinner("🧠 Đang gửi ảnh đến Gemini..."):
        result = classify_image_topic(temp_path)

    # Result
    st.subheader("📚 Kết quả phân loại:")
    st.success(result)
