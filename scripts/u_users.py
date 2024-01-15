from django.contrib.auth.models import User
from accounts.models import CustomUser
from faker import Faker


def run():
    # customers_id = CustomUser.objects.all().values_list('id', flat=True)
    # for i in customers_id:
    #     CustomUser.objects.get(id=i).delete()
    CustomUser.objects.all().update('password', 'Zaq12wsxcde3')
