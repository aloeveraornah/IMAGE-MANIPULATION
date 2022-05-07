from PIL import Image, ImageFilter
import os

wallpaper1 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper1.jpg")
wallpaper2 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper2.jpg")
wallpaper3 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper3.jpg")
wallpaper4 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper4.jpg")
wallpaper5 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper5.jpg")
wallpaper6 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper6.jpg")
wallpaper7 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper7.jpg")
wallpaper8 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper8.jpg")
wallpaper9 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper9.jpg")
wallpaper10 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper10.jpg")

def to_size():
    while True:
        thumbnail_size = int(input("Enter thumbnail size (200, 400 or 600): "))
        dimensions = (thumbnail_size, thumbnail_size)

        if thumbnail_size == 200 or thumbnail_size == 400 or thumbnail_size == 600:

            for f in os.listdir("."):
                if f.endswith(".jpg"):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)

                    i.thumbnail(dimensions)
                    i.save(f"{thumbnail_size}/{thumbnail_size}_{thumbnail_size}{thumbnail_size}".format(fn, fext))

            break
        else:
            continue

def to_png():
    while True:
        switch = input("Convert jpg to png? Enter 'Y' for yes or 'N' for no").upper()

        if switch == "Y":

            for f in os.listdir("."):
                if f.endswith(".jpg"):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save("png/{}.png".format(fn))

        elif switch == "N":
            break
        else:
            continue

def to_rotate():
    wallpaper1 = wallpaper1.rotate(90).save("/Users/chrispark/Downloads/Pillow/wallpaper1.jpg")
    wallpaper1 = Image.open("/Users/chrispark/Downloads/Pillow/wallpaper1.jpg")

def to_shades():
    wallpaper1.convert(mode="L").save("/Users/chrispark/Downloads/Pillow/wallpaper4.jpg")
    wallpaper2.convert(mode="L").save("/Users/chrispark/Downloads/Pillow/wallpaper5.jpg")
    wallpaper3.convert(mode="L").save("/Users/chrispark/Downloads/Pillow/wallpaper6.jpg")
    wallpaper4.convert(mode="L").save("/Users/chrispark/Downloads/Pillow/wallpaper7.jpg")    

def to_blur():
    while True:
        blur = int(input("How much do you want to blur some images? (30, 40 or 50): "))
        if blur == 30 or blur == 40 or blur == 50:
            wallpaper1.filter(ImageFilter.GaussianBlur(blur)).save("/Users/chrispark/Downloads/Pillow/wallpaper8.jpg")
            wallpaper2.filter(ImageFilter.GaussianBlur(blur)).save("/Users/chrispark/Downloads/Pillow/wallpaper9.jpg")
            wallpaper3.filter(ImageFilter.GaussianBlur(blur)).save("/Users/chrispark/Downloads/Pillow/wallpaper10.jpg")
            break
        else:
            continue

to_size()
to_png()
to_rotate()
to_shades()
to_blur()
