from pieces.config.schemas.model import ModelInfo
from pieces.settings import Settings


def change_model(**kwargs):  # Change the model used in the ask command
    model_index = kwargs.get("MODEL_INDEX")
    if model_index:
        models = Settings.pieces_client.get_models()
        # because we begin from 1
        model_name = list(models.keys())[model_index - 1]
        model_id = models[model_name]
        Settings.model_config.model = ModelInfo(name=model_name, uuid=model_id)
        Settings.logger.print(f"Switched to {model_name}")
    else:
        raise Exception("Invalid model index or model index not provided.")
