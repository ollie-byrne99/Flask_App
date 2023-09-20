from application import db, app
from datetime import datetime

app.app_context().push()

class Location(db.Model):
    __tablename__ = "locations"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    business_name = db.Column(db.String(150), nullable=False)
    contact_email = db.Column(db.String(150), nullable=True)
    contact_phone = db.Column(db.String(20), nullable=True)
    price_per_day = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    is_available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Location(id: {self.id}, name: {self.name}, address: {self.address}, business: {self.business_name})"

    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "date_posted": self.date_posted,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "business_name": self.business_name,
            "contact_email": self.contact_email,
            "contact_phone": self.contact_phone,
            "price_per_day": self.price_per_day,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "is_available": self.is_available
        }
