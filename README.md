# 🎨 AI-Powered Studio-Quality Product Photos with Vertex AI Imagen 3

🔗 **Try it in Colab:** [Google Colab Notebook](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4#scrollTo=Kex2ltfOg68z&uniqifier=2)  
📂 **GitHub File:** [image_generation.py](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/image_generation.py)  

# Vertex AI Imagen 3 - Image Generation

## 🚀 Overview  
Generate professional product images using **Google Vertex AI Imagen 3** to create studio-quality visuals from text prompts. 🖼️✨  

You can generate high-resolution AI-powered photos of **[specify product, e.g., sneakers, jewelry, clothing]**, showcasing them from multiple angles while highlighting key details like **[materials, textures, branding, lighting, etc.]**. 🎨🔍  


## 🔧 Installation  

🚀 Clone the repository and install dependencies:  

```bash
git clone https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab.git
cd vertex-ai-imagen3-colab
pip install google-auth google-cloud-aiplatform pillow
```

### 🎯 Key Features
✅ **1024x1024 Resolution** - Studio-quality output  
✅ **Multi-angle Generation** - Show products from different views  
✅ **Colab Integration** - Cloud-based execution  
✅ **Commercial Ready** - Watermark-free options  

## 🔗 Quick Start
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]([[https://colab.research.google.com/github/yourusername/repo/blob/main/notebook.ipynb](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4#scrollTo=Kex2ltfOg68z&uniqifier=2)](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/image_generation.py))

   
## 🛠 Setup Guide

### 1️⃣ Prerequisites
- Google Cloud project with billing enabled
- Vertex AI API activated
- `Vertex AI User` IAM role

### 2️⃣ Authentication
```python
from google.colab import auth
auth.authenticate_user()

import vertexai
vertexai.init(project="YOUR-PROJECT-ID", location="us-central1")
```

### 3️⃣ Generate Images
```python
from vertexai.preview import vision_models
from IPython.display import display

# Initialize model
generator = vision_models.ImageGenerationModel.from_pretrained("imagegeneration-002")

# Create product images
response = generator.generate_images(
    prompt="Professional studio photo of luxury sneakers, 360 view, 4K resolution",
    number_of_images=4,
    aspect_ratio="1:1",
    guidance_scale=15,
    seed=1234
)

# Display results
for idx, image in enumerate(response.images):
    print(f"Image {idx+1}")
    display(image._pil_image)
```

## 🖼 Example Outputs
| Prompt | Preview |
|--------|---------|
| "Premium coffee machine on marble countertop, steam rising" | ![Coffee Machine](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img0.png)
| "Designer sunglasses on beach towel with ocean background" | ![Sunglasses](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img1.png)) |
| "Generate high-resolution, professional product photos of sneakers, showcasing them from multiple angles and highlighting details like stitching, texture, and sole design" | ![Sunglasses](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img03.png)) |

## ⚙️ Customization
```python
# Advanced generation with negative prompts
response = generator.generate_images(
    prompt="Modern office chair with leather upholstery",
    number_of_images=3,
    negative_prompt="low quality, blurry, distorted",
    aspect_ratio="16:9",
    guidance_scale=20
)
```

## 📚 Documentation
- [Imagen 3 Technical Guide](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview)
- [Vertex AI Python SDK](https://googleapis.dev/python/aiplatform/latest/vertexai.html)
- [Colab Notebook Help](https://colab.research.google.com/notebooks/intro.ipynb)

## ⚠️ Troubleshooting
**Common Issues:**
- `Permission Denied`: Verify IAM roles
- `Model Not Found`: Check model name spelling
- `Invalid Aspect Ratio`: Use supported ratios (1:1, 4:3, 16:9)
  
 ## Common fixes
    pip install --upgrade google-cloud-aiplatform
    gcloud services enable aiplatform.googleapis.com

```bash
# Update SDK if errors persist
pip install --upgrade google-cloud-aiplatform
```
## 🙌 Thank You!  

If you find this project helpful, feel free to ⭐ star the repository and 🔄 fork it to explore more!  

Happy coding! 🚀  

