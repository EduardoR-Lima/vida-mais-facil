from typing import Optional

class InvalidCredentialsError(Exception):
    """
    Exceção levantada quando não for possível validar as credenciais
    informadas, tanto no processo de validação do token quanto no
    processo de login
    """

    def __init__(self, message: Optional[str] = None):
        if not message:
            self.message = "Could not validate credentials"
        else:
            self.message = message

        super().__init__(self.message)
