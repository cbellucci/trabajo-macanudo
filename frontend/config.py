import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  
  RECAPTCHA_USE_SSL = True
  RECAPTCHA_PUBLIC_KEY = '6LcK79ESAAAAAKosCIouR-X-9FBawGYE1rEr02FO'
  RECAPTCHA_PRIVATE_KEY = '6LcK79ESAAAAAKy-jWiShHL0lbmSoEWMixfISNmV'
  RECAPTCHA_OPTIONS = {'theme': 'clean', 'lang': 'es'}
  
  DEBUG_TB_PROFILER_ENABLED = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  
  TWITTER_CONSUMER_KEY = 'xV6ojPUAlNUgKDlVuEqS4w',
  TWITTER_CONSULER_SECRET = '1X1wDMReQkcc2H63mxRJWCykXy5lONhpBZQwsARE'
  TWITTER_TOKEN = '587752364-ywSbTBnX2AdunBXnx7SnGtIYMencJC4TbFtnDXlB'
  TWITTER_SECRET = 'EWjVWxWV1FPrse94X3PhdRTleSxux5h0cHuHmaSRA'

class DefaultConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__)

class TestingConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)

class HerokuConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  RECAPTCHA_PUBLIC_KEY = '6Lco79ESAAAAAPKyci6r9mVxKzXu9QbSICcRWRnE'
  RECAPTCHA_PRIVATE_KEY = '6Lco79ESAAAAAE6_QrNDFzb9S2J979gk5fDsgDWj'
