from PIL import Image
import os

dir_name = input("请输入文件夹名\n")
real_path= dir_name + '/'
file_list = os.listdir(real_path)
extension_list = ['.png', '.jpg']

for file_name in file_list:
    print(file_name)
    if (os.path.splitext(file_name)[1] in extension_list):
        image_file = Image.open(real_path + file_name)
        image_file = image_file.convert('L')
        image_file.save(real_path+file_name + "black_white.png")
