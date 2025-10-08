from pathlib import Path
import json

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

# Capturando o diretório atual 
_current_dir = Path(__file__).parent

def get_log_config() -> dict:
    """
    Retorna um dicionário contendo as configurações do logger
    """
    config_file = _current_dir.joinpath("logger_config.json")

    with open(config_file, encoding='utf-8') as log_config_f:
        return json.load(log_config_f)

class Settings(BaseSettings):
    """
    Model para mapear as configurações da aplicação
    """
    model_config = SettingsConfigDict(env_file='.env')

    sqlalchemy_database_uri: str
    secret_key: str
    access_token_expire_time: int = 30
    token_hash_algorithm: str = "HS256"

settings = Settings()
