import os
import modules.utilities as utilities

from sydney import SydneyClient


async def get_alt_text_for_path(input_path, format, verbose=False, overwrite=False):
    output_path = "thumbnails/"
    if not os.path.exists(output_path):
        if verbose:
            print("-" * 40)
            print("Creating thumbnail directory: %s" % output_path)
        os.mkdir(output_path)

    print("Retrieving images")
    images = utilities.find_all_images(input_path, output_path, format, verbose, overwrite)
    print("-" * 40)
    print("%s images retrieved and enqueued for elaboration" % len(images))
    print("-" * 40)
    for image in images:
        response = await get_alt_text_for_image(image.get("thumbnail"), verbose)
        utilities.generate_alt_text_file(input_path, image.get("filename"), format, response)


async def get_alt_text_for_image(path, verbose=False):
    response = ""
    async with SydneyClient(style="precise") as sydney:
        if verbose:
            print("Uploading image %s as attachment" % path)
        response = await sydney.ask("Genera un alt text semplice per questa immagine", attachment=path)
        if verbose:
            print(" Response received: %s " % response)
        await sydney.reset_conversation()

    return response
