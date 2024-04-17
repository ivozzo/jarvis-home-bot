import os

def find_all_images(path, format="jpg"):
    images = []

    try:
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if format in f:
                    print("Found file: %s " % f)
                    images.append(f)
    except FileNotFoundError:
        print("ERROR: you haven't specified a valid path!")
