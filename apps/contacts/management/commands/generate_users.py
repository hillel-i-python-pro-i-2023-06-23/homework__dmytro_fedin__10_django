from django.core.management.base import BaseCommand


class GenerateUsers(BaseCommand):
    help = "Generate users"

    # Get parser for command args
    def add_arguments(self, parser):
        parser.add_argument(
            "amount",
            type=int,
            help="Number of users to generate",
            default=20,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        print(f"amount: {amount}")
