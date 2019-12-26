import os
import sys

if "SECRET_KEY" not in os.environ:
    print("SECRET_KEY environment variable does not exist", file=sys.stderr)
    sys.exit(1)

if "DATABASE_URI" not in os.environ:
    base_uri = os.path.abspath(os.path.dirname(__file__))
    db_path = "sqlite:///" + os.path.join(base_uri, "db.sqlite")
else:
    db_path = os.environ["DATABASE_URI"]

HOST = "0.0.0.0"
PORT = 8080
DEBUG = True


class AppConfig:
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ["SECRET_KEY"]
