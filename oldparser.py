import json

def load_file(path: str) -> dict:
    with open(path, 'r', encoding="latin-1") as f:
        content = f.read().encode("utf-8").decode()

    content = content.replace("\t", "")

    content = content.replace("\n\n", "\n")
    content = content.replace("\n{", "{")
    content = content.replace("{\n", "{ \"")
    content = content.replace("\n}", "},")
    content = content.replace("\n", ", \"")

    content = content.replace("=", "\": ")
    content = content.replace(" yes,", " true,")
    content = content.replace(" no,", " false,")
    content = content.replace(" yes}", " true}")
    content = content.replace(" no}", " false}")

    content = content.replace(",,", ",")
    content = content.replace(",}", "}")
 
    content = content.replace("{ \"2 }}", " 2 }")
    content = content.replace("{ \"}", "{ }")

    with open(path+".json", 'w') as f:
        f.write("{\"" + content+ "}")

    with open(path+".json", 'r') as f:
        json.load(f)

if __name__ == "__main__":
    path = "china.v2" #input("Path: ")
    load_file(path)
