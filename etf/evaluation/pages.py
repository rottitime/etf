from etf.evaluation import choices


class EvaluationPageStatus(choices.Choices):
    DONE = "Done"
    IN_PROGRESS = "In progress"
    INCOMPLETE = "Incomplete"
    NOT_STARTED = "Not started"


class PageNames:
    @staticmethod
    def get_display_page_names():
        return {
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
            "status": "Status"
        }


def get_default_page_statuses():
    page_statuses = {
        "intro": (EvaluationPageStatus.NOT_STARTED.name, 0),
        "title": (EvaluationPageStatus.NOT_STARTED.name, 1),
        "description": (EvaluationPageStatus.NOT_STARTED.name, 2),
        "issue-description": (EvaluationPageStatus.NOT_STARTED.name, 3),
        "studied-population": (EvaluationPageStatus.NOT_STARTED.name, 4),
        "participant-recruitment": (EvaluationPageStatus.NOT_STARTED.name, 5),
        "evaluation-costs": (EvaluationPageStatus.NOT_STARTED.name, 6),
        "policy-costs": (EvaluationPageStatus.NOT_STARTED.name, 7),
        "publication-intention": (EvaluationPageStatus.NOT_STARTED.name, 8),
        "documents": (EvaluationPageStatus.NOT_STARTED.name, 9),
        "event-dates":( EvaluationPageStatus.NOT_STARTED.name, 10),
        "evaluation-types": (EvaluationPageStatus.NOT_STARTED.name, 11),
        "impact-design": (EvaluationPageStatus.NOT_STARTED.name, 12),
        "impact-analysis": (EvaluationPageStatus.NOT_STARTED.name, 13),
        "process-design": (EvaluationPageStatus.NOT_STARTED.name, 14),
        "process-analysis": (EvaluationPageStatus.NOT_STARTED.name, 15),
        "economic-design": (EvaluationPageStatus.NOT_STARTED.name, 16),
        "economic-analysis": (EvaluationPageStatus.NOT_STARTED.name, 17),
        "other-design": (EvaluationPageStatus.NOT_STARTED.name, 18),
        "other-analysis": (EvaluationPageStatus.NOT_STARTED.name, 19),
        "interventions": (EvaluationPageStatus.NOT_STARTED.name, 20),
        "outcome-measures": (EvaluationPageStatus.NOT_STARTED.name, 21),
        "other-measures": (EvaluationPageStatus.NOT_STARTED.name, 22),
        "ethics": (EvaluationPageStatus.NOT_STARTED.name, 23),
        "impact-findings": (EvaluationPageStatus.NOT_STARTED.name, 24),
        "economic-findings": (EvaluationPageStatus.NOT_STARTED.name, 25),
        "process-findings": (EvaluationPageStatus.NOT_STARTED.name, 26),
        "other-findings": (EvaluationPageStatus.NOT_STARTED.name, 27),
        "process-standards": (EvaluationPageStatus.NOT_STARTED.name, 28),
        "links": (EvaluationPageStatus.NOT_STARTED.name, 29),
        "metadata": (EvaluationPageStatus.NOT_STARTED.name, 30),
        "status": (EvaluationPageStatus.NOT_STARTED.name, 31),
    }

    page_name_and_order = {page_name: page_info[1] for page_name, page_info in page_statuses.items()}
    page_name_and_status = {page_name: page_info[0] for page_name, page_info in page_statuses.items()}
    return {"page_status_order": page_name_and_order, "page_statuses": page_name_and_status}