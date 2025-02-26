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
| **Category** | **Prompt** | **Preview** |
|-------------|-----------|------------|
| **General Product Photography** | 📷 **"Create a high-resolution, professional studio photo of a pair of sneakers, placed on a clean, minimalistic background. The lighting should be soft and diffused, highlighting textures and materials. Capture multiple angles for a complete product showcase."** | ![Sneakers](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img0.png) |
| **E-Commerce Product Listing** | 🛒 **"Generate a set of product images for an e-commerce listing of a smartwatch. Include front, back, and side views with a plain white background, even lighting, and realistic shadows."** | ![Smartwatch](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img1.png) |
| **Luxury & Premium Product Shots** | 💎 **"Studio-quality image of a luxury wristwatch on a black satin background with dramatic lighting. Highlight fine details such as textures, engravings, or embellishments to create a high-end look."** | ![Luxury Watch](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img2.png) |
| **Lifestyle Product Photography** | 🏡 **"Generate an aesthetic lifestyle shot of a designer handbag being used in a modern home setting. Ensure natural lighting, warm tones, and a cozy, inviting atmosphere."** | ![Handbag](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img3.png) |
| **360-Degree View for Interactive Display** | 🔄 **"Generate a seamless 360-degree product photography series for a high-end DSLR camera. Capture multiple angles with consistent lighting and high clarity for an interactive shopping experience."** | ![DSLR Camera](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img4.png) |
| **Minimalist Product Showcase** | ⚪ **"Create a clean, high-quality product image of a wireless earbud case placed on a neutral, gradient background. Emphasize simplicity and elegance, with soft shadows and studio lighting."** | ![Earbuds](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img5.png) |
| **Outdoor & Adventure Products** | 🌿 **"Capture a rugged outdoor product shot of a hiking backpack in a natural setting. Highlight durability and real-world use with earthy tones, dynamic lighting, and a scenic backdrop."** | ![Backpack](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img6.png) |

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
