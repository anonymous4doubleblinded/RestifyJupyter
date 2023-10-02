"""
Implementation of LabelMaker that produces only animal names, without group affiliation.
@Author Anonymous Researcher
"""

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.label_maker import LabelMaker


class AnimalLabelMaker(LabelMaker):
    """
    Implementation of LabelMaker that produces only animal names, without group affiliation.
    """

    def make_labels(self, participants: list[AssessedParticipant], reduce_to_override: bool) -> \
            list[str]:
        """
        Returns the full participant name as [colour]_[animal]
        :param participants: as the list of participants for which labels are wanted.
        :param reduce_to_override: set to true to apply a filter that stripes all non-outliers to
        the empty string.
        :return: list of strings, each entry carrying the full participant label.
        """

        result: list[str] = []
        for assessed_participant in participants:
            # if reduction is requested and participant is not in override list, strip to empty
            # string.
            if self.is_in_override(assessed_participant) or not reduce_to_override:
                result.append(assessed_participant.animal_name)
            else:
                result.append("")
        return result
