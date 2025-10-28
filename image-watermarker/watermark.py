from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(input_path, output_path, text, font_path, opacity=0.5, margin=(10,10)):
    img = Image.open(input_path).convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)
    font = ImageFont.truetype(font_path, size= int(img.size[1] / 20))
    text_size = draw.textsize(text, font=font)
    position = (img.size[0] - text_size[0] - margin[0], img.size[1] - text_size[1] - margin[1])
    draw.text(position, text, fill=(255,255,255,int(255*opacity)), font=font)
    watermarked = Image.alpha_composite(img, txt_layer)
    watermarked.convert("RGB").save(output_path, "JPEG")

# Example usage
add_text_watermark("images/input.jpg", "images/output.jpg", "© MyWatermark", "arial.ttf")
