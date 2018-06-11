from PIL import Image
from PIL import ImageDraw
import sys, os, imghdr, getopt

ASCII_CHARS = ['.', ',', ':', ';', '~', '^', '=', '*', 'a', 'g', 'M', '%', '#', '$', '&', '@']
IMAGE_EXTENSION = ['png', 'jpg', 'jpeg']
ASCII_CHARS_reverse = ASCII_CHARS[::-1]
images = []
Image.MAX_IMAGE_PIXELS = None


# 缩放图片 0:原始 dpi <10 缩放dpi >10
def scale_image(image, scale):
    if (scale == 0):
        return image
    if (0 < scale <= 10):
        (new_width, new_height) = image.size
        return image.resize((int(new_width / scale), int(new_height / scale)))
    else:
        print("Enter Error")
        sys.exit()


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
    img = Image.new('RGB', (width * 8, height * 8), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            d.text((x * 8, y * 8), chars_list[y][x], fill=(0, 0, 0))
    if (int(resolution) >= 50):
        w, h = img.size
        new_width = int(resolution)
        new_height = int(h / w * new_width)
        img = img.resize((new_width, new_height))
    img.save(output_file_name.split('.')[0] + '_ASCII.png')


# 打开图片
def open_file(image_path):
    image = None
    try:
        image = Image.open(image_path)
    except Exception:
        print("Unable to open", image_path)
        sys.exit()
    images = [image]
    return images


# 打开文件夹下的所有图片
def open_dir(image_path):
    image = None
    files_list = os.listdir(image_path)
    for file_name in files_list:
        if file_name.split('.')[-1] in IMAGE_EXTENSION:
            try:
                image = Image.open(image_path + file_name)
            except Exception:
                sys.exit()
        images.append(image)
    return images


# 更新进度条
def update_progress(current, max):
    progress = int(current / float(max) * 20)
    sys.stdout.write("\r[{0}{1}]{2}%".format('#' * progress, ' ' * (20 - progress), 100 * progress / float(20)))
    sys.stdout.flush()


# 过滤已生成图片
def filter_image(images):
    pass  # 过滤分辨率过大的文件[可以通过 Image.MAX_IMAGE_PIXELS = None 关闭限制]

    if len(images) > 1:
        # 获取所有文件名
        images_name = [image.filename for image in images]

        # 过滤所有已生成的目标文件
        images = [image for image in images if not '_ASCII' in image.filename]

        # 过滤所有已生成的源文件
        images = [image for image in images if
                  not image.filename.split('.')[0] + '_ASCII.png' in images_name]
    return images


# 检查是文件夹还是文件
def check_input(input_path):
    images = None
    # 是目录
    if os.path.isdir(input_path):
        if not input_path[-1] == '/':
            input_path += '/'
        images = open_dir(input_path)

    # 是文件
    elif os.path.isfile(input_path):
        images = open_file(input_path)

    return images


def start_up(input_path):
    images = check_input(input_path)
    images = filter_image(images)
    sys.stdout.write("\r[{0}]{1}%".format(' ' * 20, 0))
    sys.stdout.flush()
    for idx, image in enumerate(images):
        scaled_image = scale_image(image, int(scale))
        new_width, new_height = scaled_image.size
        gray_image = convert_to_gray(scaled_image)
        char_list = convert_gray_to_ASCII(gray_image)
        format_char_list = format_chars_list(char_list, new_width)
        save_chars_list_form_in_image(format_char_list, new_width, new_height, image.filename)
        update_progress(idx + 1, len(images))

    over()


def over():
    global input_path
    sys.stdout.write("\r[{0}]{1}%".format('#' * 20, 100))
    print('\nCONVERT_OVER')
    op_dir = os.path.dirname(input_path) if os.path.isfile(input_path) else input_path
    os.system("explorer " + op_dir.replace('/', '\\'))


input_path = ''
scale = 0
resolution = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:d:r:", [])
except getopt.GetoptError:
    print('convert_image_to_ascii.py -p <path> -d <scale,1~10> -r <width resolution>')
    sys.exit(3)

for opt, value in opts:
    if opt == '-h':
        print('convert_image_to_ascii.py <path> -d <scale,1~10> -r <width resolution>')
        sys.exit()
    if opt == '-d':
        scale = int(value)
    if opt == '-r':
        resolution = int(value)
    if opt == '-p':
        input_path = value

if (not (os.path.isfile(input_path) or os.path.isdir(input_path))):
    print('convert_image_to_ascii.py -p <path> -d <scale,1~10> -r <width resolution>')
    sys.exit()
print("r:", resolution, "d", scale)
start_up(input_path)
