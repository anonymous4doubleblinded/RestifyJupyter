"""
Author: Anonymous Researcher
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


def cell_16() -> None:
    """
    Jupyter cell 16. See markdown description.
    :return: None
    """
    # Plot final correlations for the summed skill vectors
    reduce_labels_to_outliers: bool = True
    scatter_series_summed_skills: ScatterSeries = ScatterSeries(SummedSkillExtractor,
                                                                MethodologyPassrateExtractor,
                                                                FullLabelMaker(),
                                                                reduce_labels_to_outliers, "16-")
    scatter_series_summed_skills.plot_coupled_series({"ide", "tc"})
