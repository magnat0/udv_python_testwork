from db.news import NewRepository

class NewService:
    
    def __init__(self, repository : NewRepository) -> None:
        self.repository = repository

    def get_news(self) -> dict:
        news = self.repository.get_news()
        news["news"] = [i_new  for i_new in news["news"] if not i_new["deleted"]]

        for i_new in news["news"]:
            i_new["comments_count"] = len(self.repository.get_comments_by_new_id(i_new["id"]))
        
        news["news_count"] = len(news["news"])

        return news

    def get_news_with_comments(self):
        news = self.repository.get_news()

        for i_new in news["news"]:
            i_new["comments"] = self.repository.get_comments_by_new_id(i_new["id"])
            i_new["comments_count"] = len(i_new["comments"])
        
        return news["news"]
        

        
