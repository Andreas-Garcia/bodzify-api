from django.db.models import Q
from django_filters import ChoiceFilter
from the_music_tree_genre_kit.criteria.CriteriaTreeName import CriteriaTreeName

from hear.filtering.filter.char.CriteriaNameFilter import CriteriaNameFilter
from hear.filtering.filter.foreign_key.ForeignKeyFilter import ForeignKeyFilter
from hear.filtering.set.private_unique_resource.PrivateUniqueResourceFilterSet import PrivateUniqueResourceFilterSet
from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist
from hear.model.playlist.children.criteria.Fields import Fields as ModelFields

from .Fields import Fields


class CriteriaPlaylistFilterSet(PrivateUniqueResourceFilterSet):
    name = CriteriaNameFilter(
        field_name=f"{ModelFields.CRITERIA}__{ModelFields.NAME}",
        field_name_public=Fields.NAME_PUBLIC,
        lookup_expr="icontains",
    )
    parent = ForeignKeyFilter(
        field_name=f"{ModelFields.CRITERIA}__{ModelFields.PARENT}__criteria_playlist",
        field_name_public=Fields.PARENT,
    )
    tree_name = ChoiceFilter(choices=CriteriaTreeName.choices, method="filter_tree_name")

    class Meta:
        model = CriteriaPlaylist
        fields = [
            Fields.NAME_PUBLIC,
            Fields.PARENT,
            Fields.TREE_NAME,
            *PrivateUniqueResourceFilterSet.get_date_fields(),
        ]

    def filter_tree_name(self, queryset, name, value):
        in_tree = Q(**{f"{ModelFields.CRITERIA}__{Fields.TREE_NAME}": value})
        if value == CriteriaTreeName.CANONICAL:
            in_tree |= Q(**{f"{ModelFields.CRITERIA}__isnull": True})
        return queryset.filter(in_tree)
