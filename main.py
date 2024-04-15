import asyncio
import modules.alt_text as altText
#from sydney import SydneyClient


async def main() -> None:

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

if __name__ == "__main__":
    asyncio.run(main())
