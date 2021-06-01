class Config:
    """General configuration parent class"""
    pass

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