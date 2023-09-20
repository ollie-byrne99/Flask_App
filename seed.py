from application import db
from application.locations.models import Location

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = Location(name="Phoebe")
entry2 = Location(name="Urkel")
entry3 = Location(name="Edward Elric (FMA)")

db.session.add_all([entry1, entry2, entry3])

db.session.commit()
