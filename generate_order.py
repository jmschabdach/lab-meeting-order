import argparse
import random

def main():
    # Set up the command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="The location of the names file", default="./names.txt")
    
    # Parse the arguments
    args = parser.parse_args()

    # Read the names from the file
    names = []
    with open(args.file, 'r') as f:
        names = f.readlines()

    # Remove whitespace from each line
    names = [n.strip() for n in names]

    # Shuffle the names
    random.shuffle(names)

    print()
    print("Quick round robin: what have you been working on, what are you planning to work on, and if you're stuck on anything, is there anything the rest of the lab can do to help?")

    # Print the names
    print("Presentation order is:")
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
