import argparse

def main():
    # Set up the command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="The location of the names file", default="./names.txt")
    
    # Parse the arguments
    args = parser.parse_args()

    # Read the names from the file
    names = []
    with open(args.file, 'r') as f:
        names = f.read()

    print(names)
    # Shuffle the names
    # Print the names
    print("Presentation order is:")



if __name__ == "__main__":
    main()
