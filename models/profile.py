from .databaseConfig import db
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    def __repr__(self):
        return f'<profile {self.username}>'
    def to_dict(self):
        return {c.username: getattr(self, c.username) for c in self.__table__.columns}