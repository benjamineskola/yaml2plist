#!/usr/bin/env python
import argparse
import os
import sys
from collections import OrderedDict

import yaml


class Yaml2Plist:
    def __init__(self, file):
        self.label = os.path.splitext(os.path.basename(file))[0]
        loaded_data = yaml.safe_load(open(file))
        self.data = OrderedDict({"Label": self.label})
        self.data.update(loaded_data)

    def generate(self):
        output = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
{self._handle_dict(None, self.data, 1)}</plist>""".strip()
        return output

    def _handle_dict(self, key, value, depth=0):
        output = ""

        if key:
            output += "  " * depth + f"<key>{key}</key>\n"
        output += "  " * depth + "<dict>\n"

        for subkey, subvalue in value.items():
            classname = subvalue.__class__.__name__

            if classname == "dict":
                output += self._handle_dict(subkey, subvalue, depth + 1)
            elif classname == "int":
                output += self._handle_int(subkey, subvalue, depth + 1)
            elif classname == "list":
                output += self._handle_list(subkey, subvalue, depth + 1)
            elif classname == "bool":
                output += self._handle_bool(subkey, subvalue, depth + 1)
            elif classname == "str":
                output += self._handle_str(subkey, subvalue, depth + 1)

        output += "  " * depth + "</dict>\n"

        return output

    def _handle_bool(self, key, value, depth=0):
        output = "  " * depth + f"<key>{key}</key>\n"
        if value:
            output += "  " * depth + "<true/>\n"
        else:
            output += "  " * depth + "<false/>\n"
        return output

    def _handle_int(self, key, value, depth=0):
        output = "  " * depth + f"<key>{key}</key>\n"
        output += "  " * depth + f"<integer>{value}</integer>\n"
        return output

    def _handle_list(self, key, value, depth=0):
        output = "  " * depth + f"<key>{key}</key>\n"
        output += "  " * depth + "<array>\n"
        for subvalue in value:
            output += self._handle_str(None, subvalue, depth + 1)
        output += "  " * depth + "</array>\n"

        return output

    def _handle_str(self, key, value, depth=0):
        output = ""
        if key:
            output += "  " * depth + f"<key>{key}</key>\n"
        output += "  " * depth + f"<string>{value}</string>\n"
        return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path to yaml file to be processed")
    parser.add_argument(
        "output",
        nargs="?",
        help="path to output plist file to (defaults to same as input, with changed extension)",
    )
    args = parser.parse_args()

    if not args.output:
        args.output = os.path.splitext(args.input)[0] + ".plist"

    print(Yaml2Plist(args.input).generate(), file=open(args.output, "w"))


if __name__ == "__main__":
    main()
