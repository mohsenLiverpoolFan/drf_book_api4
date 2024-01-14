from todo.models import Todo
from faker import Faker


def run():
    data = []
    for i in range(1, 20):
        faker = Faker()
        data.append({
            'title': faker.name(),
            'body': faker.text()
        })
    Todo.objects.bulk_create([
        Todo(**d) for d in data
    ])
