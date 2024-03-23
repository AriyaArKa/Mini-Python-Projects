# import cv2
#
# source = "Harry_Potter_character_poster.jpg"
# destination = 'resized_img.png'
#
# # Instagram square photo dimensions
# instagram_width = 1080
# instagram_height = 1080
#
# src = cv2.imread(source)
#
# # Resize the image to fit Instagram square photo dimensions
# output = cv2.resize(src, (instagram_width, instagram_height))
#
# # Write the resized image to the destination file
# cv2.imwrite(destination, output)
#
# # Wait for a key press to close the window (not necessary if not displaying image)
# cv2.waitKey(0)
#
# #for random size
# # import cv2
# #
# # source = "Harry_Potter_character_poster.jpg"
# # destination = 'resized_img.png'
# # scale_percent = 50  # Adjust scale percent as needed
# #
# # # Read the image
# # src = cv2.imread(source)
# #
# # # Calculate new dimensions based on scale percent
# # new_width = int(src.shape[1] * scale_percent / 100)
# # new_height = int(src.shape[0] * scale_percent / 100)
# #
# # # Resize the image
# # output = cv2.resize(src, (new_width, new_height))
# #
# # # Write the resized image to the destination file
# # cv2.imwrite(destination, output)
# #
# # # Wait for a key press to close the window (not necessary if not displaying image)
# # cv2.waitKey(0)
import cv2

def resize_image_for_instagram(source, destination, width, height):
    src = cv2.imread(source)
    output = cv2.resize(src, (width, height))
    cv2.imwrite(destination, output)
    cv2.waitKey(0)


if __name__ == "__main__":
    source = input("Enter the path to the input photo: ")
    destination = 'resized_img.png'  # Default destination file
    width = 1080  # Instagram square photo width
    height = 1080  # Instagram square photo height

    resize_image_for_instagram(source, destination, width, height)
