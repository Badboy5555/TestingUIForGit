from data.data import Person
from faker import Faker


Fake = Faker('en_US')
Faker.seed()

def generate_data():
    yield Person(
    FULL_NAME = Fake.first_name() + ' ' + Fake.last_name(),
    EMAIL = Fake.email(),
    CURRENT_ADDRESS = Fake.address(),
    PERMANENT_ADDRESS = Fake.address(),
    FIRST_NAME = Fake.first_name(),
    LAST_NAME = Fake.last_name(),
    AGE = Fake.pyint(18,99),
    SALARY = Fake.pyint(18000,99000),
    DEPARTMENT = Fake.job()
    )