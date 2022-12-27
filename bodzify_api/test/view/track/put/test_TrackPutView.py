from rest_framework import status

from bodzify_api.test.view.track.TrackViewTestCase import TrackViewTestCase
from bodzify_api.model.track.LibraryTrack import LibraryTrack


class TrackPutViewTestCase(TrackViewTestCase):

    fixtures = ['initial_data', 'TestUserData', 'TestViewTrackPutData']

    def setUp(self) -> None:
        obj= super().setUp("test/view/track/put/sample/")
        self.copySamplesToTestUserLibrary()
        return obj

    def test_libraryTrackPut(self):
        self.login(self.testUser)

        # On a mp3 file
        data = {
            "title": "Somewhere I Belong",
            "artist": "Linkin Park",
            "album": "Meteora",
            "genre": "Lsjdqoiqsicqjsof885fgion",
            "rating": 200,
            "language": "English"
        }

        response = self.putSampleTrack(trackUuid="36nS4LVDssLh4BvTARbJEK", data=data)
        assert response.status_code == status.HTTP_200_OK

        track = LibraryTrack.objects.get(title="Somewhere I Belong")
        assert track.artist == "Linkin Park"
        assert track.album == "Meteora"
        assert track.genre.name == "Nu metal"
        assert track.rating == 200
        assert track.language == "English"

        # On a FLAC file
        data = {
            "title": "Give Me Novocain",
            "artist": "Green Day",
            "album": "American Idiot",
            "genre": "LsjdqoifsjofsiEjf885fgion",  
            "rating": 0,
            "language": "English, German"
        }

        response = self.putSampleTrack(trackUuid="36nS4LVDoihoihvTARbJEK", data=data)
        assert response.status_code == status.HTTP_200_OK
                
        track = LibraryTrack.objects.get(title="Give Me Novocain")
        assert track.artist == "Green Day"
        assert track.album == "American Idiot"
        assert track.genre.name == "Rock"
        assert track.rating == 0
        assert track.language == "English, German"

        # On a wav file
        data = {
            "title": "Bohemian Raphsody",
            "artist": "Queen",
            "album": "A Night A the Opera",
            "genre": "Lsjdqoiqsicqjsof885fgion",
            "rating": 2,
            "language": "French"
        }

        response = self.putSampleTrack(trackUuid="dyFYZTP3anyaUBcLYVHJ3A", data=data)
        assert response.status_code == status.HTTP_200_OK
                
        track = LibraryTrack.objects.get(title="Bohemian Raphsody")
        assert track.artist == "Queen"
        assert track.album == "A Night A the Opera"
        assert track.genre.name == "Nu metal"
        assert track.rating == 2
        assert track.language == "French"
