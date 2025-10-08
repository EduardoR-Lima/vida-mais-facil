from sqlalchemy import select

from .exceptions import AlreadyExistsError
from .exceptions import EntityNotFoundError
from ._base import DatabaseRequiredService
from ..utils.security import generate_password_hash
from ..models import Cliente

class ClienteService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'cliente'
    """
    def get_by_id(self, id_cliente: int):
        """
        Busca o cliente no banco de dados a partir do id

        :raises EntityNotFoundError:
            caso não seja encontrado nenhum cliente para o id fornecido
        """
        model = self._db_session.get(Cliente, id_cliente)

        # Esse cenário não deve acontecer, já que o id do cliente é
        # recuperado através do token
        if not model:
            raise EntityNotFoundError(
                f"Could not find 'Cliente' for id {id_cliente}"
            )

        return model

    def get_by_email(self, email: str):
        """
        Busca o cliente no banco de dados a partir do e-mail

        :raises EntityNotFoundError:
            caso não seja encontrado nenhum cliente para o email fornecido
        """
        model = self._db_session.execute(
            select(Cliente)
            .where(Cliente.email == email)
        ).scalar()

        if not model:
            raise EntityNotFoundError(
                f"Could not find 'Cliente' for email {email}"
            )

        return model

    def create(self, senha: str, **model_kwargs):
        """
        Registra um novo cliente no banco de dados

        :raises AlreadyExistsError:
            caso o email ou o cpf já tenham sido cadastrados
        """
        model = Cliente(**model_kwargs)

        conflicts = []
        if self._exists(Cliente.email == model.email):
            conflicts.append(Cliente.email.name)

        if self._exists(Cliente.cpf == model.cpf):
            conflicts.append(Cliente.cpf.name)

        if conflicts:
            raise AlreadyExistsError(*conflicts)
        
        model.hash_senha = generate_password_hash(senha)

        self._db_session.add(model)
        self._db_session.commit()

        return model
