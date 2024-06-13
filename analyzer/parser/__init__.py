import ctypes

import parser as parserpy

parserc = ctypes.CDLL("analyzer/parser/parser.so")


def parse_file(savefile_name: str) -> str:
    newfile_name = savefile_name.replace(".v2", ".json")
    try:
        parserc.parse_by_name(
            bytes(savefile_name, encoding="utf-8"),
            bytes(newfile_name, encoding="utf-8"),
        )
    except:
        parserpy.parse_by_name(savefile_name, newfile_name)

    return newfile_name
