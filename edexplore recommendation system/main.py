from datetime import datetime
class Blog:
    def __init__(self,title,author,views,tags,category,publishedAt) -> None:
        self.category=category
        self.title=title
        self.author=author
        self.publishedAt=publishedAt
        self.views=views
        self.tags=tags
tags=[
    "physics",'chemistry','maths','engineering','mechanics','computer science','software development'
]
b1=Blog("All you need to know about rockets","a1",5,[tags[0],tags[3]],'physics',datetime.now())