from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

CORS_ORIGINS = [
    "http://localhost:5000",
]

def create_app():
    """
    Application factory
    """
    app = FastAPI(
        title="Vida+Fácil",
        description="..."
    )

    # Registrando os handlers primeiros para poder referenciar as
    # exceções a partir do .utils.error_handling.raises
    from .exception_handlers import register_global_handlers
    register_global_handlers(app)

    # Importando após o registro dos handlers para assegurar que os
    # erros possam ser referenciados adequadamente
    from .routers import api_router
    app.include_router(api_router)

    # Para garantir que o cors middleware seja aplicado em todas as respostas,
    # inclusive as que forem geradas por exception_handlers
    return CORSMiddleware(
        app=app,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
