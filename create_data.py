import pathlib
from logzero import logger
import eyed3
import pandas as pd


def get_music_info(path):
    p = list(path)
    musics_info = list()
    logger.info(f"getting information of {len(p)} files")
    for item in range(len(p)):
        try:
            file_path = pathlib.Path(p[item]).as_posix()
            audio = eyed3.load(file_path)
            music_dict = {'title': audio.tag.title, 'album': audio.tag.album, 'artist': audio.tag.artist,
                          'composer': audio.tag.composer, 'bpm': audio.tag.bpm, 'genre': audio.tag.genre,
                          'date': audio.tag.recording_date, 'duration': audio.info.time_secs}
            musics_info.append(music_dict)
        except Exception as e:
            logger.exception(e)
            continue
    logger.info(f"creating csv file")
    df = pd.DataFrame(musics_info)
    df.to_csv('data/musics_data.csv', index=False, header=True)


if __name__ == '__main__':
    path = pathlib.Path('E:\Telegram 7 2022').glob('**\*.mp3')
    get_music_info(path)
    logger.info("Done!")
