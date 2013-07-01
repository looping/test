from peewee import *

db = SqliteDatabase('a.db')
#db = MySQLDatabase('a_db', user='root', passwd='root')

class BaseModel(Model):
	class Meta:
		database = db

class Users(BaseModel):
	name = CharField()
	first_name = CharField()
	last_name = CharField()
	password = CharField()
	last_login = DateField()
	email = CharField()
	first_login = DateField()
	def dispose(self):
		pass
	def getpasswd_byname(self, name):
		return "testpwd"

class Groups(BaseModel):
	name = CharField()
	attribute = CharField()
	owner = ForeignKeyField(Users);	
	def __unicode__(self):
		return self.title

class UserGroups(BaseModel):
        user = ForeignKeyField(Users)
        role = CharField()
        group = ForeignKeyField(Groups)

class Messages(BaseModel):
        title = CharField()
        content = CharField()
        attribute = CharField()
        owner = ForeignKeyField(Users)
        create_time = DateField()
        send_from = ForeignKeyField(Users)
        send_to_user = ForeignKeyField(Users)
        send_to_group = ForeignKeyField(Groups)
        status = CharField()
        
class Boxes(BaseModel):
        owner = ForeignKeyField(Users)
        name = CharField()
        attribute = CharField()
        
class MessageBoxes(BaseModel):
        message = ForeignKeyField(Messages)
        box = ForeignKeyField(Boxes)

class Images(BaseModel):
        name = CharField()
        arrtibute = CharField()

class video(BaseModel):
        name = CharField()

class Audio(BaseModel):
        name = CharField()
        
class Provinces(BaseModel):
        name = CharField()
        pointx = CharField()
        pointy = CharField()
        flag_img = ForeignKeyField(Images)
        
class Citys(BaseModel):
        name = CharField()
        pointx = CharField()
        pointy = CharField()
        flag_img = ForeignKeyField(Images)
        attribute = CharField()
        location = ForeignKeyField(Provinces)
        
class Estates(BaseModel):
        name = CharField()
        owner = CharField()
        map_img = ForeignKeyField(Images)
        location = ForeignKeyField(Citys)

class Villages(BaseModel):
        name = CharField()
        location = ForeignKeyField(Estates)
        
class Buildings(BaseModel):
        name = CharField()
        owner = CharField()
        location = ForeignKeyField(Villages)

class Units(BaseModel):
        name = CharField()
        location = ForeignKeyField(Buildings)

class Floors(BaseModel):
        name = CharField()
        location = ForeignKeyField(Units)

class Rooms(BaseModel):
        name = CharField()
        location = ForeignKeyField(Floors)
