# importing module
import cv2

image = cv2.imread("shi.jpg") 

# changing image to greyscale
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# inverting image
inv_img = 255 - grey_img

# bluring image
blur = cv2.GaussianBlur(inv_img, (21, 21), 0)

# invting blured image
inv_blur = 255 - blur

# converting to sketch
pencil_sketch = cv2.divide(grey_img, inv_blur, scale=256.0)

# resizing image
scale_percent = 60 # percent of original size
width = int(pencil_sketch.shape[1] * scale_percent / 100)
height = int(pencil_sketch.shape[0] * scale_percent / 100)
dim = (width, height)
resize = cv2.resize(pencil_sketch, dim, interpolation = cv2.INTER_AREA)

# displaying image
cv2.imshow("drawn image", resize)
k = cv2.waitKey(0)

# download image
if k == ord("s"):
    cv2.imwrite("shi_sketch.png", resize)
