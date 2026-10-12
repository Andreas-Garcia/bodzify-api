from rest_framework import serializers
from the_music_tree_api_kit.serializer.EagerLoadingMixin import EagerLoadingMixin

from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist
from hear.model.playlist.PlaylistDuration import format_duration_in_hour_min_sec
from hear.model.playlist.PlaylistUploadedTracks import (
    DURATION_IN_SEC_ANNOTATED,
    UPLOADED_TRACKS_ARCHIVED_COUNT_ANNOTATED,
    UPLOADED_TRACKS_COUNT_ANNOTATED,
)
from hear.serializer.model.criteria.output.minimum import CriteriaMinimumSerializer
from hear.serializer.model.playlist.base.output.detailed import annotate_counts_and_duration
from hear.serializer.model.playlist.children.criteria.output.minumum import CriteriaPlaylistMinimumSerializer

from .Fields import Fields


class CriteriaPlaylistDetailedSerializer(EagerLoadingMixin, serializers.ModelSerializer):
    uploaded_tracks_count = serializers.IntegerField(source=UPLOADED_TRACKS_COUNT_ANNOTATED)
    uploaded_tracks_archived_count = serializers.IntegerField(source=UPLOADED_TRACKS_ARCHIVED_COUNT_ANNOTATED)
    criteria = CriteriaMinimumSerializer()
    root = CriteriaPlaylistMinimumSerializer()  # type: ignore
    parent = CriteriaPlaylistMinimumSerializer()
    duration_in_sec = serializers.IntegerField(source=DURATION_IN_SEC_ANNOTATED)
    duration_str_in_hour_min_sec = serializers.SerializerMethodField()

    @classmethod
    def setup_queryset(cls, queryset, prefix=""):  # noqa: ARG003 - annotations only apply to the top-level queryset
        return annotate_counts_and_duration(queryset).select_related(
            Fields.CRITERIA,
            f"{Fields.CRITERIA}__{Fields.PARENT}__criteria_playlist",
            f"{Fields.CRITERIA}__{Fields.ROOT}__criteria_playlist",
        )

    class Meta:
        model = CriteriaPlaylist
        fields = [
            Fields.UUID,
            Fields.NAME,
            Fields.UPLOADED_TRACKS_NOT_ARCHIVED_COUNT_PUBLIC,
            Fields.DURATION_IN_SEC,
            Fields.DURATION_STR_IN_HOUR_MIN_SEC,
            Fields.UPLOADED_TRACKS_ARCHIVED_COUNT_PUBLIC,
            Fields.CRITERIA,
            Fields.PARENT,
            Fields.ROOT,
            Fields.CREATED_ON,
            Fields.UPDATED_ON,
        ]

    def get_duration_str_in_hour_min_sec(self, obj: CriteriaPlaylist) -> str:
        return format_duration_in_hour_min_sec(getattr(obj, DURATION_IN_SEC_ANNOTATED))
