from PIL import Image
import os

dir_name = input("Please enter the folder name:\n")
real_path = dir_name

if (not dir_name[len(dir_name)-1]=='/'):
    real_path += '/'

files_list = os.listdir(real_path)
extension_list = ['.png', '.jpg', 'jpeg']

for file_name in files_list:
    print(file_name)
    if (os.path.splitext(file_name)[1] in extension_list):
        image_file = Image.open(real_path + file_name)
        image_file = image_file.convert('L')
        image_file.save(real_path + file_name + "_black_white.png")

print("\nCONVERT OVER")
