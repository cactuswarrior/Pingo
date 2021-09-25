import os

import glob
from PIL import Image


def convert_png_to_jpg(path):
    # jpg파일을 저장하기 위한 디렉토리의 생성
    if not os.path.exists(path + "_jpg"):
        os.mkdir(path + "_jpg")

    # 모든 png 파일의 절대경로를 저장
    all_image_files = glob.glob(path + "/*.png")

    for file_path in all_image_files:  # 모든 png파일 경로에 대하여
        img = Image.open(file_path).convert("RGB")  # 이미지를 불러온다.

        directories = file_path.split("/")  # 절대경로상의 모든 디렉토리를 얻어낸다.
        directories[-2] += "_jpg"  # 저장될 디렉토리의 이름 지정
        directories[-1] = directories[-1][:-4] + ".jpg"  # 저장될 파일의 이름 지정
        save_filepath = "/".join(directories)  # 절대경로명으로 바꾸기
        img.save(save_filepath, quality=100)  # jpg파일로 저장한다.


path = "./datasets/pingo/"
convert_png_to_jpg(path)
