import os
import sys


if __name__ == "__main__":
    path_list: list[str] = sys.argv[1:]

    for path in path_list:
        # file exists judge
        if not os.path.exists(path):
            print("File not found.")
            print(f" > {path}")
            print("\n")
            continue

        # .xlsx judge
        if not path.endswith(".xlsx"):
            print("Only xlsx files are supported.")
            print(f" > {path}")
            print("\n")
            continue
