from the_music_tree_api_kit.filtering.set.private_unique_resource.PrivateUniqueResourceFilterSet import (
    PrivateUniqueResourceFilterSet,
)

from hear.model.play.Play import Play


class PlayFilterSet(PrivateUniqueResourceFilterSet):
    class Meta:
        model = Play
        fields = [*PrivateUniqueResourceFilterSet.get_date_fields()]
