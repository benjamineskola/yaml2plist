# yaml2plist

Generate plist files from yaml input.

Particularly intended for LaunchAgent configuration but in theory works on any.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install yaml2plist.

```bash
pip install -e git+https://gitlab.com/benjamineskola/yaml2plist.git#egg=yaml2plist
```

## Usage

```bash
usage: yaml2plist [-h] input [output]

positional arguments:
  input       path to yaml file to be processed
  output      path to output plist file to (defaults to same as input, with
              changed extension)

optional arguments:
  -h, --help  show this help message and exit
```

## License

[CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)
