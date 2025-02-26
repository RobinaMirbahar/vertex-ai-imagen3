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
