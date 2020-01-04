#
# This is where the different debugging situations and such will be specified.
# The dream team example has a few examples.
#

# setting the amount of hash rounds
BCRYPT_LOG_ROUNDS = 12
class Config(object):
    """
    Common configurations
    """

    DEBUG = True

    # setting the amount of hash rounds
    BCRYPT_LOG_ROUNDS = 12


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True

    # setting the amount of hash rounds
    BCRYPT_LOG_ROUNDS = 12


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

    # setting the amount of hash rounds
    BCRYPT_LOG_ROUNDS = 12


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True

    # setting the amount of hash rounds
    BCRYPT_LOG_ROUNDS = 12

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
