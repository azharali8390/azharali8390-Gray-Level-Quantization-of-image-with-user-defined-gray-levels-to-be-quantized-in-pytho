from PIL import Image
import numpy as np
import cv2
import os
import string
import  random



def quantizer(image, value):
    ROOT_DIR = os.path.abspath(os.curdir)+'/static/images'
    input_image = Image.open(image)
    imgGray = input_image.convert('L')
    cols = imgGray.width
    rows = imgGray.height
    pixels_value_of_gray_image = np.array(imgGray)
    # val = int(input(" Enter to what gray levels you want to quantized"))
    quantized_gray = 256 / value
    quantize = quantized_gray
    lower = [0 for i in range(value)]
    midlle = [0 for i in range(value)]
    upper = [0 for i in range(value)]
    lower[0] = 0
    upper[0] = lower[0] + (quantized_gray - 1)
    midlle[0] = int((lower[0] + (quantized_gray - 1)) / 2)
    for i in range(1, value):
        lower[i] = upper[i - 1] + 1
        upper[i] = lower[i] + (quantized_gray - 1)
        midlle[i] = midlle[i - 1] + quantized_gray

    power_of_ans = 0
    rem = 1
    while quantized_gray != 1:
        quantized_gray = quantized_gray / 2
        power_of_ans = power_of_ans + 1
        print(power_of_ans)
    or_mask = [0, 0, 0, 0, 0, 0, 0, 0]

    bits_count_upper_map = 8 - power_of_ans
    for i in range(power_of_ans):
        or_mask[i + bits_count_upper_map] = '1'

    final_or_mask_for_highendmapping = ''.join([str(elem) for elem in or_mask])

    ######################and mask
    and_mask = [1, 1, 1, 1, 1, 1, 1, 1]
    # count2=8-power_of_ans
    # i=0
    for i in range(power_of_ans):
        and_mask[i + bits_count_upper_map] = '0'

    and_mask_low_endmapping = ''.join([str(elem) for elem in and_mask])

    ##############making or and mask for middle value
    power_of_ans = power_of_ans - 1  ### because we have to go middle value
    or_mask1 = [0, 0, 0, 0, 0, 0, 0, 0]
    bits_count_for_middle = 8 - power_of_ans
    for i in range(power_of_ans):
        or_mask1[i + bits_count_for_middle] = '1'
    or_mask_for_middle_mapping = ''.join([str(elem) for elem in or_mask1])
    and_mask1 = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(power_of_ans):
        and_mask1[i + bits_count_for_middle] = '0'
    and_mask_for_middle = ''.join([str(elem) for elem in and_mask1])
    # print("and_mask_for_middle")
    # print(and_mask_for_middle)

    dec_or_mask_big_for_highendmapping = int(final_or_mask_for_highendmapping, 2)
    dec_and_mask_low_endmapping = int(and_mask_low_endmapping, 2)
    dec_and_mask_for_middle_mapping = int(and_mask_for_middle, 2)
    dec_or_mask_for_middle_mapping = int(or_mask_for_middle_mapping, 2)

    ##############part2 mapping at high end with or mask

    image_pixels_after_high_end_mapping = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            image_pixels_after_high_end_mapping[i][j] = (
                    dec_or_mask_big_for_highendmapping | pixels_value_of_gray_image[i][j])
    img1 = Image.fromarray(image_pixels_after_high_end_mapping)
    # img1.show()
    rand1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))+'.jpg'
    img1.convert('RGB').save(ROOT_DIR + '/'+str(rand1))
    high_img = ROOT_DIR +'/'+str(rand1)

    ##############part3 mapping at low end with and mask
    image_pixels_after_low_end_mapping = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            image_pixels_after_low_end_mapping[i][j] = (dec_and_mask_low_endmapping & pixels_value_of_gray_image[i][j])
    img2 = Image.fromarray(image_pixels_after_low_end_mapping)
    # img2.show()
    rand2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))+'.jpg'
    img2.convert('RGB').save(ROOT_DIR + '/'+str(rand2))
    low_img = ROOT_DIR +'/'+str(rand2)

    ###################part4 for middle mapping
    image_pixels_after_middle_mapping = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            pixel_value = pixels_value_of_gray_image[i][j]
            for k in range(value):
                if (pixel_value > lower[k] and pixel_value <= upper[k]):
                    if pixel_value < midlle[k]:
                        image_pixels_after_middle_mapping[i][j] = (
                                pixels_value_of_gray_image[i][j] | dec_or_mask_for_middle_mapping)
                    else:
                        image_pixels_after_middle_mapping[i][j] = (
                                pixels_value_of_gray_image[i][j] & dec_and_mask_for_middle_mapping)
                    break

    img3 = Image.fromarray(image_pixels_after_middle_mapping)
    rand3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))+'.jpg'
    img3.convert('RGB').save(ROOT_DIR+'/'+str(rand3))
    middle_img = ROOT_DIR + '/'+str(rand3)
    return {'High_v': str(final_or_mask_for_highendmapping),'high_p':str(rand1), 'Low_v': str(and_mask_low_endmapping),'low_p': str(rand2), 'middle_v':str(and_mask_for_middle),'or_middle_v':str(or_mask_for_middle_mapping),'middle_p': str(rand3)}
