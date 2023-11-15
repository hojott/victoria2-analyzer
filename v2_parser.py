import json

def load_file(path: str) -> str:
    """ Load vic2 savefile """

    with open(path, 'r', encoding="latin-1") as f:
        # Also parse tabs
        content = f.read().replace("\t", "")

    return content

def paste_file(path: str, content: dict) -> None:
    """ Save the data as json """

    with open(path.replace(".v2", ".json"), 'w') as f:
        json.dump(content, f)

def strip(string: str) -> int|float|str:
    """ Strip \n, \" and useless whitespaces, and turn to int/float """

    string = string.replace("\n", "").replace("\"", "").strip()
    try:
        string = int(string)
    except ValueError:
        try:
            string = float(string)
        except ValueError:
            pass
    
    return string

def parse(content: str, main=True) -> dict:
    """ Parse vic2 savefile recursively """

    # Start with bracket
    bracket_counter = 1
    dictionary = {}
    jump = 0
    length = len(content)

    for i, char in enumerate(content):

        # Progressbar
        if main and i%100:
            print(i/length, end="\r")

        # Jump over chars done with recursive functions
        if jump:
            jump -= 1
            continue

        # Check brackets + EOF
        try:
            if char == "{":
                bracket_counter += 1
        except IndexError:
            # End with bracket
            bracket_counter -= 1

        if char == "}":
            bracket_counter -= 1

        # Return when brackets have been closed
        if bracket_counter == 0:

            # The game uses some random keyless dicts that need to be cleared
            if not dictionary:
                i_copy = i - 1
                while content[i_copy] not in "\n{":
                    i_copy -= 1

                dictionary = strip(content[i_copy+1:i])

            return dictionary, i

        # The shit
        if char == "=":

            # Find key by going backwards (probably pretty slow)
            i_copy = i
            while content[i_copy] != "\n":
                i_copy -= 1

            key = content[i_copy+1:i]
            
            if content[i+1] in "\n " and content[i+2] == "{":
                # If the value is a dict, call the function for it
                data, jump = parse(content[i+3:], main=False)

                # Jump appears to need a bit of a push
                jump += 3

            else:
                # If it's a proper value, it will end with a newline
                i_copy = i
                while content[i_copy] != "\n":
                    i_copy += 1

                data = content[i+1:i_copy+1]
                data = strip(data)


            # Create list from data if the key already exists
            if key in dictionary.keys():
                if isinstance(dictionary[key], list):
                    dictionary[key].append(data)
                else:
                    dictionary[key] = [dictionary[key], data]
            else:
                dictionary[key] = data

    # I dunno just in case?
    return dictionary, i


if __name__ == "__main__":

    content = load_file("china.v2")

    json_data, _ = parse(content)

    paste_file("china.v2", json_data)


