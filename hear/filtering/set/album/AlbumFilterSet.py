from the_music_tree_api_kit.filtering.filter.char.NonEmptiableCharFilter import NonEmptiableCharFilter
from the_music_tree_api_kit.filtering.filter.char.RelatedObjectCharFilter import RelatedObjectCharFilter
from the_music_tree_api_kit.filtering.set.private_unique_resource.PrivateUniqueResourceFilterSet import (
    PrivateUniqueResourceFilterSet,
)

from hear.model.album.Album import Album
from hear.model.album.Fields import Fields as ModelFields
from hear.model.artist.Fields import Fields as ArtistModelFields

from .Fields import Fields


class AlbumFilterSet(PrivateUniqueResourceFilterSet):
    name = NonEmptiableCharFilter(
        field_name=ModelFields.NAME_INTERNAL, field_name_public=ModelFields.NAME_PUBLIC, lookup_expr="icontains"
    )
    album_artist_name = RelatedObjectCharFilter(
        primary_field=ArtistModelFields.NAME_INTERNAL,
        field_name=ModelFields.ALBUM_ARTISTS,
        field_name_public=Fields.ALBUM_ARTIST_NAME,
        lookup_expr="icontains",
    )

    class Meta:
        model = Album
        # Include both album-specific fields and base fields for dates
        fields = [Fields.NAME_PUBLIC, Fields.ALBUM_ARTIST_NAME, *PrivateUniqueResourceFilterSet.get_date_fields()]
