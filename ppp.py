class cal:
    def __init__(self,category,date,title,submit):
        self.category=category
        self.date=date
        self.title=title
        self.submit=submit
        EmailData.totalCount+=1

    def display(self):
        print (EmailData.totalCount)
        print (EmailData.allData[0])
