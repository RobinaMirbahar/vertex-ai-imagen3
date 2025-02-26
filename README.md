# 🎨 AI-Powered Studio-Quality Product Photos with Vertex AI Imagen 3

🔗 **Try it in Colab:** [Google Colab Notebook](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4#scrollTo=Kex2ltfOg68z&uniqifier=2)  
📂 **GitHub File:** [image_generation.py](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/image_generation.py)  

# Vertex AI Imagen 3 - Image Generation

## 🚀 Overview  
Generate professional product images using **Google Vertex AI Imagen 3** to create studio-quality visuals from text prompts. 🖼️✨  

You can generate high-resolution AI-powered photos of **[specify product, e.g., sneakers, jewelry, clothing]**, showcasing them from multiple angles while highlighting key details like **[materials, textures, branding, lighting, etc.]**. 🎨🔍  



### ⚙️ Clone the repository and install dependencies:  
```bash
git clone https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab.git
cd vertex-ai-imagen3-colab
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### 🎯 Key Features
✅ **1024x1024 Resolution** - Studio-quality output  
✅ **Multi-angle Generation** - Show products from different views  
✅ **Colab Integration** - Cloud-based execution  
✅ **Commercial Ready** - Watermark-free options  

## 🔗 Quick Start  

🚀 Run the notebook instantly in Google Colab:  

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4)  

📂 View the source code on GitHub:  
[**image_generation.py**](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/image_generation.py)  


   
## 🔧 Installation & Setup

 ### 📋 Prerequisites
- Google Cloud account with [billing enabled](https://console.cloud.google.com/)
- [Vertex AI API enabled](https://console.cloud.google.com/vertex-ai)
- IAM permissions: `Vertex AI User` role



### 🔐 Authentication
```python
from google.colab import auth
auth.authenticate_user()

import vertexai
vertexai.init(project="YOUR-PROJECT-ID", location="us-central1")
```

### 📸 Image Generation
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

## 📊 Example Outputs
| Prompt | Preview |
|--------|---------|
| "Premium coffee machine on marble countertop, steam rising" | ![Coffee Machine](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img0.png)
| "Designer sunglasses on beach towel with ocean background" | ![Sunglasses](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img1.png)) |
| "Generate high-resolution, professional product photos of sneakers, showcasing them from multiple angles and highlighting details like stitching, texture, and sole design" | ![Sunglasses](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img03.png)) |

## 🎚️ Advanced Configuration
```python
# Customized generation with negative prompts
response = generator.generate_images(
    prompt="Modern office chair with leather upholstery",
    number_of_images=3,
    negative_prompt="low quality, blurry, distorted, watermark",
    aspect_ratio="16:9",
    guidance_scale=20,
    temperature=0.7,
    person_generation="avoid"
)
```


## 🚨 Troubleshooting Guide

### Common Errors & Solutions
| Error | Solution |
|-------|----------|
| `PermissionDenied: 403` | Verify IAM roles & enable Vertex AI API |
| `InvalidModelName: 404` | Check model name spelling & regional availability |
| `InvalidAspectRatio` | Use supported ratios: 1:1, 4:3, or 16:9 |

## Maintenance Commands
# Update SDK components
pip install --upgrade google-cloud-aiplatform

# Enable required services
gcloud services enable aiplatform.googleapis.com

## 📚 Documentation Resources  

- [📖 Imagen 3 Technical Docs](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview)  
- [🐍 Python SDK Reference](https://googleapis.dev/python/aiplatform/latest/vertexai.html)  
- [📝 Prompt Engineering Guide](https://cloud.google.com/vertex-ai/docs/generative-ai/image/prompting)  
- [🔒 Safety Filter Settings](https://cloud.google.com/vertex-ai/docs/generative-ai/image/safety)  

## 🤝 Contributing  

We welcome contributions! Follow these steps to contribute:  

1. **Fork the repository** 🔄  
2. **Clone your fork**  
   ```bash
   git clone https://github.com/your-username/vertex-ai-imagen3-colab.git
   cd vertex-ai-imagen3-colab


## 🙌 Thank You!  

If you find this project helpful, feel free to ⭐ star the repository and 🔄 fork it to explore more!  

Happy coding! 🚀  
## ⚠️ Disclaimer  

Generated images must comply with [Google's Generative AI Prohibited Use Policy](https://cloud.google.com/terms/service-terms#19-google-generative-ai). Ensure responsible and ethical use of AI-generated content. 🚀  
