import io
import os
import shutil
import zipfile


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
    __copy_media(path, file_name)


def __get_file_name(path: str, with_extension: bool = False) -> str:
    if with_extension:
        return os.path.basename(path)
    else:
        return os.path.splitext(os.path.basename(path))[0]


def __copy_file(path: str, file_name: str) -> None:
    copy_name: str = os.path.join(
        os.getcwd(), f"resources{os.sep}input{os.sep}{file_name}.zip"
    )

    shutil.copy(path, copy_name)


def __copy_media(path: str, file_name: str) -> None:
    print(f"Start dump > {path}")
    if not os.path.exists(f"resources{os.sep}output{os.sep}{file_name}"):
        os.makedirs(f"resources{os.sep}output{os.sep}{file_name}")

    try:
        zip: zipfile.ZipFile = zipfile.ZipFile(
            f"resources{os.sep}input{os.sep}{file_name}.zip", "r"
        )
    except Exception as e:
        print("Failed dump.")
        print(e)
        print("Please make sure you have the correct .xlsx file.")
        print("\n")
        return

    file_list: list[zipfile.ZipInfo] = zip.infolist()

    media_count: int = 0
    for file in file_list:
        if file.filename.startswith("xl/media/"):
            save_name: str = __get_file_name(file.filename, with_extension=True)
            with zip.open(file.filename) as image:
                img_bin = io.BytesIO(image.read())
                with open(
                    f"resources{os.sep}output{os.sep}{file_name}{os.sep}{save_name}",
                    "wb",
                ) as save_file:
                    try:
                        save_file.write(img_bin.getbuffer())
                    except Exception as e:
                        print("File save failed.")
                        print("\n")

                    media_count += 1
                    print(f"Saving... {media_count}files.")
    print(f"Save {media_count} files.")
    print(f"Output > resources{os.sep}output{os.sep}{file_name}{os.sep}{save_name}")
    print("\n")
