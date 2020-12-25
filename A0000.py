# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image, ImageDraw, ImageFont


def load_image(image_file, text='merry christmas'):
    image = Image.open(image_file)
    width, height = image.size
    image_draw = ImageDraw.Draw(image)  # 以打开的图片生成一个用以绘画的对象
    font_1_size = min(width // 18, height // 18)
    font_1 = ImageFont.truetype(r'‪C:\Windows\Fonts\arial.ttf', font_1_size) # 字体， 大小
    image_draw.text((width - len(text)*font_1_size*0.5 - width//18, height * 0.02), text, 'red',font=font_1,) #增加文字
    image.save('sample_1.jpg')


if __name__ == '__main__':
    load_image('bayern girl.jpg','how are you these days')
