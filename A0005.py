# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# iphone5 分辨率为 640*1136
from PIL import Image
import os


def search_image(file_catalog, size_expect):
    files = os.listdir(file_catalog)
    for file in files:
        if file.endswith('jpeg') or file.endswith('jpg') or file.endswith('png') \
                or file.endswith('bmp') or file.endswith('gif'):
            zoom_image(file_catalog, file, size_expect)

    # os.mkdir()


def zoom_image(root, file_name, size_expect):
    img = Image.open(root + file_name)
    width, height = img.size
    scale = max(width / size_expect[0], height / size_expect[1])
    if scale > 1:
        new_size = (int(width / scale), int(height / scale))
        img = img.resize(new_size)
    img.save('./pic_after/' + file_name)


if __name__ == '__main__':
    size = (640, 1136)
    catalog = './picture/'
    search_image(catalog, size)
