import sys, json

import v2_parser
import cmds

def load_data(path: str) -> dict:
    
    if ".v2" in path:
        file = v2_parser.load_file(path)
        return v2_parser.parse(file)

    if ".json" in path:
        with open(path, 'r') as f:
            return json.load(f)

    raise Exception("Wrong filetype :D")



def main():
    try:
        path = sys.argv[1]
    except IndexError:
        path = input("Input savefile path (.v2/.json): ")

    save_data = load_data(path)

    running = True
    while running:

        cmd = input("Input command (h for help): ").split(" ")
        if cmd[0] == "war":
            try:
                cmds.war_analyze(save_data, cmd)
            except AttributeError:
                print("The Independence War is goofyly written")

        elif cmd[0] in ["exit", "quit", "stop", "q"]:
            running = False
            break

if __name__ == "__main__":
    main()



