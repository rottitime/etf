import itertools

from etf.evaluation import utils


class EvaluationPageStatus(utils.Choices):
    DONE = "Done"
    IN_PROGRESS = "In progress"
    INCOMPLETE = "Incomplete"
    NOT_STARTED = "Not started"


page_display_names = {
    "intro": "Intro",
    "title": "Title",
    "description": "Description",
    "issue-description": "Issue description",
    "studied-population": "Studied population",
    "participant-recruitment": "Participant recruitment",
    "evaluation-costs": "Evaluation costs",
    "policy-costs": "Policy costs and budget",
    "publication-intention": "Publication intention",
    "documents": "Documents",
    "event-dates": "Event dates",
    "evaluation-types": "Evaluation types",
    "impact-design": "Impact evaluation design",
    "impact-analysis": "Impact evaluation analysis",
    "process-design": "Process evaluation design",
    "process-analysis": "Process evaluation analysis",
    "economic-design": "Economic evaluation design",
    "economic-analysis": "Economic evaluation analysis",
    "other-design": "Other evaluation design",
    "other-analysis": "Other evaluation analysis",
    "interventions": "Interventions",
    "outcome-measures": "Outcome measures",
    "other-measures": "Other measures",
    "ethics": "Ethical considerations",
    "impact-findings": "Impact evaluation findings",
    "economic-findings": "Economic evaluation findings",
    "process-findings": "Process evaluation findings",
    "other-findings": "Other evaluation findings",
    "processes-standards": "Processes and standards",
    "links": "Links and IDs",
    "metadata": "Metadata",
    "status": "Evaluation status",
    "end": "End",
}

page_url_names = (
    "intro",
    "title",
    "description",
    "issue-description",
    "studied-population",
    "participant-recruitment",
    "evaluation-costs",
    "policy-costs",
    "publication-intention",
    "documents",
    "event-dates",
    "evaluation-types",
    "impact-design",
    "impact-analysis",
    "process-design",
    "process-analysis",
    "economic-design",
    "economic-analysis",
    "other-design",
    "other-analysis",
    "interventions",
    "outcome-measures",
    "other-measures",
    "ethics",
    "impact-findings",
    "economic-findings",
    "process-findings",
    "other-findings",
    "processes-standards",
    "links",
    "metadata",
    "status",
    "end",
)

object_page_url_names = {
    "interventions": "intervention-page",
    "outcome-measures": "outcome-measure-page",
    "other-measures": "other-measure-page",
    "processes-standards": "processes-standard-page",
    "evaluation-costs": "evaluation-cost-page",
    "documents": "document-page",
    "links": "link-page",
    "event-dates": "event-date-page",
}

_evaluation_type_page_mapping = {
    "Impact evaluation": set(("impact-analysis", "impact-design", "impact-findings")),
    "Process evaluation": set(("process-analysis", "process-design", "process-findings")),
    "Economic evaluation": set(("economic-analysis", "economic-design", "economic-findings")),
    "Other": set(("other-analysis", "other-design", "other-findings")),
}

_all_evaluation_type_pages = set().union(*_evaluation_type_page_mapping.values())


def get_prev_next_page_name(page_name):
    assert page_name in page_url_names
    page_index = page_url_names.index(page_name)
    if page_index == 0:
        prev_url_name = None
    else:
        prev_url_name = page_url_names[page_index - 1]
    if page_index + 1 == len(page_url_names):
        next_url_name = None
    else:
        next_url_name = page_url_names[page_index + 1]
    return prev_url_name, next_url_name


page_name_and_order = {page_name: page_url_names.index(page_name) for page_name in page_url_names}
default_page_statuses = {page_name: EvaluationPageStatus.NOT_STARTED.name for page_name in page_url_names}


@utils.dictify
def get_page_name_and_order(evaluation_type):
    pages_to_remove = _all_evaluation_type_pages - _evaluation_type_page_mapping.get(evaluation_type, set())
    counter = itertools.count(0)

    for page_name in page_url_names:
        if page_name not in pages_to_remove:
            yield page_name, next(counter)


def get_default_page_statuses():
    return dict(default_page_statuses)
