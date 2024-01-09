import cv2
from PIL import Image
import numpy as np
from rembg import remove

def cv_to_pil(img):
	return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA))


def pil_to_cv(img):
	return cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGRA)


def motion_blur(img, distance, amount):
    # Convert pil to cv
    cv_img = pil_to_cv(img)

    # Generating the kernel
    kernel_motion_blur = np.zeros((distance, distance))
    kernel_motion_blur[int((distance-1)/2), :] = np.ones(distance)
    kernel_motion_blur = kernel_motion_blur / distance

    # Applying the kernel to the input image
    output = cv2.filter2D(cv_img, -1, kernel_motion_blur)

    # Convert cv to pil
    blur_img = cv_to_pil(output).convert('RGBA')

    # Blend the original image and the blur image
    final_img = Image.blend(img, blur_img, amount)

    return final_img


def background_motion_blur(background, distance_blur, amount_blur, amount_subject):
    # Remove background
    subject = remove(background)

    # Blur the background
    background_blur = motion_blur(background, distance_blur, amount_blur)
    
    # Put the subject on top of the blur background
    subject_on_blur_background = Image.alpha_composite(background_blur, subject)

    # Blend the subject and the blur background
    result = Image.blend(background_blur, subject_on_blur_background, amount_subject)

    return result