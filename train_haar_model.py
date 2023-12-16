import os

positive_images_path = r'E:\Python\CV\haar-like_dataset\pos'
negative_images_path = r'E:\Python\CV\haar-like_dataset\neg'

cascade_classifier_output_path = r'E:\Python\CV\haar-like_dataset\haar-like.xml'

positive_images_count = len(os.listdir(positive_images_path))
negative_images_count = len(os.listdir(negative_images_path))

image_size = (608, 1080)

positive_images_list_file = r'E:\Python\CV\haar-like_dataset\positive_images.txt'
negative_images_list_file = r'E:\Python\CV\haar-like_dataset\negative_images.txt'

num_stages = 10  
with open(positive_images_list_file, 'w') as file:
    for filename in os.listdir(positive_images_path):
        file.write(os.path.join(positive_images_path, filename) + '\n')


with open(negative_images_list_file, 'w') as file:
    for filename in os.listdir(negative_images_path):
        file.write(os.path.join(negative_images_path, filename) + '\n')

opencv_bin_path = r'E:\Program\opencv\build\x86\vc14\bin'


command = f'{opencv_bin_path}\\opencv_traincascade -data {cascade_classifier_output_path} -vec {positive_images_list_file} ' \
          f'-bg {negative_images_list_file} -numStages {num_stages} -w {image_size[0]} -h {image_size[1]}'

os.system(command)