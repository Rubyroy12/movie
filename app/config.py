class Config:
    """General configuration parent class"""
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    link= 'https://api.themoviedb.org/3/movie/550?api_key=5b554e67624057bcd681bdca1bb261ec'

class ProdConfig(Config):
    """Production configuration child class
    Args:
    Config: general configuration parent class that conatains general configurations
    """
    pass
class DevConfig(Config):
    """Develpment configuration child class
    Args: 
    Config: parent configuration class that conatains general configurations
    
    """
    DEBUG=True