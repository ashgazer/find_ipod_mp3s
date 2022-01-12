from main import load_mp3_directories


def test_load_mp3_directories():
    result = load_mp3_directories()
    assert result == [
        "./sample_data/A2/file_example_MP3_5MG.mp3",
        "./sample_data/A1/file_example_MP3_5MG.mp3",
    ]
