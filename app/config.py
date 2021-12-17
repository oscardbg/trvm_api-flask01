import sqlalchemy


class Config:
	DEBUG = True
	SECRET_KEY = 'lsjdlkfj2l3k4jlk'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///apidata.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	