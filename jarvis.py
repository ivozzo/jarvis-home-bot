import asyncio
import sys
import getopt
import modules.copilot as copilot
import modules.utilities as utilities
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

copilot_env_variable = "BING_COOKIES"


async def cli_usage():
    print("""
Jarvis CLI HELP

    help            Shows this help section
    exit            Exit from CLI mode
    set-cookie     Set the cookie needed for Copilot, you'll be prompted to paste your cookie
    unset-cookie    Delete che cookie needed for Copilot previously set
""")


async def cli() -> None:

    print("Starting Jarvis, please hold on.")
    print("Jarvis startup completed.")

    while True:
        prompt = input("command: ")
        print("Received command %s" % prompt)

        # Create alt text for photographs contained in a folder
        if prompt == "help":
            await cli_usage()

        if prompt == "set-cookie":
            cookie = input("paste your cookie: ")
            if cookie is None or cookie == "" or cookie == " ":
                print("No cookie has been inserted")
            else:
                os.environ[copilot_env_variable] = cookie
                print("Environment variable %s has been set" % copilot_env_variable)

        if prompt == "unset-cookie":
            answer = input("are you sure? [y/N]: ")
            if answer != "N":
                os.environ.pop(copilot_env_variable)
                print("Environment variable %s has been deleted" % copilot_env_variable)

        elif prompt == "exit":
            print("Jarvis is shutting down. Thank you sir")
            break


def usage():
    print("""
Jarvis HELP
          
    -h  --help                  Shows this help section
    -a  --generate-alt-text     Generate alt text for images found in a selected path
    -f  --format                Select the format to filter the images
    -p  --prompt                Use a custom prompt enclosed with " " 
    -v  --verbose               Enable verbose mode
    -o  --overwrite             Enable overwrite mode
    
Select none of the above to enter CLI mode
""")


async def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:a:f:p:sov", ["help", "generate-alt-text=", "format=", "prompt=",
                                                         "set-cookie", "overwrite", "verbose"])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    else:
        # Default values
        format = ".jpg"
        path = "."
        command = ""
        overwrite = False
        verbose = False
        prompt = ""
        use_cookie = False

        # Getting user input values
        for o, a in opts:
            if o == '-h':
                usage()
                sys.exit()
            elif o in ("-s", "--set-cookie"):
                use_cookie = True
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
            elif o in ("-p", "--prompt"):
                prompt = a

        if command == "alttext":
            print("Generating alt text for images in selected path")
            if prompt == "":
                prompt = "Generate a brief alt text for this image"

            if use_cookie:
                print("Reading cookie from file and setting it as environment variable")
                utilities.set_cookie(copilot_env_variable, verbose)

            if verbose:
                print("-"*40)
                print("Path: %s" % path)
                print("Format: %s" % format)
                print("Prompt: %s" % prompt)
                print("-" * 40)

            await copilot.get_alt_text_for_path(path, format, prompt, verbose, overwrite)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Executing Jarvis in command mode...")
        asyncio.run(main(sys.argv[1:]))
    else:
        print("Entering Jarvis CLI mode...")
        asyncio.run(cli())