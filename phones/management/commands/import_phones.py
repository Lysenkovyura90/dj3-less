import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

            for phone in phones:
                # TODO: Добавьте сохранение модели
                print(phone)

                new_phone = Phone.objects.create(
                    id=int(phone["id"]), name=phone["name"],
                    image=phone["image"], price=int(phone["price"]),
                    release_date=phone["release_date"],
                    lte_exist=phone["lte_exists"],
                    slug=slugify(phone["name"]),
                )