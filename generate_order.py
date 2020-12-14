import argparse

def main():
    # Set up the command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="The location of the names file", default="./names.txt")
    
    # Parse the arguments
    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    main()
