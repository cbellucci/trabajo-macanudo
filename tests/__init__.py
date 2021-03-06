import warnings
warnings.simplefilter("ignore", DeprecationWarning)

from flaskext.testing import TestCase

from frontend import create_app
from frontend.config import TestingConfig
from frontend.extensions import db

class FrontendTestCase(TestCase):
  def create_app(self):
    app = create_app(TestingConfig)
    return app

  def setUp(self):
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
