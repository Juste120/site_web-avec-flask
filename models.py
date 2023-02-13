
from project import app
from flask_sqlalchemy import SQLAlchemy


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/users'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add columns to your table here
    name = db.Column(db.String(80))
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    password = db.Column(db.String(150))
db.create_all()
