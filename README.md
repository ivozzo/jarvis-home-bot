# Jarvis

[![Latest Release](https://img.shields.io/github/v/release/ivozzo/jarvis-home-bot.svg)](https://github.com/ivozzo/jarvis-bot/releases/tag/v1.0.0)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/ivozzo/jarvis-bot/blob/master/LICENSE)

Useful bot for...stuff.

## Features

- Generate Alt Text for all images in a directory through the usage of Copilot (
  through [vsakkas/sydney.py](https://github.com/vsakkas/sydney.py))

## Requirements

- Python 3.9 or newer

## Usage
Jarvis can be used in Command mode or CLI mode.

### Prerequisites
Please check [vsakkas/sydney.py](https://github.com/vsakkas/sydney.py?tab=readme-ov-file#prerequisites) prerequisites
for setting up the Copilot integration.

### Command mode

| **option** | **long option**     | **description**                                       |
|------------|---------------------|-------------------------------------------------------|
| -h         | --help              | Shows a recap of this help section                    |
| -a         | --generate-alt-text | Generate alt text for images found in a selected path |
| -f         | --format            | Select the format to filter the images                |
| -p         | --prompt            | Use a custom prompt enclosed with " "                 |
| -v         | --verbose           | Enable verbose mode                                   |
| -o         | --overwrite         | Enable overwrite mode                                 |

### CLI mode

| **command**  | **description**                                                            |
|--------------|----------------------------------------------------------------------------|
| help         | Shows a recap of this help section                                         |
| exit         | Exit from CLI mode                                                         |
| set-cookie   | Set the cookie needed for Copilot, you'll be prompted to paste your cookie |
| unset-cookie | Delete che cookie needed for Copilot previously set                        |

### Examples

**Generating alt text for all jpg images found in /images/previousWeek** 
```shell
python jarvis.py -a /images/previousWeek -v -f jpg
```

**Generating alt text for all jpg images found in /images/previousWeek with a custom prompt** 
```shell
python jarvis.py -a /images/previousWeek -f jpg -p "Pretty please generate a very simple alt text for this image"
```

**Start Jarvis in CLI mode**
```shell
python jarvis.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.