# Code by Hings Hsu

import cv2
import numpy as np

def reduce_resolution(image, factor):

    height, width, _ = image.shape    # 获取原始图像的宽度和高度

    new_width = int(width / factor) # 计算新的宽度和高度
    new_height = int(height / factor)

    # 使用resize方法来缩小图像分辨率，保持尺寸不变
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image

def motion_blur(image, degree=12, angle=45):
    image = np.array(image)

    # 这里生成任意角度的运动模糊kernel的矩阵， degree越大，模糊程度越高
    M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

    motion_blur_kernel = motion_blur_kernel / degree
    blurred = cv2.filter2D(image, -1, motion_blur_kernel)

    # convert to uint8
    cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
    blurred = np.array(blurred, dtype=np.uint8)
    return blurred


img = cv2.imread(r'YOUR/IMAGE/PATH')

idex = 1
Image_perturbation_Gaussian_idex = 1.10*idex
Image_perturbation_Motion_idex = 5*idex
Image_perturbation_reduceresolution_idex = 2.5*idex

#
Gaussian_blurred_image = cv2.GaussianBlur(img, ksize=(0,0), sigmaX=Image_perturbation_Gaussian_idex) # ksize 必须是一个正奇数,可以通过 (0, 0) 来自动计算核的大小
Motion_blurred_image = motion_blur(img, degree=Image_perturbation_Motion_idex, angle=45)
reduce_resolution_image = reduce_resolution(img, factor=Image_perturbation_reduceresolution_idex)

# cv2.imshow('Original', img)
# cv2.imshow('Gaussian Filter', Gaussian_blurred_image)
# cv2.imshow('Motion Filter', Motion_blurred_image)
# cv2.imshow('reduce_resolution Filter', reduce_resolution_image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 保存图像
cv2.imwrite("save/Gaussian_blurred_image" + str(Image_perturbation_Gaussian_idex) +".jpg", Gaussian_blurred_image)  # 保存降低分辨率后的图像
# cv2.imwrite("save/Motion_blurred_image" + str(Image_perturbation_Motion_idex) +".jpg", Motion_blurred_image)  # 保存降低分辨率后的图像
# cv2.imwrite("save/reduced_resolution_image_" + str(Image_perturbation_reduceresolution_idex) +".jpg", reduce_resolution_image)  # 保存降低分辨率后的图像