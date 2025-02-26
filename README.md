🎨 AI-Powered Studio-Quality Product Photos with Vertex AI Imagen 3

📌 Overview
This project leverages Google Vertex AI Imagen 3 to generate studio-quality product images from text prompts. You can create high-resolution AI-generated photos of [specify product, e.g., sneakers, jewelry, clothing], showcasing them from multiple angles while emphasizing key details like [materials, textures, branding, lighting, etc.].

🎯 Key Features
✅ Studio-Quality AI Images – Generate high-resolution, photorealistic product images
✅ Customizable Prompts – Define specific angles, lighting, and product details
✅ Google Colab Integration – Run the notebook easily with no local setup required
✅ Powered by Vertex AI Imagen 3 – Uses Google's latest Imagen 3 model for stunning AI-generated images

🔗 Live Demo
🚀 Try it now on Google Colab: Click Here
## 📌 Setup Instructions  

🛠 Setup & Installation
Follow these steps to run the project:

1️⃣ Prerequisites
✔ A Google Cloud account with Vertex AI enabled
✔ Google Colab for running the Jupyter notebook
✔ IAM permissions for Vertex AI API

2️⃣ Authentication in Google Colab
✔ Open the Google Colab notebook here.
✔ Run the first cell to authenticate your Google Cloud account:

from google.colab import auth
auth.authenticate_user()

✔ Initialize Vertex AI with your project details:
import vertexai
vertexai.init(project="your-project-id", location="us-central1")

3️⃣ Run the Notebook to Generate Images
✔ Load the Imagen 3 model:
from vertexai.vision_models import ImageGenerationModel  
generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

✔ Provide a text prompt and generate the image:
images = generation_model.generate_images(
    prompt="Generate high-resolution, professional product photos of sneakers, showcasing them from multiple angles and highlighting details like stitching, texture, and sole design",
    number_of_images=1,
    aspect_ratio="1:1",
    add_watermark=True
)

✔ Display the generated image:
from PIL import ImageOps as PIL_ImageOps
import IPython.display  

def display_image(image, max_width: int = 600, max_height: int = 350) -> None:
    pil_image = image._pil_image  
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    pil_image = PIL_ImageOps.contain(pil_image, (max_width, max_height))
    IPython.display.display(pil_image)

display_image(images[0])
✔ Customize the Prompt – Modify the prompt field to generate images of different products!

🖼 Example AI-Generated Images
Prompt	Output
"A futuristic smartwatch on a wooden table, soft lighting"	🖼 View Image
"A sleek, modern electric car in a showroom"	🖼 View Image
"A designer handbag with floral patterns on a white background"	🖼 View Image
🚀 Customization
🔹 Modify the Prompt – Describe your product, lighting, and scene
🔹 Change Image Size & Aspect Ratio – Adjust settings like "aspect_ratio": "16:9"
🔹 Generate Multiple Images – Increase number_of_images=3

💡 Use Cases
✅ E-Commerce & Product Listings – Generate professional photos without a photoshoot
✅ Marketing & Ads – Create eye-catching promotional images
✅ Prototyping & Concept Art – Visualize product designs before production

📜 Official Google Documentation
📖 Vertex AI Overview: Vertex AI Documentation
📖 Vertex AI Model Garden: Model Garden Docs
📖 Imagen 3 Model API: Imagen Model Documentation
📖 Google Colab Guide: Colab Documentation
📖 Google Cloud Authentication: Google Auth Docs
