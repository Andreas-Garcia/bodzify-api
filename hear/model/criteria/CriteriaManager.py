from typing import TYPE_CHECKING, Any, TypeVar

from the_music_tree_genre_kit.criteria.AbstractCriteriaManager import AbstractCriteriaManager

if TYPE_CHECKING:
    from hear.model.uploaded_track.UploadedTrack import UploadedTrack

    from .Criteria import Criteria

T = TypeVar("T", bound="Criteria")


class CriteriaManager(AbstractCriteriaManager[T]):
    model: type[T]

    def _create_lineage_rel(self, *, user: Any, descendant: T, ascendant: T, degree: int) -> None:
        from hear.model.criteria.lineage_rel.CriteriaLineageRel import CriteriaLineageRel

        CriteriaLineageRel.objects.create(user=user, descendant=descendant, ascendant=ascendant, degree=degree)

    def _on_created(self, instance: T, *, actor: Any = None) -> None:
        from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist

        CriteriaPlaylist.objects.create(user=instance.user, criteria=instance, type=instance.type)

    def _on_bulk_created(self, instances: list[T], *, actor: Any = None) -> None:
        from hear.model.playlist.children.criteria.CriteriaPlaylist import CriteriaPlaylist

        CriteriaPlaylist.objects.bulk_create_for_criteria(instances)

    def _on_renamed(self, instance: T, *, old_name: str, actor: Any = None) -> None:
        if instance.tracks:
            for uploaded_track in instance.tracks.all():
                uploaded_track.update_file_metadata_from_uploaded_track_instance_values()

    def _on_track_genre_cleared(self, track: UploadedTrack, *, actor: Any = None) -> None:
        track.update_file_metadata_from_uploaded_track_instance_values()
