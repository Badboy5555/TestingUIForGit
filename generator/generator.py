from data.data import Person
from faker import Faker


Fake = Faker('en_US')
Faker.seed()

def generate_data():
    yield Person(
    FULL_NAME = Fake.first_name() + ' ' + Fake.last_name(),
    EMAIL = Fake.email(),
    CURRENT_ADDRESS = Fake.address(),
    PERMANENT_ADDRESS = Fake.address()
    )