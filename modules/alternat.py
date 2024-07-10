import os

import modules.utilities as utilities
from alternat.generation import Generator


async def get_alt_text_for_path(input_path, format, verbose=False, overwrite=False):
    thumbnail_output_path = "thumbnails/"
    generated_output_path = "output/"
    if not os.path.exists(thumbnail_output_path):
        if verbose:
            print("-" * 40)
            print("Creating thumbnail directory: %s" % thumbnail_output_path)
        os.mkdir(thumbnail_output_path)

    if not os.path.exists(generated_output_path):
        if verbose:
            print("-" * 40)
            print("Creating thumbnail directory: %s" % generated_output_path)
        os.mkdir(generated_output_path)

    print("Retrieving images")
    images = utilities.find_all_images(input_path, thumbnail_output_path, format, verbose, overwrite)
    total_images = len(images)
    processed_images = 0
    error_images = 0

    print("-" * 40)
    print("%s images retrieved and enqueued for elaboration" % total_images)
    print("-" * 40)
    for image in images:
        if verbose:
            print("=" * 40)
            print("Elaborating image: %s" % image.get("filename"))
        try:
            generator = Generator("opensource")
            get_alt_text_for_image(generator, image, generated_output_path, verbose)
            processed_images = processed_images + 1
        except Exception as e:
            print(e)
            error_images = error_images + 1
        if verbose:
            print("=" * 40)
            print()

    print("""
=============== REPORT ================
%s images found
%s images processed
%s images in error
=======================================
""" % (total_images, processed_images, error_images))


def get_alt_text_for_image(generator, image, output_path, verbose=False):

    input_file = image.get("path") + image.get("filename")

    if verbose:
        print(" >>> Path: %s " % input_file)
    generator.generate_alt_text_from_file(
        input_image_path=input_file,
        output_dir_path=output_path
    )
