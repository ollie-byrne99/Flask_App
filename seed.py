from application import db
from application.locations.models import Location

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = Location(
    name="Workspace Central",
    address="123 Main St, Springfield",
    description="A spacious workstation with dual monitors.",
    business_name="Central Inc.",
    contact_email="central@workspaces.com",
    contact_phone="123-456-7890",
    price_per_day=25.00,
    latitude=34.0522,
    longitude=-118.2437,
    is_available=True
)

entry2 = Location(
    name="Serenity Desk",
    address="456 Elm St, Shelbyville",
    description="Quiet and serene workspace by the window.",
    business_name="Serenity Spaces",
    contact_email="serenity@workspaces.com",
    contact_phone="987-654-3210",
    price_per_day=30.00,
    latitude=34.0525,
    longitude=-118.2440,
    is_available=True
)

entry3 = Location(
    name="Techie's Paradise",
    address="789 Oak St, Capital City",
    description="Tech-friendly desk with all essential tools.",
    business_name="TechSpace Inc.",
    contact_email="tech@workspaces.com",
    contact_phone="555-444-3333",
    price_per_day=35.00,
    latitude=34.0530,
    longitude=-118.2450,
    is_available=False
)

entry4 = Location(
    name="Zen Corner",
    address="101 Pine St, Ogdenville",
    description="Minimalistic workspace for focused work.",
    business_name="ZenWork Co.",
    contact_email="zen@workspaces.com",
    contact_phone="222-333-4444",
    price_per_day=20.00,
    latitude=34.0540,
    longitude=-118.2460,
    is_available=True
)

entry5 = Location(
    name="Business Suite",
    address="202 Birch St, North Haverbrook",
    description="Elegant desk for professionals.",
    business_name="BusinessDesk Ltd.",
    contact_email="business@workspaces.com",
    contact_phone="666-777-8888",
    price_per_day=40.00,
    latitude=34.0550,
    longitude=-118.2470,
    is_available=False
)

db.session.add_all([entry1, entry2, entry3, entry4, entry5])

db.session.commit()
