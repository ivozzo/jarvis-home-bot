import os
import modules.utilities as utilities

from sydney import SydneyClient


async def get_alt_text_for_path(input_path, format):
    output_path = "thumbnails/"
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    images = utilities.find_all_images(input_path, output_path, format)
    for image in images:
        await get_alt_text_for_image(image)


async def get_alt_text_for_image(path):
    response = ""
    async with SydneyClient(style="precise") as sydney:
        # await sydney.start_conversation()
        print("Uploading image %s " % path)
        response = await sydney.ask("Genera un breve alt text per questa immagine", attachment=path)
        print("Response: %s " % response)
        # await sydney.close_conversation()

    return response
