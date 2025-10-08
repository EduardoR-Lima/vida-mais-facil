import logging.config
import logging

from ..config import get_log_config

# Configurando o logger antes de criar uma instância
logging.config.dictConfig(get_log_config())

# Criando instância global
logger = logging.getLogger('video_storage')