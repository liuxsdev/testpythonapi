from fastapi import FastAPI
from fastapi.responses import Response
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from os import join
app = FastAPI()


def gen_png(x,y,z):
    size=(256,256)
    font_color = (156,220,255,255)
    font_size = 40
    im = Image.new("RGBA",size,(255, 255, 255,0))
    font = ImageFont.truetype(join("api","CascadiaMono.ttf"), font_size)
    draw = ImageDraw.Draw(im)
    draw.text((256/2, 256/2), "x={}\ny={}\nz={}".format(x,y,z),font=font,anchor="mm",fill=font_color)
    draw.rectangle([1,1,255,255],outline=(0, 0, 0, 255))
    return im

@app.get("/api/tile")
async def maptile(x: int, y: int, z: int):
    image = BytesIO()
    img = gen_png(x,y,z)
    img.save(image, format="PNG")
    image.seek(0)
    return Response(content=image.read(), media_type="image/png")