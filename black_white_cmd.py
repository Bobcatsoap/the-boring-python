from PIL import Image
import os
import sys
import getopt

extension_list = ['.png', '.jpg', 'jpeg']


def convert_file(real_path):
    files_list = os.listdir(real_path)
    for file_name in files_list:
        print(file_name)
        if (os.path.splitext(file_name)[1] in extension_list):
            image_file = Image.open(real_path + file_name)
            image_file = image_file.convert('L')
            image_file.save(real_path + file_name + "_black_white.png")
    print("\nConvert Over")


def cmd_help():
    print("python", sys.argv[0], "-i <folder name>\n")
    print("python", sys.argv[0], "--help")


def get_cmd_input():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:", ["help", "input="])
    except getopt.GetoptError:
        cmd_help()
        sys.exit()
    for name, value in opts:
        if name in ("-i", "--input"):
            if (not value[len(value) - 1] == '/'):
                return value + '/'
            return value
        if name in ["--help"]:
            cmd_help()


if (not get_cmd_input() == None):
    convert_file(get_cmd_input())
else:
    cmd_help()
