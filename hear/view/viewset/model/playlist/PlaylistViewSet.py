from drf_spectacular.utils import (
    OpenApiParameter,  # type: ignore
    OpenApiTypes,
    extend_schema,
)
from the_music_tree_api_kit.view.viewset.model.AppModelViewSet import AppModelViewSet
from the_music_tree_genre_kit.filtering.set.playlist.PlaylistFilterSet import PlaylistFilterSet
from the_music_tree_genre_kit.playlist.Fields import Fields as QueryParamsFields
from the_music_tree_genre_kit.playlist.Playlist import Playlist
from the_music_tree_genre_kit.view.viewset.playlist.PlaylistTracksActionMixin import PlaylistTracksActionMixin

from hear.serializer.model.playlist.base.output.detailed import PlaylistDetailedSerializer
from hear.serializer.model.playlist.base.output.simple import PlaylistSimpleSerializer
from hear.serializer.model.track_playlist_rel.output.in_page import TrackPlaylistRelInPageSerializer


class PlaylistViewSet(PlaylistTracksActionMixin, AppModelViewSet[Playlist]):
    track_playlist_rel_serializer_class = TrackPlaylistRelInPageSerializer

    def __init__(self, **kwargs):
        super().__init__(
            model_class=Playlist,
            filterset_class=PlaylistFilterSet,
            simple_serializer_class=PlaylistSimpleSerializer,
            detailed_serializer_class=PlaylistDetailedSerializer,
            **kwargs,
        )

    @staticmethod
    def _get_queryset_str_filter_value_to_filter_nothing():
        return ""

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name=QueryParamsFields.NAME_PUBLIC, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name=QueryParamsFields.TYPE_LABEL_INTERNAL, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY
            ),
        ]
    )
    def list(self, *args, **kwargs):
        return self._handle_list()

    def retrieve(self, *args, **kwargs):
        return self._handle_retrieve()
