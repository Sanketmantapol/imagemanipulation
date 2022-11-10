from PIL import Image
from image_manipulation import flip


# Get image path
image_path = input("Enter full path of your image: ")
im = Image.open(image_path)

option = input("Choose number from below, what would you like to do? \n \
    1. Flip the image \n \
    2. Rotate the image \n \
    3. Resize the image \n \
    4. Crop the image \n \
    5. Blur the image\n")

if option == "1":
    flip_option = input("How would you like to flip? \n \
        a. Flip left to right \n \
        b. Flip top to bottom \n \
        c. Rotate 90 \n \
        d. Rotate 180 \n \
        e. Rotate 270\n")
    flip_result = flip(im, flip_option)
    flip_result.show()

elif option == "2":
    pass


#     rotate_option =
# im = Image.open("./Input/Dragon1.jpg")


if __name__ == "__main__":
    pass