from django.contrib.auth.models import User
from accounts.models import CustomUser
from faker import Faker


def run():
    data = []
    for i in range(1, 2):
        faker = Faker()
        data.append({
            'username': faker.user_name(),
            'password': '123456789',
            'name': faker.name()

        })
    print(data)
    CustomUser.objects.bulk_create([
        CustomUser(**d) for d in data
    ])
    # CustomUser.objects.create({'username': 'kalim', 'password': 'kalim', 'name': 'kalimli'})
