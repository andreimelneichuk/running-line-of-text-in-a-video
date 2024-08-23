import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_video_with_text(text="Hello world", font_path="PionerSans8-VF.ttf"):
    width, height = 100, 100
    duration = 3  # длительность видео в секундах
    fps = 24  # кадров в секунду
    out = cv2.VideoWriter("video_text.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    font_size = 50 
    font = ImageFont.truetype(font_path, font_size)

    text_width = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font)[2]
    total_frames = duration * fps
    speed = (text_width + width) / total_frames

    for i in range(total_frames):
        frame = np.full((height, width, 3), (0,0,255) ,dtype=np.uint8)

        x = int(width - i * speed)
        y = height // 2

        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y), text, font=font, fill=(255, 255, 255))
        frame = np.array(img_pil)

        out.write(frame)

    out.release()
    print("Done")

text = "Привет мир"
create_video_with_text(text)
