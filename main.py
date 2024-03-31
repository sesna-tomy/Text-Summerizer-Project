from scr.textSummarizer.pipeline.stage01_data_ing import DataIngestionTrainingPipeline
from scr.textSummarizer.logging import logger
from scr.textSummarizer.pipeline.stage02_data_val import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<< stage {STAGE_NAME} completed >>>>>\n\nX====X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"<<<<< stage {STAGE_NAME} completed >>>>>\n\nX====X")
except Exception as e:
    logger.exception(e)
    raise e
