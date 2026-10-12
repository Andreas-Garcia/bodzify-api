from django.core.exceptions import ImproperlyConfigured
from rest_framework import serializers
from the_music_tree_api_kit.serializer.EagerLoadingMixin import EagerLoadingMixin

from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist
from hear.model.playlist.PlaylistUploadedTracks import UPLOADED_TRACKS_COUNT_ANNOTATED, uploaded_tracks_count_annotation
from hear.serializer.model.criteria.output.simple import CriteriaSimpleSerializer
from hear.serializer.model.playlist.children.criteria.output.Fields import Fields as AvailableFields
from hear.serializer.model.playlist.children.criteria.output.minumum import CriteriaPlaylistMinimumSerializer


class Fields:
    UUID = AvailableFields.UUID
    NAME = AvailableFields.NAME
    UPLOADED_TRACKS_NOT_ARCHIVED_COUNT_PUBLIC = AvailableFields.UPLOADED_TRACKS_NOT_ARCHIVED_COUNT_PUBLIC
    DURATION_STR_IN_HOUR_MIN_SEC = AvailableFields.DURATION_STR_IN_HOUR_MIN_SEC
    CRITERIA = AvailableFields.CRITERIA
    PARENT = AvailableFields.PARENT
    ROOT = AvailableFields.ROOT
    CREATED_ON = AvailableFields.CREATED_ON
    UPDATED_ON = AvailableFields.UPDATED_ON


class CriteriaPlaylistSimpleSerializer(EagerLoadingMixin, serializers.ModelSerializer):
    criteria = CriteriaSimpleSerializer()
    parent = CriteriaPlaylistMinimumSerializer()
    root = CriteriaPlaylistMinimumSerializer()  # type: ignore
    uploaded_tracks_count = serializers.IntegerField(source=UPLOADED_TRACKS_COUNT_ANNOTATED)

    @classmethod
    def setup_queryset(cls, queryset, prefix=""):  # noqa: ARG003 - annotations only apply to the top-level queryset
        queryset = queryset.select_related(
            Fields.CRITERIA,
            f"{Fields.CRITERIA}__{Fields.PARENT}__criteria_playlist",
            f"{Fields.CRITERIA}__{Fields.ROOT}__criteria_playlist",
        ).annotate(**{UPLOADED_TRACKS_COUNT_ANNOTATED: uploaded_tracks_count_annotation(archived=False)})
        for nested in (Fields.PARENT, Fields.ROOT):
            queryset = CriteriaPlaylistMinimumSerializer.setup_queryset(
                queryset, prefix=f"{Fields.CRITERIA}__{nested}__criteria_playlist__"
            )
        return CriteriaSimpleSerializer.setup_queryset(queryset, prefix=f"{Fields.CRITERIA}__")

    def to_representation(self, instance):
        if not isinstance(instance, CriteriaPlaylist):
            raise ImproperlyConfigured("Invalid instance type")
        return super().to_representation(instance)

    class Meta:
        model = CriteriaPlaylist
        fields = [
            Fields.UUID,
            Fields.NAME,
            Fields.CRITERIA,
            Fields.PARENT,
            Fields.ROOT,
            Fields.UPLOADED_TRACKS_NOT_ARCHIVED_COUNT_PUBLIC,
            Fields.CREATED_ON,
            Fields.UPDATED_ON,
        ]
