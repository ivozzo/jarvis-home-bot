import asyncio
import modules.alt_text as altText
import sys
import getopt


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
            altText.find_all_images(command[1], command[2])
            continue

        elif prompt == "exit":
            print("Jarvis is shutting down. Thank you sir")
            break


def usage():
    print("""
Jarvis HELP
          
    -h  --help                  Shows this help section
    -a  --generate--alt-text    Generate alt text for images found in a selected path
    -f  --format                Select the format to filter the images
    
Don't select any of the above to enter CLI mode
""")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "haf:v", ["generate-alt-text=", "format="])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    if len(opts) == 0:
        print("Entering Jarvis CLI mode...")
        asyncio.run(cli())
    else:
        # Default values
        format="jpg"
        path="."

        # Getting user input values
        for opt, arg in opts:
            if opt == '-h':
                usage()
                sys.exit()
            elif opt in ("-a", "--generate-alt-text"):
                print("Generating alt text for images in path: %s" % arg)
            elif opt in ("-f", "--format"):
                print(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
