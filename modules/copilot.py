import asyncio
import modules.utilities as utilities

from sydney import SydneyClient


def get_alt_text_for_path(path, format):
        images = utilities.find_all_images(path, format)
        get_alt_text_for_image(images[0])


async def get_alt_text_for_image(path):
    async with SydneyClient(style="precise") as sydney:
        await sydney.start_conversation()
        response = await sydney.ask("What does this picture show?", attachment=path)
        print(response)
