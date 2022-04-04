from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    user_id = db.Column(db.Integer, primary_key=True)
    code_role = db.Column(db.Integer)
    name_rol = db.Column(db.String(200), unique=True)
    description_rol = db.Column(db.String(200))
    create_date = db.Column(db.Timestamp)
    
class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    code_role = db.Column
    active = db.Column
    user_id =
    roles_creation_date =
    last_registration_roles =

class User(db.Model):
    __tablename__ = 'users'
    user_id = 
    email = 
    password = 
    name = 
    last_name =
    active
    user_creation_date = 
    last_registration_date =

class RolModule(db.Model):
    __tablename__ = 'rol_modules'
    user_id = 
    code_module = 
    roles_creation_date = 
    last_registration_roles =

class Module(db.Model):
    __tablename__ = 'modules'
    code_module =
    name_module = 
    description_module = 
    creation_date = 