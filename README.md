#Суть тестового задания  
Реализация back-end сервиса новостей, в котором будет REST API для получения новостей с комментариями.  

#Эндпоинты  
- GET "/" - возвращает список новостей следующего формата  
```
{
  "news": [
    {
      "id": 1,
      "title": "news_1",
      "date": "2019-01-01T20:56:35",
      "body": "The news",
      "deleted": false,
      "comments_count": 1,
    },
  ],
  "news_count": 1,
}
```  
- GET "/news/{id}" - возвращает новость по ее id  
```
{
  "id": 1,
  "title": "news_1",
  "date": "2019-01-01T20:56:35",
  "body": "The news",
  "deleted": false,
  "comments": [
    {
      "id": 1,
      "news_id": 1,
      "title": "comment_1",
      "date": "2019-01-02T21:58:25",
      "comment": "Comment",
    },
  ],
  "comments_count": 1,
}
```  
#Запуск проекта  
Чтобы запустить бэкенд на своей ПК, нужно выполнить следующие действия:
  
1. Склонировать репозиторий  

```git clone https://github.com/magnat0/udv_python_testwork.git```  
  
2. Перейти в директорию проекта  
  
```cd udv_python_testwork```  
  
3. Установить зависимости  
  
```pip3 install -r requirements.txt```  
  
4. Перейти в папку src  
  
```cd src```  
  
5. Запустить FastAPI 

```uvicorn app:app --reload```  

