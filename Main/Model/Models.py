from .. import db, flask_bcrypt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(255), unique=True, nullable=False)
    ssn = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(100),default='Admin')
    username = db.Column(db.String(50), unique=True)
    passwordHash = db.Column(db.String(100))
    manager=db.relationship('Business', backref='user', lazy=True)
    employee = db.relationship('Service', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.passwordHash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Business(db.Model):
    """ Business Model for storing business related details """
    __tablename__ = "business"

    businessID = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    managerID = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    service = db.relationship('Service', backref='business', lazy=True)


class Service(db.Model):
    """ Service Model for storing service realated details """
    __tablename__ = "service"

    serviceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Integer, nullable=False)
    employerID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)
    businessID = db.Column(db.Integer, db.ForeignKey('business.businessID'), nullable=False)