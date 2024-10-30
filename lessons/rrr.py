import sys
def main():
    if len(sys.argv) == 1:
        print("Error")
        sys.exit(1)
    else:
        print("Programm ", sys.argv[0], " was started with args")
        for arg in sys.argv[1:]:
            print(arg)
if __name__ == "__main__":
    main()