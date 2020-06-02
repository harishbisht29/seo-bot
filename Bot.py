import abc

class Bot(abc.ABC):
    
    @abc.abstractmethod
    def post_on_account(self):
        pass
    @abc.abstractmethod
    def get_articles(self):
        pass
