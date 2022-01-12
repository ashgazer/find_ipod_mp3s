import argparse
import glob
from typing import List


from mutagen.easyid3 import EasyID3


def load_mp3_directories(dir: str) -> List[str]:
    return glob.glob(f"/{dir}/*/*.mp3")


def load_mp3_tags(file: str) -> EasyID3:
    return EasyID3(file)


def create_db_csv(mp3_files: List[str]) -> None:
    with open("mp3_data.csv", "w") as f:
        for mp3 in mp3_files:
            mp3_tags = load_mp3_tags(mp3)
            mp3_values = [tag[0] for tag in mp3_tags.values()]
            mp3_values.append(mp3)
            f.write(",".join(mp3_values) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--flag")

    args = parser.parse_args()

    file_path = args.flag
    mp3s = load_mp3_directories(file_path)
    create_db_csv(mp3s)
