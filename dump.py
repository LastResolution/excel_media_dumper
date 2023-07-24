import sys

from file_util import exists_file, get_media, initialize, is_xlsx


if __name__ == "__main__":
    path_list: list[str] = sys.argv[1:]

    if not len(path_list):
        print("Arguments is None.")
        print("Please input dump .xlsx file path.")

    initialize()

    for path in path_list:
        # file exists judge
        if not exists_file(path):
            continue

        # .xlsx judge
        if not is_xlsx(path):
            continue

        # run main function
        get_media(path)
