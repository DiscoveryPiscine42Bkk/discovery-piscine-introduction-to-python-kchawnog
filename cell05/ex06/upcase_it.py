import sys
def main():
    if len(sys.argv) < 2:
        print("none")
    else:        
        text = " ".join(sys.argv[1:])
        print(text.upper())
main()
