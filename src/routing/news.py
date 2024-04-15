from fastapi import APIRouter, Depends, HTTPException
from depends import get_new_service
from services.news import NewService

router = APIRouter(prefix="/news", tags=["news"])

@router.get("", description="Getting all the news that has not been deleted")
async def get_not_del_news(new_service: NewService = Depends(get_new_service)) -> dict:
    news = new_service.get_news()
    return news

@router.get("/{news_id}", description="Getting news by index with a list of comments")
async def get_news_with_comments(news_id: int, new_service: NewService = Depends(get_new_service)) -> dict:
    news = new_service.get_news_with_comments()
    for i_new in news:
        if i_new['id'] == news_id:
            if i_new['deleted']:
                raise HTTPException(status_code=404, detail="The news has been deleted")
            return i_new
    raise HTTPException(status_code=404, detail="News not found")