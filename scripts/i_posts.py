from posts.models import Post
from faker import Faker
from accounts.models import CustomUser
import random


def run():
    data = []
    accounts_id = CustomUser.objects.all().values_list('id', flat=True)
    for i in range(1, 25):
        faker = Faker()
        data.append({
            'title': faker.name(),
            'body': faker.text(),
            'author': CustomUser.objects.get(id=random.choice(accounts_id))

        })
    Post.objects.bulk_create([
        Post(**d) for d in data
    ])
