import argparse
import os

def find(path):
    try:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith((".c", ".java", ".py", ".go")):
                    file_path = os.path.join(root, file)
                    print(file_path)
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = args.path
    find(path)