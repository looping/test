from peewee import *

db = SqliteDatabase('a.db')
#db = MySQLDatabase('a_db', user='root', passwd='root')
class BaseModel(Model):
	class Meta:
		database = db
class Blog(BaseModel):
	content = CharField()
	title = CharField()
	def __unicode__(self):
		return self.title
class User(BaseModel):
	name = CharField()
	username = CharField()
	password = CharField()
	last_login = DateField()


def create_tables():
	User.create_table()
	Blog.create_table()
