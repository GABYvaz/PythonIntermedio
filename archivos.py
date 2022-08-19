from ast import Pass


def read():
    number = []
    with open("./archivos/number.txt", "r",encoding="utf-8") as f:
        for line in f:
            number.append(int (line))
            print(number)


def write():
    names = ["Gabriela","Gerardo", "Ruth", "Francisco"]
    with open("./archivos/name.txt", "w") as f:
        for name in name:
            f.write(name)
            f.write("\n")

def run():
   read()


if __name__ == '__main__':
    run()