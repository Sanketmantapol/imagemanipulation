from PIL import Image, ImageFilter
im = Image.open(r"C:\Users\Asus\Downloads\Image Manipulation\Image Manipulation\Input\Dragon2.jpg")

im.show()

# Basic image manipulation - Flip, Rotate, Resize, Crop
# Filtering - Blur, 
# Image Enhancement - Sharpness, contrast

# Transpose/Flip
out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# out = im.transpose(Image.Transpose.ROTATE_90)
# out = im.transpose(Image.Transpose.ROTATE_180)

out.show()


def flip(im, option):
    if option == "a":
        out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif option == "b":
        out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    elif option == "c":
        out = im.transpose(Image.Transpose.ROTATE_90)
    elif option  == "d":
        out = im.transpose(Image.Transpose.ROTATE_180)
    else:
        out = im.transpose(Image.Transpose.ROTATE_270)
    return out

# Rotate
# out = im.rotate(45, expand = True, fillcolor=(255, 255, 255))

#Resize
# out  = im.resize((1920, 1080))
# out.save(r"E:\NextStepInfoTechCourses\10 Python 10\Project Works\Image Manipulation\Output\Resized.png")

#Resizing image maintaing aspect ratio
# im.thumbnail((1920, 1080))
# im.save(r"E:\NextStepInfoTechCourses\10 Python 10\Project Works\Image Manipulation\Output\Thumbnail.png")

# print(im.size)
# scale = 2

# out = im.resize((im.size[0]*scale, im.size[1]*scale))
# out.save(r"E:\NextStepInfoTechCourses\10 Python 10\Project Works\Image Manipulation\Output\Resize.jpg")

#Crop
# out = im.crop((500, 500, 1800, 1200))
# out.show()


# im1 = im.filter(ImageFilter.BoxBlur(9))
# im1.show()