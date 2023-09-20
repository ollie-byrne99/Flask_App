from application import db, app

app.app_context().push()

class Location(db.Model):
    __tablename__ = "locations"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)



    def __repr__(self):
        return f"Character(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name}
