from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_validation import DataValidtion
from textsummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        # Configuration setup
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
    
        # Data Validation steps
        data_validation = DataValidtion(config=data_validation_config)
        data_validation.validate_all_files_exist()