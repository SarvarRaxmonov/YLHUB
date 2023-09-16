from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from apps.student_test.models import Test, TestQuestion


@receiver(post_save, sender=Test)
def add_questions_to_new_created_test_signal(sender, instance, created, **kwargs):
    if created:
        update_test_questions_relationship(instance, question_count=instance.questions)
    return instance


@receiver(pre_save, sender=Test)
def add_questions_to_updated_test_signal(sender, instance, **kwargs):
    try:
        old_questions = Test.objects.get(id=instance.id).questions
        if instance.questions > old_questions:
            question_count_difference = instance.questions - old_questions
            update_test_questions_relationship(instance, question_count=question_count_difference)
        else:
            question_count_difference = old_questions - instance.questions
            remove_test_question_relationship(instance, question_count=question_count_difference)
    except instance.DoesNotExist:
        return instance


@receiver(pre_save, sender=TestQuestion)
def test_question_update_signal(sender, instance, **kwargs):
    try:
        old_test_question = TestQuestion.objects.get(id=instance.id)
        if old_test_question.test != instance.test:
            obj = Test.objects.get(id=old_test_question.test.id)
            obj.questions -= 1
            Test.objects.bulk_update([obj], ["questions"])
            obj_2 = Test.objects.get(id=instance.test.id)
            obj_2.questions += 1
            Test.objects.bulk_update([obj_2], ["questions"])
    except Exception:
        pass


@receiver(pre_delete, sender=TestQuestion)
def test_question_delete_signal(sender, instance, **kwargs):
    try:
        if instance:
            obj = Test.objects.get(id=instance.test.id)
            obj.questions -= 1
            Test.objects.bulk_update([obj], ["questions"])
    except Exception:
        pass


def update_test_questions_relationship(instance=None, question_count=0):
    test_questions_to_update = TestQuestion.objects.filter(subject=instance.subject.id, test__isnull=True).order_by("?")
    if test_questions_to_update and instance and test_questions_to_update.count() >= question_count:
        updated_test_questions = [TestQuestion(id=test_question.id, test=instance) for test_question in test_questions_to_update[:question_count]]
        TestQuestion.objects.bulk_update(updated_test_questions, ["test"])


def remove_test_question_relationship(instance=None, question_count=0):
    test_questions_to_update = TestQuestion.objects.filter(subject=instance.subject.id, test=instance)
    if test_questions_to_update.count() >= question_count:
        updated_test_questions = [TestQuestion(id=test_question.id, test=None) for test_question in test_questions_to_update[:question_count]]
        TestQuestion.objects.bulk_update(updated_test_questions, ["test"])
