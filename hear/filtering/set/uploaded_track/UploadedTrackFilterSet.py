from django_filters import CharFilter
from the_music_tree_api_kit.filtering.filter.char.EmptiableCharFilter import EmptiableCharFilter
from the_music_tree_api_kit.filtering.filter.char.RelatedObjectCharFilter import RelatedObjectCharFilter
from the_music_tree_api_kit.filtering.set.private_unique_resource.PrivateUniqueResourceFilterSet import (
    PrivateUniqueResourceFilterSet,
)

from hear.model.album.Fields import Fields as AlbumFields
from hear.model.artist.Fields import Fields as ArtistFields
from hear.model.criteria.Criteria import Fields as CriteriaFields
from hear.model.uploaded_track.UploadedTrack import UploadedTrack
from hear.model.uploaded_track.UploadedTrackFieldKey import UploadedTrackFieldKey as ModelFields

from .UploadedTrackFilterFieldKey import UploadedTrackFilterFieldKey


class UploadedTrackFilterSet(PrivateUniqueResourceFilterSet):
    title = CharFilter(field_name=ModelFields.TITLE.value, lookup_expr="icontains")
    artists_name = RelatedObjectCharFilter(
        primary_field=ArtistFields.NAME_INTERNAL,
        field_name=ModelFields.ARTISTS.value,
        field_name_public=UploadedTrackFilterFieldKey.ARTISTS_NAME.value,
        lookup_expr="icontains",
    )

    album_name = RelatedObjectCharFilter(
        primary_field=AlbumFields.NAME_INTERNAL,
        field_name=ModelFields.ALBUM.value,
        field_name_public=UploadedTrackFilterFieldKey.ALBUM_NAME.value,
        lookup_expr="icontains",
    )

    genre_name = RelatedObjectCharFilter(
        primary_field=CriteriaFields.NAME_INTERNAL,
        field_name=ModelFields.GENRE.value,
        field_name_public=UploadedTrackFilterFieldKey.GENRE_NAME.value,
        lookup_expr="icontains",
    )
    language = EmptiableCharFilter(
        field_name_public=ModelFields.LANGUAGE.value, field_name=ModelFields.LANGUAGE.value, lookup_expr="icontains"
    )

    class Meta:
        model = UploadedTrack
        fields = [
            UploadedTrackFilterFieldKey.TITLE.value,
            UploadedTrackFilterFieldKey.LANGUAGE.value,
            *PrivateUniqueResourceFilterSet.get_date_fields(),
        ]
