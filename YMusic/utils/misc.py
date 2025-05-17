modules_help = {}  # Dictionary to store help info for modules
prefix = "."       # Default command prefix

def resize_image(image_path):
    """Basic image resizing function"""
    from PIL import Image
    img = Image.open(image_path)
    img.thumbnail((320, 320))
    return img
