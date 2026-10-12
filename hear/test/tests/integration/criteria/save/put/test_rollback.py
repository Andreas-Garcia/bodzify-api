from unittest.mock import patch

from rest_framework import status

from hear.model.criteria.children.genre.Genre import Genre
from hear.test.tests.integration.criteria.GenreTestCase import GenreTestCase


class TestCase(GenreTestCase):
    def test_exception_then_rollback(self):
        genre_rock = self.model_fixture_factory.create_genre(name="Rock")
        genre_punk = self.model_fixture_factory.create_genre(name="Punk", parent=genre_rock)
        genre_metal = self.model_fixture_factory.create_genre(name="Metal")

        with patch(
            "the_music_tree_genre_kit.criteria.AbstractCriteriaManager.AbstractCriteriaManager._on_parent_changed"
        ) as mock:
            exception_message = "Save failed!"
            mock.side_effect = Exception(exception_message)

            response = self._put_genre(uuid=genre_punk.uuid, parent=genre_metal.uuid)
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            genre: Genre = Genre.objects.get(user=self.test_user1, uuid=genre_punk.uuid)
            assert genre.parent.pk == genre_rock.pk
