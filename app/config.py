class Config:
    """General configuration parent class"""
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/{}?api_key={}'

    
    # link= 'https://api.themoviedb.org/3/movie/550?api_key=5b554e67624057bcd681bdca1bb261ec'
    #link2= 'https://api.themoviedb.org/3/movie/popular?api_key=de8ccdacc8a9ecfbc3a3e112926d20d9'

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