import pytest
from PIL import Image
from .core import resize

def test_resize():
    img = Image.new("RGB", (400, 200))
    img.save("test_image.png")

    result = resize("test_image.png", 200)
    assert result.size == (200, 100)