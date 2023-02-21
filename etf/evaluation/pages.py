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
    "policy-costs": "Policy costs",
    "publication-intention": "Publication intention",
    "documents": "Documents",
    "event-dates": "Event dates",
    "evaluation-types": "Evaluation types",
    "impact-design": "Impact design",
    "impact-analysis": "Impact analysis",
    "process-design": "Process design",
    "process-analysis": "Process analysis",
    "economic-design": "Economic design",
    "economic-analysis": "Economic analysis",
    "other-design": "Other design",
    "other-analysis": "Other analysis",
    "interventions": "Interventions",
    "outcome-measures": "Outcome measures",
    "other-measures": "Other measures",
    "ethics": "Ethics",
    "impact-findings": "Impact findings",
    "economic-findings": "Economic findings",
    "process-findings": "Process findings",
    "other-findings": "Other findings",
    "process-standards": "Process and standards",
    "links": "Links and IDs",
    "metadata": "Metadata",
    "status": "Status",
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
    "process-standards",
    "links",
    "metadata",
    "status",
)

page_name_and_order = {page_name: page_url_names.index(page_name) for page_name in page_url_names}
default_page_statuses = {page_name: EvaluationPageStatus.NOT_STARTED.name for page_name in page_url_names}
