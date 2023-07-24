import os
import shutil


def initialize() -> None:
    if not os.path.exists("resources"):
        os.makedirs("./resources/input")
        os.makedirs("./resources/output")


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


def get_media(path: str) -> bool:
    file_name: str = __get_file_name(path)
    __copy_file(path, file_name)


def __get_file_name(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def __copy_file(path: str, file_name: str) -> None:
    copy_name: str = os.path.join(
        os.getcwd(), f"resources{os.sep}input{os.sep}{file_name}.zip"
    )

    shutil.copy(path, copy_name)
