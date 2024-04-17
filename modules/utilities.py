import os
from PIL import Image


def find_all_images(input_path, output_path, format):
    images = []
    try:
        for (root, dirs, file) in os.walk(input_path):
            for f in file:
                if format in f:
                    print("Found file: %s " % f)
                    images.append(dict(thumbnail=generate_thumbnails(input_path, output_path, f), filename=f))
    except FileNotFoundError:
        print("ERROR: you haven't specified a valid path!")

    return images


def generate_thumbnails(input_path, output_path, filename):
    input_filepath = input_path + filename
    print("Generating thumbnail for file: %s " % input_filepath)

    image = Image.open(input_filepath)
    image.thumbnail((720,720))
    output_filepath = output_path + filename
    image.save(output_filepath)

    return output_filepath


def generate_alt_text_file(output_path, filename, format, body):
    output_filepath = output_path + filename.replace(format, '.txt')
    print("Saving response in %s " % output_filepath)
    with open(output_filepath, 'w') as f:
        f.write(body)

