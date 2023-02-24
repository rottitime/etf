from etf.evaluation import choices


class EvaluationPageStatus(choices.Choices):
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
)

page_name_and_order = {page_name: page_url_names.index(page_name) for page_name in page_url_names}
default_page_statuses = {page_name: EvaluationPageStatus.NOT_STARTED.name for page_name in page_url_names}


def get_default_page_statuses():
    return dict(default_page_statuses)
