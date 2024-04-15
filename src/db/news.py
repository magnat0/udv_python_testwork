from config import NEWS_PATH, COMMENTS_PATH
import json


class NewRepository:

    def get_news(self) -> dict:
        with open(NEWS_PATH) as news_file:
            news_data = json.load(news_file)
        
        return news_data

    def get_comments(self) -> dict:
        with open(COMMENTS_PATH) as comments_file:
            comments_data = json.load(comments_file)
        
        return comments_data
    
    def get_comments_by_new_id(self, new_id: int) -> list:
        news_comments = []
        comments_data = self.get_comments()
        
        for i_comment in comments_data["comments"]:
            if i_comment["news_id"] == new_id:
                news_comments.append(i_comment)
        
        return news_comments

        