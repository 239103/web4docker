from . import db

class host(db.Model):
    __tablename__ = 'hosts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    ipaddr = db.Column(db.String(15), unique=True)

    def __repr__(self):
        return '<Host %r>' % self.name

class container(db.Model):
    __tablename__ = 'container'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
