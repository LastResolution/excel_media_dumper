import os


def initialize() -> None:
    if not os.path.exists("resources"):
        os.makedirs("./resources")


def exists_file(path: str) -> bool:
    if not os.path.exists(path):
        print("File not found.")
        print(f" > {path}")
        print("\n")
        return False
    else:
        return True


def is_xlsx(path: str) -> bool:
    if not path.endswith(".xlsx"):
        print("Only xlsx files are supported.")
        print(f" > {path}")
        print("\n")
        return False
    else:
        return True
