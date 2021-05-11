import os

def execute(command):
    try:
        if "<" in command:
            print()
            print("Executing.......")
            print()
            
            cmd = command.split("<", 1)
            os.system("type {}".format(cmd[1]))
        
        elif ">" in command:
            print()
            print("Executing.......")
            print()
            
            cmd = command.split(">", 1)
            print()
            print("Write everything you want")
            print("When you're done, type 'Ragnarok' on a single line and press Enter")

            string_list = []
            while True:
                print("> ", end = "")
                line = input()
                if line == "Ragnarok":
                    break
                string_list.append(line)
            multi_string = "\n".join(string_list)

            print("You entered.......")
            print()
            print(multi_string)

            f = open("{}".format(cmd[1]), "w")
            f = open("{}".format(cmd[1]), "a")
            f.write(multi_string)
            f.close()

    except Exception:
        print("Command not found: {}".format(command))


def help():
    print()
    print(" -----------------Window Shell by Python-----------------")
    print("r < [file name] : Read the data of the file and print it out")
    print("Example : r < input.txt, remember to put space: r_<_file")
    print("w > [file name] : Write everthing you'd input into the file")
    print("Example : w > output.txt, remember to put space: w_>_file")
    print("cls : Clear screen")
    print("exit : Exit") 
    print("help : Provide help information for commands")
    print(" --------------------------------------------------------")
    print()

def cls():
    os.system("cls")

def main():
    print("Type 'help' for more information\n")

    while True:
        good_boiz = input(">>>> ")
        if good_boiz == "exit":
            print("Bravo Six, we're going dark !")
            break
        elif good_boiz == "help":
            help()
        elif good_boiz == "cls":
            cls()
        else:
            execute(good_boiz)

if __name__ == '__main__':
    main()  