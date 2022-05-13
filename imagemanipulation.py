from PIL import Image, ImageFilter
import os

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)
        i.thumbnail(size_700)
        i.save("700/{}_700{}".format(fn,fext))
        i.thumbnail(size_300)
        i.save("300/{}_300{}".format(fn,fext))

wallpaper1= Image.open("wallpaper1.jpg")
wallpaper1.rotate(90).show("wallpaper1.jpg")
wallpaper2 = Image.open("wallpaper2.jpg")
wallpaper2.convert(mode = "L").show("wallpaper2.jpg")
wallpaper3 = Image.open("wallpaper3.jpg")
wallpaper3.rotate(180).show("wallpaper3.jpg")
wallpaper4 = Image.open("wallpaper4.jpg")
wallpaper4.filter(ImageFilter.GaussianBlur(10)).show("wallpaper4.jpg")
wallpaper5 = Image.open("wallpaper5.jpg")
wallpaper5.convert(mode = "L").show("wallpaper5.jpg")
wallpaper6 = Image.open("wallpaper6.jpg")
wallpaper6.rotate(20).show("wallpaper6.jpg")
wallpaper7 = Image.open("wallpaper7.jpg")
wallpaper7.filter(ImageFilter.GaussianBlur(15)).show("wallpaper7.jpg")
wallpaper8 = Image.open("wallpaper8.jpg")
wallpaper8.convert(mode = "L").show("wallpaper8.jpg")
wallpaper9 = Image.open("wallpaper9.jpg")
wallpaper9.rotate(90).show("wallpaper9.jpg")
wallpaper10 = Image.open("wallpaper10.jpg")
wallpaper10.show("wallpaper10.jpg")

wp_list = ["wallpaper1", "wallpaper2", "wallpaper3","wallpaper4", "wallpaper5", "wallpaper6","wallpaper7", "wallpaper8", "wallpaper9", "wallpaper10"]
mod_list = ["rotate", "resize", "png", "blur", "black and white"]

def list(x):
    for i in x:
        print(i)
    print("")

#this function asks users what image they want to change
def run():
    while True:
        print("Images: ")
        list(wp_list)
        change = input("What image would you like to change?: ").lower()
        if change in wp_list:
            userImage = Image.open(f"{change}.jpg")
            userImage.show()
            if editimage() == True:
                break
            else:
                print("Invalid Input\n")
        alterimage()

#this function asks users if they want to edit a photo
def editimage():
    choice = input ("Would you like to edit this photo? Type 'Y' (yes) or 'N' (no): ").upper()
    if choice == "Y":
        return True
    elif choice == "N":
        print("")
        run()
    else:
        print("Invalid response, please try again")

#this function asks users if they want to either rotate, resize, convert to png, blur, or change the shade to black and white
def alterimage():
    while True:
        print ("Alter options: ")
        list(mod_list)
        alter = input("Select alter mode: ").lower()
        if alter in mod_list:
            if editimage() == True:
                if alter == mod_list[0]:
                    alter.rotate()
                if alter == mod_list[1]:
                    alter.resize()
                if alter == mod_list[2]:
                    alter.png()
                if alter == mod_list[3]:
                    alter.blur()
                if alter == mod_list[4]:
                    alter.blacknwhite()
