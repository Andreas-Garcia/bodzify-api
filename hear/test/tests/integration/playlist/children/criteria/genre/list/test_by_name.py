from rest_framework import status
from the_music_tree_api_kit.exception.validation.FieldValidationErrorCode import FieldValidationErrorCode
from the_music_tree_genre_kit.playlist.Fields import Fields as FilterFields

from hear.model.playlist.children.criteria.genre.GenrePlaylist import GenrePlaylist
from hear.serializer.model.playlist.children.criteria.output.detailed import Fields as RietrieveFields
from hear.test.tests.integration.playlist.children.criteria.genre.GenrePlaylistTestCase import GenrePlaylistTestCase
from hear.test.utils.field.filter.char.NotNullableFreeCharFilterTestCase import NotNullableFreeCharFilterTestCase


class TestCase(GenrePlaylistTestCase, NotNullableFreeCharFilterTestCase):
    def test_empty_then_400_bad_request(self):
        self.model_fixture_factory.create_genre(name="Rock")

        response = self._list_genre_playlists(**{FilterFields.NAME_PUBLIC: ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert self.bad_request_result_field_errors[0]["field"] == FilterFields.NAME_PUBLIC
        assert self.bad_request_result_field_errors[0]["code"] == FieldValidationErrorCode.BLANK

    def test_tag_playlists_then_not_in_results(self):
        tag = self.model_fixture_factory.create_tag(name="foot")
        genre = self.model_fixture_factory.create_genre(name="foot rock")

        response = self._list_genre_playlists(**{FilterFields.NAME_PUBLIC: "foot"})

        assert response.status_code == status.HTTP_200_OK
        assert self.results_overall_total == 1
        result_names = [result[RietrieveFields.NAME] for result in self.results]
        assert genre.name in result_names
        assert tag.name not in result_names

    def test_contains_in_another_case_then_results(self):
        criteria1 = self.model_fixture_factory.create_genre(name="Rock")
        criteria2 = self.model_fixture_factory.create_genre(name="Rockabilly")
        self.model_fixture_factory.create_genre(name="Punk")

        response = self._list_genre_playlists(**{FilterFields.NAME_PUBLIC: "RO"})

        assert response.status_code == status.HTTP_200_OK
        assert self.results_overall_total == 2
        result_names = [result[RietrieveFields.NAME] for result in self.results]
        assert criteria1.name in result_names
        assert criteria2.name in result_names

    def test_not_provided_then_results(self):
        criteria1 = self.model_fixture_factory.create_genre(name="Rock")
        criteria2 = self.model_fixture_factory.create_genre(name="Rockabilly")
        criteria3 = self.model_fixture_factory.create_genre(name="Punk")

        response = self._list_genre_playlists()

        assert response.status_code == status.HTTP_200_OK
        assert self.results_overall_total == 4
        result_names = [result[RietrieveFields.NAME] for result in self.results]
        assert criteria1.name in result_names
        assert criteria2.name in result_names
        assert criteria3.name in result_names

    def test_name_in_genreless_and_criteria_name_then_results(self):
        genre_genre = self.model_fixture_factory.create_genre(name="genre")
        genre_rock = self.model_fixture_factory.create_genre(name="Rock")

        response = self._list_genre_playlists(**{FilterFields.NAME_PUBLIC: "geN"})

        assert response.status_code == status.HTTP_200_OK
        assert self.results_overall_total == 2
        result_names = [result[RietrieveFields.NAME] for result in self.results]
        assert genre_genre.name in result_names
        assert genre_rock.name not in result_names
        genreless_playlist: GenrePlaylist = GenrePlaylist.objects.get(user=self.test_user1, criteria=None)
        assert genreless_playlist.name in result_names
