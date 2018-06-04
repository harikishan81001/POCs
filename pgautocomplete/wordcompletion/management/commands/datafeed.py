import random

from django.core.management.base import BaseCommand, CommandError

from wordcompletion.models import Warehouses

from faker import Faker


faker = Faker('en_US')


CENTERS = [faker.bban() for e in range(1, 100)]
SELLERS = [faker.ssn() for e in range(1, 10)]
STATES = [True, False]


class Command(BaseCommand):
    help = 'Feeds data polling it from third party catalog'

    def get_data_feed(self):
        data = {}
        data["name"] = faker.name()
        data["registered_name"] = faker.name()
        data["address"] = {
            "address": faker.address(),
            "phone_number": faker.phone_number()
        }
        data["pin_code"] = faker.postalcode()
        data["seller_id"] = random.choice(SELLERS)
        data["active"] = random.choice(STATES)
        data["incoming_center"] = random.choice(CENTERS)
        data["rto_center"] = random.choice(CENTERS)
        data["dto_center"] = random.choice(CENTERS)
        return data

    def add_arguments(self, parser):
        parser.add_argument('--count', dest="count", type=int)

    def handle(self, *args, **options):
        """
        Perform action
        """
        count = options.get("count", 1)
        self.stdout.write("=" * 50)
        self.stdout.write(
            self.style.SUCCESS('Loading data for count={}'.format(count)))
        self.stdout.write("=" * 50)
        self.stdout.write("\n")

        dataList = []

        for i in xrange(0, count):
            data = self.get_data_feed()
            dataList.append(Warehouses(**data))

            if len(dataList) % 100 == 0:
                Warehouses.objects.bulk_create(dataList)
                dataList = []
                percent = float(float(i+1)/float(count)) * 100
                self.stdout.write(
                    self.style.SUCCESS("{}% Completed !".format(percent)),
                    ending='\r')
                self.stdout.flush()

        if len(dataList) > 0:
            Warehouses.objects.bulk_create(dataList)
            dataList = []

        self.stdout.write("\n")
        self.stdout.write("=" * 50)
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully loaded data count={}'.format(count)))
        self.stdout.write("=" * 50)
