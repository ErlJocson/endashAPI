from app import db
import base64


class Cards(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    order = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(254), unique=True)
    link = db.Column(db.String(254), unique=True)
    icon = db.Column(db.BLOB)
    video = db.Column(db.BLOB, unique=True)

    def to_dict(self):
        return {
            "uid": self.uid,
            "order": self.order,
            "name": self.name,
            "icon": base64.b64encode(self.icon).decode('utf-8'),
            "video": base64.b64encode(self.video).decode('utf-8') 
        }