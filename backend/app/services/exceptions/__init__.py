from typing import Optional

class AlreadyExistsError(Exception):
    """
    Exceção levantada quando uma constraint de unicidade for violada
    """

    def __init__(self, *fields: str, message: Optional[str] = None):
        self.fields = fields

        if not message:
            self.message = "The listed fields have already been taken"
        else:
            self.message = message

        super().__init__(self.message)

class EntityNotFoundError(Exception):
    """
    Exceção levantada quando não for possível encontrar uma entidade para
    o parâmetro informado e o retorno não puder ser vazio
    """

    def __init__(self, message: Optional[str] = None):
        if not message:
            self.message = "Could not find a entity for the given key"
        else:
            self.message = message

        super().__init__(self.message)

class ForbiddenOperationError(Exception):
    """
    Exceção levantada quando um usuário tentar acessar um resource que
    não pertence a ele
    """

    def __init__(self, message: Optional[str] = None):
        if not message:
            self.message = "You have no permission to access this resource"
        else:
            self.message = message

        super().__init__(self.message)
