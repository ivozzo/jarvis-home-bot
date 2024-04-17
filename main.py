import asyncio
import sys
import getopt
import modules.copilot as copilot
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


async def cli() -> None:

    print("Starting Jarvis, please hold on.")
    print("Jarvis startup completed.")

    while True:
        prompt = input("command: ")
        print("Received command %s" % prompt)

        # Create alt text for photographs contained in a folder
        if prompt.startswith("alttext"):
            command = prompt.split(' ')

            if len(command) == 1 or command[1] == '':
                print("No path prompted, please add the path (relative or absolute) to your request.")
                continue

            if command[1] == "help":
                print("Command usage: 'alttext path [format]'. I.e. 'alttext /images/2024_04_15 jpg'")
                continue

            print("Creating alt text for all the photographs in the path prompted")
            # altText.find_all_images(command[1], command[2])
            continue

        elif prompt == "exit":
            print("Jarvis is shutting down. Thank you sir")
            break


def usage():
    print("""
Jarvis HELP
          
    -h  --help                  Shows this help section
    -a  --generate-alt-text    Generate alt text for images found in a selected path
    -f  --format                Select the format to filter the images
    -v  --verbose               Enable verbose mode
    -o  --overwrite             Enable overwrite mode
    
Select none of the above to enter CLI mode
""")


async def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:a:f:ov", ["help", "generate-alt-text=", "format=", "overwrite", "verbose"])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    if len(opts) == 0:
        print("Entering Jarvis CLI mode...")
        asyncio.run(cli())
    else:
        # Default values
        format = ".jpg"
        path = "."
        command = ""
        overwrite = False
        verbose = False

        # Getting user input values
        for o, a in opts:
            if o == '-h':
                usage()
                sys.exit()
            elif o in ("-a", "--generate-alt-text"):
                path = a
                if not path.endswith("/"):
                    path = path + "/"
                command = "alttext"
            elif o in ("-f", "--format"):
                format = a
                if not format.startswith("."):
                    format = "." + format
            elif o in ("-o", "--overwrite"):
                overwrite = True
            elif o in ("-v", "--verbose"):
                verbose = True

        if command == "alttext":
            print("Generating alt text for images in selected path")
            if verbose:
                print("-"*40)
                print("Path: %s" % path)
                print("Format: %s" % format)
                print("-" * 40)
            await copilot.get_alt_text_for_path(path, format, verbose, overwrite)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
