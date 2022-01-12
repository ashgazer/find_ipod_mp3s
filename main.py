import argparse
import csv
import glob
from typing import List

VALID_TAGS = ["artist", "album", "title"]

from mutagen.easyid3 import EasyID3


def load_mp3_directories(dir: str) -> List[str]:
    return glob.glob(f"{dir}/*/*.mp3")


def load_mp3_tags(file: str) -> EasyID3:
    return EasyID3(file)


def create_db_csv(mp3_files: List[str]) -> None:
    headers = ["artist", "album", "title", "dir"]
    with open("mp3_data.csv", "w") as f:
        f.write(",".join(headers) + "\n")
        try:
            for mp3 in mp3_files:
                mp3_tags = load_mp3_tags(mp3)
                mp3_values = dict(mp3_tags)
                mp3_values = [mp3_values[tag][0] for tag in VALID_TAGS]
                mp3_values.append(mp3)
                csv_writer = csv.writer(
                    f, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL,
                )
                csv_writer.writerow(mp3_values)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--flag")

    args = parser.parse_args()

    file_path = args.flag
    mp3s = load_mp3_directories(file_path)
    create_db_csv(mp3s)
