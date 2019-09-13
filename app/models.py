class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language

class Articles:
   '''
    to define articles objects
   '''
   def __init__(self,id,author,title,description,url,image,date):
       self.id = id
       self.author = author
       self.title = title
       self.description = description
       self.url = url
       self.image = image
    #    self.date = date