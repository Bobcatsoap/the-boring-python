from PIL import Image
from PIL import ImageDraw
import sys, os, imghdr

ASCII_CHARS = ['.', ',', ':', ';', '^', '/', '=', '+', '*', 'a', 'g', '%', '$', '@', '&']
IMAGE_EXTENSION = ['png', 'jpg', 'jpeg']
ASCII_CHARS_reverse = ASCII_CHARS[::-1]
images = []


# 缩放图片
def scale_image(image, width):
    (origin_width, origin_height) = image.size
    height = int(width * origin_height / float(origin_width))

    return image.resize((width, height))


# 转化为灰度图
def convert_to_gray(image):
    return image.convert('L')


# 转化为 ASCII 码列表
def convert_gray_to_ASCII(image):
    pixel = list(image.getdata())
    char_list = [ASCII_CHARS_reverse[int(float(level) / 255 * (len(ASCII_CHARS) - 1))] for level in pixel]
    return ''.join(char_list)


# 按照长宽格式化 ASCII 码列表
def format_chars_list(chars_list, image_width):
    format_char_list = [chars_list[index:index + image_width] for index in range(0, len(chars_list), image_width)]
    return format_char_list  # 返回分完组的字符二维数组


# 保存
def save_chars_list_form_in_image(chars_list, width, height, output_file_name):
    img = Image.new('RGB', (width * 10, height * 10), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            d.text((x * 10, y * 10), chars_list[y][x], fill=(0, 0, 0))
    img.save(output_file_name.split('.')[0] + '_ASCII.png')


def open_file(image_path):
    image = None
    try:
        image = Image.open(image_path)
    except Exception:
        print("Unable to open", image_path)
        sys.exit()
    images = [image]
    return images


def open_dir(image_path):
    image = None
    files_list = os.listdir(image_path)
    for file_name in files_list:
        if imghdr.what(input_path + file_name) in IMAGE_EXTENSION:
            try:
                image = Image.open(image_path + file_name)
            except Exception:
                sys.exit()
        images.append(image)
    return images


try:
    input_path = sys.argv[1]
    width = sys.argv[2]
except:
    print('please enter image path and target width')
    sys.exit()

# 是目录
if os.path.isdir(input_path):
    if not input_path[-1] == '/':
        input_path += '/'
    images = open_dir(input_path)

# 是文件
elif os.path.isfile(input_path):
    images = open_file(input_path)

for image in images:
    scaled_image = scale_image(image, int(width))
    new_width, new_height = scaled_image.size
    gray_image = convert_to_gray(scaled_image)
    char_list = convert_gray_to_ASCII(gray_image)
    format_char_list = format_chars_list(char_list, new_width)
    save_chars_list_form_in_image(format_char_list, new_width, new_height, image.filename)
