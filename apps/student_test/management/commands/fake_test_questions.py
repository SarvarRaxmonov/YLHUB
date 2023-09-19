from django.core.management.base import BaseCommand
from faker import Faker

from apps.student_test.models import Subject, TestQuestion


class Command(BaseCommand):
    help = "Generate fake data for TestQuestion model"

    def handle(self, *args, **kwargs):
        fake = Faker()
        subjects = Subject.objects.all()
        question_types = [choice[0] for choice in TestQuestion.QuestionType.choices]
        fake_records = []
        num_fake_records = 100

        for _ in range(num_fake_records):
            test_question = TestQuestion(
                question=fake.sentence(),
                type=fake.random_element(question_types),
                subject=fake.random_element(subjects),
            )
            fake_records.append(test_question)

        TestQuestion.objects.bulk_create(fake_records)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {num_fake_records} fake TestQuestion records."
            )
        )
