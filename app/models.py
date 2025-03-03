from app import db

class Cards(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    order = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(254), unique=True)
    link = db.Column(db.String(254), unique=True)
    icon = db.Column(db.LargeBinary)
    video = db.Column(db.LargeBinary, unique=True)

    def to_dict(self):
        return {
            "uid": self.uid,
            "order": self.order,
            "name": self.name,
            "link": self.link,
            "video": self.video
        }