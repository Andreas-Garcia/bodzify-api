from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from the_music_tree_api_kit.view.viewset.model.AppModelViewSet import AppModelViewSet
from the_music_tree_genre_kit.criteria.CriteriaTreeName import CriteriaTreeName
from the_music_tree_genre_kit.criteria.Fields import Fields as FilterFields
from the_music_tree_genre_kit.filtering.set.criteria_playlist.CriteriaPlaylistFilterSet import CriteriaPlaylistFilterSet
from the_music_tree_genre_kit.view.viewset.playlist.PlaylistTracksActionMixin import PlaylistTracksActionMixin

from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist
from hear.serializer.model.playlist.children.criteria.output.detailed import CriteriaPlaylistDetailedSerializer
from hear.serializer.model.playlist.children.criteria.output.simple import CriteriaPlaylistSimpleSerializer
from hear.serializer.model.track_playlist_rel.output.in_page import TrackPlaylistRelInPageSerializer


class CriteriaPlaylistViewSet(PlaylistTracksActionMixin, AppModelViewSet[CriteriaPlaylist]):
    track_playlist_rel_serializer_class = TrackPlaylistRelInPageSerializer

    def __init__(self, model_class, **kwargs):
        super().__init__(
            service=None,
            model_class=model_class if model_class else CriteriaPlaylist,
            filterset_class=CriteriaPlaylistFilterSet,
            simple_serializer_class=CriteriaPlaylistSimpleSerializer,
            detailed_serializer_class=CriteriaPlaylistDetailedSerializer,
            **kwargs,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(name=FilterFields.NAME_PUBLIC, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
            OpenApiParameter(name=FilterFields.PARENT, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
            OpenApiParameter(
                name=FilterFields.TREE_NAME,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=CriteriaTreeName.values,
                description="Genreless/Tagless playlists are listed under canonical.",
            ),
        ]
    )
    def list(self, *args, **kwargs):
        return self._handle_list()

    def retrieve(self, *args, **kwargs):
        return self._handle_retrieve()
