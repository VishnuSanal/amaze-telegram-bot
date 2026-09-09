from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Exclusions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(256))
    summary = db.Column(db.String(256))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, device_id, summary, is_active):
        self.device_id = device_id
        self.summary = summary
        self.is_active = is_active

    def __repr__(self):
        return "<Exclusions(device_id='{}', summary='{}', is_active='{}', created_at='{}', updated_at='{}')>".format(self.device_id,
                                                                                                                     self.summary,
                                                                                                                     self.is_active,
                                                                                                                     self.created_at,
                                                                                                                     self.updated_at)
