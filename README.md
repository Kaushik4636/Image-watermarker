# Image Watermarker

A simple Python project to add **text watermarks** to images. This project uses the **Pillow (PIL)** library to open, edit, and save images with a watermark.

---

## Features

- Add a text watermark to any image.
- Watermark uses the **Roboto** font for a clean, professional look.
- Saves a new watermarked image without modifying the original.

---

## Folder Structure

image-watermarker/
├── watermark.py # Python script to add watermark
├── roboto/ # Folder containing the Roboto font
│ └── Roboto-Regular.ttf
└── images/ # Folder for images
└── input.jpg # Image to watermark
└── output.jpg # Watermarked image (generated)

yaml
Copy code

---

## Requirements

- Python 3.x
- Pillow library

Install Pillow using:

```bash
pip install pillow
How to Use
Place the image you want to watermark in the images folder and name it input.jpg.

Ensure the font Roboto-Regular.ttf is in the roboto folder.

Open the project folder in VS Code.

Open the terminal in VS Code.

Run the script:

bash
Copy code
python watermark.py
The watermarked image will be saved as images/output.jpg.

Customization
To change the watermark text, edit this line in watermark.py:

python
Copy code
"© Kaushik Madhavan"
You can also adjust the font size, opacity, or position in the script if needed.

Notes
Always keep a backup of your original images.

Make sure your terminal is in the project folder when running the script.

The watermark is applied to the bottom-right corner by default.
