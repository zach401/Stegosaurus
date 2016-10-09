# Stegosaurus
A simple steganography module written in Python. 
Stegosaurus allows you to hide messages in the last bits of image pixels and retreive it later.
All data is hidden throughout the image based on a user specified password. Without this password it would be extremely difficult to retreive any data from an image or even tell that data was stored in the image.

# Image Formats
So far Stegosaurus has only been tested with png images. Jpg images will not work, as the data is compressed out of the picture.

# Input File Formats
So far hide.py and uncover.py have only been designed to work with plain text files. In the future other file types may be supported.

# Use
Stegosaurus can be be used from the command line through the hide.py and uncover.py scripts provided or embedded in another project.

## hide.py
1. Clone or download the repo.
2. Navigate to the downloaded directory.
3. Run the command python3 hide.py input_image_name output_image_name message_file 
-Replace input_file_name, output_image_name, and message_file with the full or relative path to the input png image, the desired output png image, and the input message file that you want to hide.
4. If you receive an error message saying that your message will not fit in the given image, try again with a larger image or a shorter message.
5. When prompted for a password, enter a password you can remember and press enter. 
6. When the script exits, your message has been successfully hidden.

## uncover.py
1. Clone or download the repo.
2. Naviage to the downloaded directory. 
2. Run the command python3 hide. input_image_name -
-Replace input_image_name with the full or relative path to the image containing your hidden message.
3. Enter the same password used to encode the message.
4. If the password was current, the text hiden in the image will display. If it was not, gibberish will be displayed. 
5. You will be prompted if you would like to save the message. Type y to save the image.
6. Enter the full or relative path to the file where you would like to save the image. 


