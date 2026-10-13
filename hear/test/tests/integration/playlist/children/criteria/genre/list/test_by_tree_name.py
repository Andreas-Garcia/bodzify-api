from rest_framework import status
from the_music_tree_genre_kit.criteria.CriteriaTreeName import CriteriaTreeName
from the_music_tree_genre_kit.criteria.Fields import Fields as FilterFields

from hear.model.playlist.children.criteria.genre.GenrePlaylist import GenrePlaylist
from hear.serializer.model.playlist.children.criteria.output.detailed import Fields as RietrieveFields
from hear.test.tests.integration.playlist.children.criteria.genre.GenrePlaylistTestCase import GenrePlaylistTestCase


class TestCase(GenrePlaylistTestCase):
    def setUp(self):
        super().setUp()
        self.genre_rock = self.model_fixture_factory.create_genre(name="Rock")
        self.genre_italian_prog = self.model_fixture_factory.create_genre(
            name="Italian progressive rock", tree_name=CriteriaTreeName.REGIONAL
        )
        self.genreless_playlist = GenrePlaylist.objects.get(user=self.test_user1, criteria=None)

    def _result_names(self):
        return {result[RietrieveFields.NAME] for result in self.results}

    def test_canonical_then_canonical_tree_and_genreless(self):
        response = self._list_genre_playlists(**{FilterFields.TREE_NAME: CriteriaTreeName.CANONICAL})

        assert response.status_code == status.HTTP_200_OK
        assert self._result_names() == {self.genre_rock.name, self.genreless_playlist.name}

    def test_regional_then_only_regional_tree(self):
        response = self._list_genre_playlists(**{FilterFields.TREE_NAME: CriteriaTreeName.REGIONAL})

        assert response.status_code == status.HTTP_200_OK
        assert self._result_names() == {self.genre_italian_prog.name}

    def test_invalid_tree_name_then_400_bad_request(self):
        response = self._list_genre_playlists(**{FilterFields.TREE_NAME: "bogus"})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
