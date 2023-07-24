import sys

from file_util import exists_file, is_xlsx


if __name__ == "__main__":
    path_list: list[str] = sys.argv[1:]

    for path in path_list:
        # file exists judge
        if not exists_file(path):
            continue

        # .xlsx judge
        if not is_xlsx(path):
            continue
