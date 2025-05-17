import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Vision model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to classify image topic
def classify_image_topic(image_path):
    # Open the image with PIL
    image = Image.open(image_path)

    #Prompting the model
    prompt = """
Bạn là một trợ lý học tập chuyên về AP Calculus BC.
Hãy nhìn vào hình ảnh bài toán và xác định bài này thuộc **chủ đề chính nào** trong chương trình AP Calculus BC.
Chỉ trả lời một dòng:

- Chủ đề chính: ...
    """

    #Result
    response = model.generate_content([prompt, image])
    return response.text.strip()
