import abc

class Bot(abc.ABC):
    
    @abc.abstractmethod
    def post_on_account(self):
        pass
    @abc.abstractmethod
    def get_articles(self):
        pass

    def get_source_url(self, url):
        if url[-1] == '/':
            url= url[0:-1]
        
        url= url+ "?source=twitter/"
        return url
