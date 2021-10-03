from NarutoAnimeBot.events import register
from NarutoAnimeBot import OWNER_ID
from NarutoAnimeBot import telethn as tbot
import os
import random
from PIL import Image, ImageDraw, ImageFont


logopics = [
 
 "./NarutoAnimeBot/resources/logopics/photo_2021-09-11_10-41-31.jpg",
	
 "./NarutoAnimeBot/resources/logopics/photo_2021-09-11_15-46-57.jpg",

 "./NarutoAnimeBot/resources/logopics/photo_2021-09-18_13-56-02.jpg",

 "/NarutoAnimeBot/resources/logopics/photo_2021-09-18_14-07-29.jpg",

 "./NarutoAnimeBot/resources/logopics/photo_2021-09-15_18-51-19.jpg",
	
 "./NarutoAnimeBot/resources/logopics/photo_2021-09-14_16-34-25.jpg"
 
]

logofonts = [
 
 "./NarutoAnimeBot/resources/logofonts/Pocket Monk.tff"
 
]

pic_choice = random.choice(logopics)
font_choice = random.choice(logofonts)


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(pic_choice)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype(font_choice , 150)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="blue", stroke_width=10, stroke_fill="black")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @VALTAOITHEBOT")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @pigasussupport, {e}')

   
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__mod_name__ = "Logos"

__help__ = """
`/logo`*:* Create a logo with text!
"""
