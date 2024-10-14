from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.logging import logger

def execute_stage(stage_name, pipeline_class):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        stage_pipeline = pipeline_class()
        stage_pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

# Usage
execute_stage("Data Ingestion", DataIngestionTrainingPipeline)
execute_stage("Data Validation", DataValidationTrainingPipeline)
execute_stage("Data Transformation", DataTransformationTrainingPipeline)
#execute_stage("Model Trainer", ModelTrainerTrainingPipeline)
#execute_stage("Model Evaluation", ModelEvaluationTrainingPipeline)
