from db.news import NewRepository
from services.news import NewService

new_repository = NewRepository()

new_service = NewService(new_repository)

def get_new_service() -> NewService:
    return new_service