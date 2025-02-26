# 🎨 Vertex AI Imagen 3 - AI Image Generation in Google Colab 🚀

Generate **stunning AI images** directly in **Google Colab** using **Google Cloud's Vertex AI** with `Imagen 3.0`! 🖼️✨  

## 📌 Setup Instructions  

### 1️⃣ Authenticate Google Cloud  
```python
from google.colab import auth
auth.authenticate_user()

import google.auth
credentials, project = google.auth.default()
print(f"Authenticated to project: {project}")

import vertexai
from vertexai.vision_models import ImageGenerationModel

vertexai.init(project="your-project-id", location="us-central1")
generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

images = generation_model.generate_images(
    prompt="A futuristic cityscape at night",
    number_of_images=1,  
    aspect_ratio="1:1",
    add_watermark=True,
)

import IPython.display
from PIL import ImageOps as PIL_ImageOps

def display_image(image, max_width: int = 600, max_height: int = 350):
    pil_image = image._pil_image  
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    image_width, image_height = pil_image.size
    if max_width < image_width or max_height < image_height:
        pil_image = PIL_ImageOps.contain(pil_image, (max_width, max_height))
    IPython.display.display(pil_image)

display_image(images[0])

📌 Google Colab Notebook 📓
Run this project in Google Colab:
🔗 Colab Notebook
