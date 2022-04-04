from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    user_id = db.Column(db.Integer, primary_key=True)

class RoleUser(db.Model):
    __tablename__ = 'roles_users'

class User(db.Model):
    __tablename__ = 'users'

class RolModule(db.Model):
    __tablename__ = 'rol_module'

class Module(db.Model):
    __tablename__ = 'modules'