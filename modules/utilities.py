import os
from PIL import Image
from PIL.ExifTags import TAGS


def find_all_images(input_path, output_path, format, verbose=False, overwrite=False):
    images = []
    try:
        if verbose:
            print("The following images has been found:")
        for (root, dirs, file) in os.walk(input_path):
            for f in file:
                if format in f:
                    if verbose:
                        print("- %s " % f)

                    # Check if thumbnail has already been created, if not or overwriting create it again
                    if check_if_thumbnail_already_exists(output_path, filename=f, verbose=verbose) and not overwrite:
                        if verbose:
                            print("     Thumbnail already existing, skipping")
                        thumb = output_path + f
                    else:
                        if verbose:
                            print("     Generating thumbnail")
                        thumb = generate_thumbnails(input_path, output_path, f)

                    metadata = get_metadata(input_path, f)

                    # Check if text has already been generated, if not or overwriting enqueue the item for generation
                    if not check_alt_file_existence(input_path, filename=f, format=format, verbose=verbose) or overwrite:
                        if verbose:
                            print("     Enqueueing image for Alt Text generation")
                        images.append(dict(thumbnail=thumb,
                                           filename=f,
                                           metadata=metadata))
                    else:
                        if verbose:
                            print("     Alt text has already been generated, skipping")
    except FileNotFoundError:
        print("ERROR: you haven't specified a valid path!")

    return images


def set_cookie(copilot_env_variable, verbose=False):
    cookie_file="bing_cookie.txt"
    with (open(cookie_file, 'r')) as f:
        cookie = f.read()
        if verbose:
            print("-" * 40)
            print(cookie)
            print("-" * 40)
        os.environ[copilot_env_variable] = cookie


def delete_all_files(input_path, verbose=False):
    try:
        if verbose:
            print("Deleting file:")
        for (root, dirs, file) in os.walk(input_path):
            for f in file:
                if verbose:
                    print("- %s " % f)
                os.remove(input_path + f)
    except FileNotFoundError:
        print("ERROR: you haven't specified a valid path!")


def check_if_thumbnail_already_exists(output_path, filename, verbose=False):
    for (root, dirs, file) in os.walk(output_path):
        for f in file:
            if filename in f:
                return True
    return False


def check_alt_file_existence(output_path, filename, format, verbose=False):
    for (root, dirs, file) in os.walk(output_path):
        for f in file:
            if filename.replace(format, '.txt') in f:
                return True
    return False


def generate_thumbnails(input_path, output_path, filename):
    input_filepath = input_path + filename

    image = Image.open(input_filepath)
    image.thumbnail((720,720))
    output_filepath = output_path + filename
    image.save(output_filepath)

    return output_filepath


def get_metadata(input_path, filename):
    metadata = []
    input_filepath = input_path + filename

    image = Image.open(input_filepath)
    exifdata = image.getexif()

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()

        metadata.append(dict(tag=tag,
                             value=data))

    return metadata


def generate_alt_text_file(output_path, filename, format, body, verbose=False):
    output_filepath = output_path + filename.replace(format, '.txt')
    print("Saving generated Alt Text for %s in %s " % (filename, output_filepath))
    with open(output_filepath, 'w') as f:
        f.write(body)
