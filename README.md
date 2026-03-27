# 🎨 AI-Powered Studio-Quality Product Photos with Vertex AI Imagen 3

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4)
[![GitHub Stars](https://img.shields.io/github/stars/RobinaMirbahar/vertex-ai-imagen3-colab?style=social)](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/stargazers)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Vertex AI](https://img.shields.io/badge/Google-Vertex%20AI-4285F4?logo=google-cloud)](https://cloud.google.com/vertex-ai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)


🔗 **Try it in Colab:** [Google Colab Notebook](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4#scrollTo=Kex2ltfOg68z&uniqifier=2)
📂 **Source Code:** [image_generation.py](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/image_generation.py)

---

## 📖 Overview

Generate **professional, studio-quality product images** using **Google Vertex AI Imagen 3** — entirely from text prompts. Whether you're building an e-commerce store, a marketing campaign, or a product catalog, this tool lets you produce high-resolution AI-powered visuals at scale.

You can generate images of **any product** (sneakers, jewelry, clothing, electronics, and more), showcasing them from multiple angles while highlighting key details like **materials, textures, branding, and lighting**.

---

## ✨ Key Features

| Feature | Details |
|--------|---------|
| 🖼️ **High Resolution** | 1024×1024 studio-quality output |
| 🔄 **Multi-angle Generation** | Show products from different views |
| ☁️ **Colab Integration** | Cloud-based, no local GPU needed |
| 🚫 **Watermark-Free** | Commercial-ready images |
| 🎚️ **Advanced Controls** | Guidance scale, temperature, negative prompts |
| 🛡️ **Safety Filters** | Configurable content safety settings |

---

## 🚀 Quick Start

Run the notebook instantly in Google Colab — no setup required:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13dpz6jw5rPNVOj-JgLWG9QuStetGc9Y4)

Or clone and run locally (see [Installation](#-installation--setup) below).

---

## 🔧 Installation & Setup

### 📋 Prerequisites

Before you begin, make sure you have:

- A [Google Cloud account](https://console.cloud.google.com/) with **billing enabled**
- [Vertex AI API enabled](https://console.cloud.google.com/vertex-ai)
- IAM role: **`Vertex AI User`**
- Python **3.8+**

### ⚙️ Clone & Install

```bash
git clone https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab.git
cd vertex-ai-imagen3-colab

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### 🔐 Authentication

#### In Google Colab:
```python
from google.colab import auth
auth.authenticate_user()

import vertexai
vertexai.init(project="YOUR-PROJECT-ID", location="us-central1")
```

#### Locally (Service Account):
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"
```

---

## 📸 Basic Usage

```python
from vertexai.preview import vision_models
from IPython.display import display

# Initialize the model
generator = vision_models.ImageGenerationModel.from_pretrained("imagegeneration-002")

# Generate product images
response = generator.generate_images(
    prompt="Professional studio photo of luxury sneakers, 360 view, 4K resolution",
    number_of_images=4,
    aspect_ratio="1:1",
    guidance_scale=15,
    seed=1234
)

# Display results
for idx, image in enumerate(response.images):
    print(f"Image {idx + 1}")
    display(image._pil_image)
```

---

## 🎚️ Advanced Configuration

Use negative prompts, custom aspect ratios, and fine-tuned parameters for more control:

```python
response = generator.generate_images(
    prompt="Modern office chair with leather upholstery, studio lighting",
    number_of_images=3,
    negative_prompt="low quality, blurry, distorted, watermark, shadow artifacts",
    aspect_ratio="16:9",        # Supported: "1:1", "4:3", "16:9"
    guidance_scale=20,          # Higher = more prompt-adherent (range: 1–30)
    temperature=0.7,            # Controls creativity (range: 0.0–1.0)
    person_generation="avoid"   # Options: "allow", "avoid"
)
```

### ⚙️ Parameter Reference

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | `str` | Text description of the image to generate |
| `number_of_images` | `int` | Number of images to generate (1–8) |
| `negative_prompt` | `str` | Elements to exclude from the image |
| `aspect_ratio` | `str` | Output dimensions: `"1:1"`, `"4:3"`, `"16:9"` |
| `guidance_scale` | `float` | Prompt adherence strength (1–30) |
| `temperature` | `float` | Creativity level (0.0–1.0) |
| `seed` | `int` | Random seed for reproducibility |
| `person_generation` | `str` | Controls human appearance in output |

---

## 📊 Example Outputs & Prompts

| Category | Prompt | Preview |
|----------|--------|---------|
| 📷 **General Product** | `"Professional studio photo of sneakers on a minimalistic background, soft diffused lighting, multiple angles"` | ![Sneakers](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img0.png) |
| 🛒 **E-Commerce Listing** | `"Product images of a smartwatch — front, back, side views, plain white background, even lighting, realistic shadows"` | ![Smartwatch](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img1.png) |
| 💎 **Luxury / Premium** | `"Studio-quality luxury wristwatch on black satin, dramatic lighting, fine textures and engravings highlighted"` | ![Luxury Watch](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img2.png) |
| 🏡 **Lifestyle Shot** | `"Aesthetic lifestyle shot of a designer handbag in a modern home, natural lighting, warm tones, cozy atmosphere"` | ![Handbag](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img3.png) |
| 🔄 **360° View** | `"Seamless 360-degree product series of a high-end DSLR camera, consistent lighting, high clarity for interactive shopping"` | ![DSLR Camera](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img4.png) |
| ⚪ **Minimalist** | `"Clean product image of a wireless earbud case on a neutral gradient background, soft shadows, studio lighting"` | ![Earbuds](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img5.png) |
| 🌿 **Outdoor / Adventure** | `"Rugged outdoor product shot of a hiking backpack in a natural setting, earthy tones, dynamic lighting, scenic backdrop"` | ![Backpack](https://github.com/RobinaMirbahar/vertex-ai-imagen3-colab/blob/main/Images/img6.png) |

---

## 🧠 Prompt Engineering Tips

Writing better prompts leads to significantly better results. Here are some best practices:

- **Be specific about lighting:** `"soft diffused lighting"`, `"dramatic side lighting"`, `"golden hour sunlight"`
- **Specify background:** `"plain white background"`, `"black satin surface"`, `"blurred outdoor setting"`
- **Include view angles:** `"front view"`, `"360-degree view"`, `"top-down flat lay"`
- **Add quality modifiers:** `"4K resolution"`, `"ultra-realistic"`, `"studio quality"`, `"sharp focus"`
- **Use negative prompts** to exclude unwanted artifacts: `"no watermark, no blurring, no distortion"`

📖 See the full [Prompt Engineering Guide](https://cloud.google.com/vertex-ai/docs/generative-ai/image/prompting) for more.

---

## 🚨 Troubleshooting

### Common Errors & Fixes

| Error | Cause | Solution |
|-------|-------|----------|
| `PermissionDenied: 403` | Missing IAM permissions | Verify `Vertex AI User` role is assigned |
| `InvalidModelName: 404` | Wrong model name or region | Check spelling & regional availability |
| `InvalidAspectRatio` | Unsupported ratio used | Use `"1:1"`, `"4:3"`, or `"16:9"` only |
| `QuotaExceeded` | API quota limit hit | Request quota increase in Cloud Console |
| `BillingNotEnabled` | GCP billing inactive | Enable billing at [console.cloud.google.com](https://console.cloud.google.com/) |

### Maintenance Commands

```bash
# Update the Vertex AI SDK
pip install --upgrade google-cloud-aiplatform

# Enable required GCP services
gcloud services enable aiplatform.googleapis.com

# Verify authentication
gcloud auth application-default print-access-token
```

---

## 📁 Project Structure

```
vertex-ai-imagen3-colab/
├── image_generation.py       # Core image generation script
├── requirements.txt          # Python dependencies
├── Images/                   # Sample output images
│   ├── img0.png              # Sneakers example
│   ├── img1.png              # Smartwatch example
│   └── ...
└── README.md                 # This file
```

---

## 📚 Documentation & Resources

| Resource | Link |
|----------|------|
| 📖 Imagen 3 Technical Docs | [cloud.google.com/vertex-ai/docs](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) |
| 🐍 Python SDK Reference | [googleapis.dev/python/aiplatform](https://googleapis.dev/python/aiplatform/latest/vertexai.html) |
| 📝 Prompt Engineering Guide | [Image Prompting Best Practices](https://cloud.google.com/vertex-ai/docs/generative-ai/image/prompting) |
| 🔒 Safety Filter Settings | [Content Safety Docs](https://cloud.google.com/vertex-ai/docs/generative-ai/image/safety) |
| 💰 Pricing | [Vertex AI Pricing](https://cloud.google.com/vertex-ai/pricing) |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository 🔄
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/vertex-ai-imagen3-colab.git
   cd vertex-ai-imagen3-colab
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit** your changes:
   ```bash
   git commit -m "Add: description of your change"
   ```
5. **Push** and open a **Pull Request** 🚀

Please follow existing code style and include comments where appropriate.

---

## 📄 License

This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

All generated images must comply with [Google's Generative AI Prohibited Use Policy](https://cloud.google.com/terms/service-terms#19-google-generative-ai). Please ensure responsible and ethical use of AI-generated content.

---

## 🙌 Acknowledgements

Built with ❤️ using [Google Vertex AI Imagen 3](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview).

If you find this project helpful:
- ⭐ **Star** the repository
- 🔄 **Fork** it to build your own version
- 📣 **Share** it with others who might benefit

Happy generating! 🚀
