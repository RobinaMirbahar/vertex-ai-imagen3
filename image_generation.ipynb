from google.colab import auth
import google.auth
import typing
import IPython.display
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps
import vertexai
from vertexai.vision_models import ImageGenerationModel  

def authenticate():
    """Authenticate the user in Google Colab."""
    auth.authenticate_user()
    credentials, project = google.auth.default()
    print(f"Authenticated to project: {project}")

def display_image(image, max_width: int = 600, max_height: int = 350) -> None:
    """Display an image with a max size limitation."""
    pil_image = image._pil_image  # Access PIL Image object
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    image_width, image_height = pil_image.size
    if max_width < image_width or max_height < image_height:
        pil_image = PIL_ImageOps.contain(pil_image, (max_width, max_height))
    IPython.display.display(pil_image)

def generate_image(prompt: str, number_of_images: int = 1, aspect_ratio: str = "1:1", add_watermark: bool = True):
    """Generate images using Vertex AI's Image Generation Model."""
    vertexai.init(project="your-google-cloud-project", location="us-central1")
    generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = generation_model.generate_images(
        prompt=prompt,
        number_of_images=number_of_images,  
        aspect_ratio=aspect_ratio,
        add_watermark=add_watermark,
    )
    return images

if __name__ == "__main__":
    authenticate()
    prompt = "A futuristic cityscape at night"
    images = generate_image(prompt)
    display_image(images[0])
