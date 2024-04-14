from PIL import Image, ImageDraw, ImageFont

def add_watermark_overlay(input_image_path, output_image_path_watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size

    overlay = Image.new('RGBA', input_image.size, (255,255,255,0))