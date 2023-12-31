from django.apps import AppConfig


class StudentTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.student_test"

    def ready(self):
        import apps.student_test.signals
