import os

from sydney.exceptions import NoResponseException, CreateConversationException

import modules.utilities as utilities

from sydney import SydneyClient


async def get_alt_text_for_path(input_path, format, prompt, verbose=False, overwrite=False):
    thumbnail_output_path = "thumbnails/"
    if not os.path.exists(thumbnail_output_path):
        if verbose:
            print("-" * 40)
            print("Creating thumbnail directory: %s" % thumbnail_output_path)
        os.mkdir(thumbnail_output_path)
    else:
        if verbose:
            print("-" * 40)
            print("thumbnail directory already existing, clearing: %s" % thumbnail_output_path)
        utilities.delete_all_files(thumbnail_output_path, verbose)

    results_output_path = "results/"
    if not os.path.exists(results_output_path):
        if verbose:
            print("-" * 40)
            print("Creating results directory: %s" % results_output_path)
        os.mkdir(results_output_path)
    else:
        if verbose:
            print("-" * 40)
            print("results directory already existing, clearing: %s" % results_output_path)
        utilities.delete_all_files(results_output_path, verbose)

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
        if verbose:
            print("=" * 40)
            print("Image metadata:")
            for metadata in image.get("metadata"):
                tag = metadata.get("tag")
                value = metadata.get("value")
                print(f"{tag:25}: {value}")
        try:
            response = await get_alt_text_for_image(image.get("thumbnail"), prompt, verbose)
            utilities.generate_alt_text_file(results_output_path, image.get("filename"), format, response)
            processed_images = processed_images + 1
        except NoResponseException as e:
            print(e)
            print("Please try again")
            error_images = error_images + 1
        except CreateConversationException as e:
            print(e)
            print("Please try again")
            error_images = error_images + 1
        if verbose:
            print("=" * 40)
            print()

    print("""
============ REPORT ============
%s images found
%s images processed
%s images in error (please try again)
================================
""" % (total_images, processed_images, error_images))


async def get_alt_text_for_image(path, prompt, verbose=False):
    response = ""
    async with SydneyClient(style="precise") as sydney:
        if verbose:
            print(" >>> Prompt asked: %s " % prompt)
            print(" >>> Uploading image %s as attachment" % path)
        response = await sydney.ask(prompt, attachment=path)
        if verbose:
            print(" <<< Response received: %s " % response)
        await sydney.reset_conversation()

    return response
