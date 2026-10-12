from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from the_music_tree_api_kit.view.viewset.model.AppModelViewSet import AppModelViewSet
from the_music_tree_genre_kit.filtering.set.manual_playlist.ManualPlaylistFilterSet import ManualPlaylistFilterSet
from the_music_tree_genre_kit.manual_playlist.Fields import Fields
from the_music_tree_genre_kit.view.viewset.playlist.PlaylistTracksActionMixin import PlaylistTracksActionMixin

from hear.model.playlist.children.manual.ManualPlaylist import ManualPlaylist
from hear.serializer.model.playlist.children.manual.input.input import ManualPlaylistInputSerializer
from hear.serializer.model.playlist.children.manual.input.post import ManualPlaylistPostSerializer
from hear.serializer.model.playlist.children.manual.input.put import ManualPlaylistPutSerializer
from hear.serializer.model.playlist.children.manual.output.detailed import ManualPlaylistDetailedSerializer
from hear.serializer.model.playlist.children.manual.output.simple import ManualPlaylistSimpleSerializer
from hear.serializer.model.track_playlist_rel.output.in_page import TrackPlaylistRelInPageSerializer


class ManualPlaylistViewSet(PlaylistTracksActionMixin, AppModelViewSet[ManualPlaylist]):
    track_playlist_rel_serializer_class = TrackPlaylistRelInPageSerializer

    def __init__(self, **kwargs):
        super().__init__(
            model_class=ManualPlaylist,
            filterset_class=ManualPlaylistFilterSet,
            simple_serializer_class=ManualPlaylistSimpleSerializer,
            detailed_serializer_class=ManualPlaylistDetailedSerializer,
            create_serializer_class=ManualPlaylistPostSerializer,
            update_serializer_class=ManualPlaylistPutSerializer,
            **kwargs,
        )

    # @transaction.atomic not needed
    @extend_schema(request=ManualPlaylistInputSerializer, responses=ManualPlaylistDetailedSerializer)
    def create(self, request, *args, **kwargs):
        return self._handle_post(request)

    @extend_schema(
        parameters=[
            OpenApiParameter(name=Fields.NAME_PUBLIC, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        ]
    )
    def list(self, *args, **kwargs):
        return self._handle_list()

    def retrieve(self, *args, **kwargs):
        return self._handle_retrieve()

    # @transaction.atomic not needed
    @extend_schema(request=ManualPlaylistInputSerializer, responses=ManualPlaylistDetailedSerializer)
    def update(self, request, *args, **kwargs):
        return self._handle_update(request)
