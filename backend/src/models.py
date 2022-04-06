from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    user_id= db.Column(db.Integer, primary_key=True)
    code_role= db.Column(db.Integer)
    name_rol= db.Column(db.String(200), unique=True)
    description_rol= db.Column(db.String(200))
    create_date= db.Column(db.DataTime, default=datatime.utcnow)
    
class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    code_role= db.Column(db.Integer)
    active= db.Column(db.Boolean, default=true)
    user_id= db.Column(db.Integer, primary_key=True)
    roles_creation_date= db.Column(db.DataTime, default=datatime.utcnow)
    last_registration_roles= db.Column(db.DataTime, default=datatime.utcnow)

class User(db.Model):
    __tablename__ = 'users'
    user_id= db.Column(db.Integer, db.ForeingKey('roles_users.user_id') primary_key=True)
    email= db.Column(db.String(200), nullable=False, unique=True )
    password= db.Column(db.String(200))
    name= db.Column(db.String(200))
    last_name= db.Column(db.String(200))
    active= db.Column(db.Boolean, default=True)
    user_creation_date= db.Column(db.DataTime, default=datatime.utcnow)
    last_registration_date= db.Column(db.DataTime, default=datatime.utcnow)

class RolModule(db.Model):
    __tablename__ = 'rol_modules'
    user_id= db.Column(db.Integer, primary_key=True)
    code_module= db.Column(db.Integer)
    roles_creation_date= db.Column(db.DataTime, default=datatime.utcnow)
    last_registration_roles= db.Column(db.DataTime, default=datatime.utcnow)

class Module(db.Model):
    __tablename__ = 'modules'
    code_module= db.Column(db.Integer)
    name_module= db.Column(db.String(200))
    description_module= db.Colum(db.Text(500))
    creation_date= db.Column(db.DataTime, default=datatime.utcnow)