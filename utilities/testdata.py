""" Test case data """
from faker import Faker


class TestData:
    """
    Fake data used for testing
    """
    faker = Faker(['pt_BR'])
    url = "https://worldofwarcraft.blizzard.com/en-us/start"
    dob_day = '01'
    dob_mon = '01'
    dob_year = '1970'
    user_first_name = faker.name()
    user_last_name = faker.last_name()
    user_email = faker.email()
    user_phone = faker.phone_number()
