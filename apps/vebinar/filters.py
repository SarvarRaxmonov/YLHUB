import django_filters

from apps.vebinar.choices import VEBINARType
from apps.vebinar.models import UserSearchVebinar, Vebinar


class VebinarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", method="name_filter")
    type = django_filters.ChoiceFilter(choices=VEBINARType.choices)

    class Meta:
        model = Vebinar
        fields = ("name", "type")

    def name_filter(self, queryset, name, value):
        if value:
            UserSearchVebinar.objects.get_or_create(keyword=value, user=self.request.user)
        return queryset.filter(name__icontains=value)
