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


def get_default_page_statuses():
    page_statuses = {
        "intro": 0,
        "title": 1,
        "description": 2,
        "issue-description": 3,
        "studied-population": 4,
        "participant-recruitment": 5,
        "evaluation-costs": 6,
        "policy-costs": 7,
        "publication-intention": 8,
        "documents": 9,
        "event-dates": 10,
        "evaluation-types": 11,
        "impact-design": 12,
        "impact-analysis": 13,
        "process-design": 14,
        "process-analysis": 15,
        "economic-design": 16,
        "economic-analysis": 17,
        "other-design": 18,
        "other-analysis": 19,
        "interventions": 20,
        "outcome-measures": 21,
        "other-measures": 22,
        "ethics": 23,
        "impact-findings": 24,
        "economic-findings": 25,
        "process-findings": 26,
        "other-findings": 27,
        "process-standards": 28,
        "links": 29,
        "metadata": 30,
        "status": 31,
    }

    page_name_and_order = {page_name: page_info for page_name, page_info in page_statuses.items()}
    page_name_and_status = {
        page_name: EvaluationPageStatus.NOT_STARTED.name for page_name, page_info in page_statuses.items()
    }
    return {"page_status_order": page_name_and_order, "page_statuses": page_name_and_status}
