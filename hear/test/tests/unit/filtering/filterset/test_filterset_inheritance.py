from datetime import timedelta

from django.utils import timezone
from django_filters import FilterSet
from the_music_tree_api_kit.filtering.set.private_unique_resource.Fields import Fields as PrivateUniqueResourceFields
from the_music_tree_genre_kit.filtering.set.criteria.CriteriaFilterSet import CriteriaFilterSet
from the_music_tree_genre_kit.filtering.set.criteria_playlist.CriteriaPlaylistFilterSet import CriteriaPlaylistFilterSet
from the_music_tree_genre_kit.filtering.set.manual_playlist.ManualPlaylistFilterSet import ManualPlaylistFilterSet
from the_music_tree_genre_kit.filtering.set.playlist.PlaylistFilterSet import PlaylistFilterSet
from the_music_tree_genre_kit.playlist.Playlist import Playlist

from hear.filtering.set.album.AlbumFilterSet import AlbumFilterSet
from hear.filtering.set.artist.ArtistFilterSet import ArtistFilterSet
from hear.filtering.set.play.PlayFilterSet import PlayFilterSet
from hear.filtering.set.uploaded_track.UploadedTrackFilterSet import UploadedTrackFilterSet
from hear.model.criteria.Criteria import Criteria
from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist
from hear.model.playlist.children.manual.ManualPlaylist import ManualPlaylist
from hear.test.utils.AppTestCase import AppTestCase


class TestFilterInheritance(AppTestCase):
    def setUp(self):
        super().setUp()
        self.expected_filters = {
            PrivateUniqueResourceFields.CREATED_ON,
            PrivateUniqueResourceFields.CREATED_ON_GT,
            PrivateUniqueResourceFields.CREATED_ON_LT,
            PrivateUniqueResourceFields.CREATED_ON_GTE,
            PrivateUniqueResourceFields.CREATED_ON_LTE,
            PrivateUniqueResourceFields.UPDATED_ON,
            PrivateUniqueResourceFields.UPDATED_ON_GT,
            PrivateUniqueResourceFields.UPDATED_ON_LT,
            PrivateUniqueResourceFields.UPDATED_ON_GTE,
            PrivateUniqueResourceFields.UPDATED_ON_LTE,
        }

    def assert_datetime_inherited_filters(self, filterset_class, model=None):
        model = model or filterset_class.Meta.model
        filterset: FilterSet = filterset_class(queryset=model.objects.all())
        available_filters = set(filterset.filters.keys())
        inherited_filters = self.expected_filters & available_filters
        assert inherited_filters == self.expected_filters, (
            f"{filterset_class.__name__} is missing some datetime filters. "
            f"Missing: {self.expected_filters - inherited_filters}"
        )

        for filter_name in self.expected_filters:
            assert filter_name in filterset.filters, f"{filterset_class.__name__} is missing filter: {filter_name}"
            assert hasattr(filterset.filters[filter_name], "filter"), (
                f"{filterset_class.__name__}'s {filter_name} filter is not callable"
            )

        # Check if datetime filters are properly defined in Meta fields
        meta_fields = getattr(filterset_class.Meta, "fields", None)
        if meta_fields != "__all__" and meta_fields is not None:
            meta_fields_set = set(meta_fields)
            # Extract base field names (without suffixes like _gt, _lt)
            base_datetime_fields = {PrivateUniqueResourceFields.CREATED_ON, PrivateUniqueResourceFields.UPDATED_ON}
            missing_fields = base_datetime_fields - meta_fields_set
            assert not missing_fields, (
                f"{filterset_class.__name__}'s Meta.fields is missing datetime fields: {missing_fields}"
            )

    def test_album_filter_inheritance(self):
        self.assert_datetime_inherited_filters(AlbumFilterSet)

    def test_artist_filter_inheritance(self):
        self.assert_datetime_inherited_filters(ArtistFilterSet)

    def test_uploaded_track_filter_inheritance(self):
        self.assert_datetime_inherited_filters(UploadedTrackFilterSet)

    def test_criteria_filter_inheritance(self):
        self.assert_datetime_inherited_filters(CriteriaFilterSet, Criteria)

    def test_base_playlist_filter_inheritance(self):
        self.assert_datetime_inherited_filters(PlaylistFilterSet, Playlist)

    def test_manual_playlist_filter_inheritance(self):
        self.assert_datetime_inherited_filters(ManualPlaylistFilterSet, ManualPlaylist)

    def test_criteria_playlist_filter_inheritance(self):
        self.assert_datetime_inherited_filters(CriteriaPlaylistFilterSet, CriteriaPlaylist)

    def test_play_filter_inheritance(self):
        self.assert_datetime_inherited_filters(PlayFilterSet)

    def test_filter_functionality_using_a_concrete_model(self):
        now = timezone.now()

        past = now - timedelta(days=5)
        future = now + timedelta(days=5)

        past_record = self.model_fixture_factory.create_genre(name="Past Criteria", created_on=past, updated_on=past)
        present_record = self.model_fixture_factory.create_genre(
            name="Present Criteria", created_on=now, updated_on=now
        )

        future_record = self.model_fixture_factory.create_genre(
            name="Future Criteria", created_on=future, updated_on=future
        )

        filterset = CriteriaFilterSet(
            {PrivateUniqueResourceFields.CREATED_ON: now.isoformat()},
            queryset=Criteria.objects.all(),
        )

        assert [record.pk for record in filterset.qs] == [present_record.pk]

        filterset = CriteriaFilterSet(
            {PrivateUniqueResourceFields.CREATED_ON_GT: now.isoformat()},
            queryset=Criteria.objects.all(),
        )

        assert [record.pk for record in filterset.qs] == [future_record.pk]

        filterset = CriteriaFilterSet(
            {PrivateUniqueResourceFields.CREATED_ON_LT: now.isoformat()},
            queryset=Criteria.objects.all(),
        )

        assert [record.pk for record in filterset.qs] == [past_record.pk]

        filterset = CriteriaFilterSet(
            {
                PrivateUniqueResourceFields.CREATED_ON_GTE: past.isoformat(),
                PrivateUniqueResourceFields.CREATED_ON_LTE: now.isoformat(),
            },
            queryset=Criteria.objects.all(),
        )

        assert {record.pk for record in filterset.qs} == {past_record.pk, present_record.pk}
