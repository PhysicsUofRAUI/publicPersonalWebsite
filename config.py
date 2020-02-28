#
# This is where the different debugging situations and such will be specified.
# The dream team example has a few examples.
#

class Config(object):
    """
    Common configurations
    """

    DEBUG = True



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True



class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False



class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
