import os
import urllib.request as rq
import zipfile
from scr.textSummarizer.logging import logger
from scr.textSummarizer.utils.common import get_size
from pathlib import Path
from scr.textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = rq.urlretrieve(
                url= self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file alreday exists of size; {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path : str
        extracts the zip file into the data directory
        function returns None
        """
        unzip_path =  self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)