import math
import pathlib

import pandas as pd

from etf.evaluation import choices, models

# Assumptions
# Sheets with relevant data to import are precisely the ones whose names are integers
# Assume columns and titles are always the same


RSM_FILENAME = "test.xlsx"
__here__ = pathlib.Path(__file__).parent
DATA_DIR = __here__ / "data"
FULL_PATH = DATA_DIR / RSM_FILENAME

INFO_NOT_IDENTIFIED = "Information not identified within the report"

EVALUATION_STANDARD_FIELDS_LOOKUP = {
    "title": "evaluation_information_evaluation_title",
    "short_title": "evaluation_information_short_title_for_evaluation",
    # "brief_description":
    # "issue_description":
    # "those_experiencing_issue":
    # "why_improvements_matter":
    # "who_improvements_matter_to":
    # "current_practice":
    # "issue_relevance":
    # "studied_population":
    # "eligibility_criteria":
    # "sample_size_units":
    # "sample_size_details":
    # "process_for_recruitment":
    # "recruitment_schedule":
    # "ethics_committee_approval":
    # "ethics_committee_details":
    # "ethical_state_given_existing_evidence_base":
    # brief_description = models.TextField(blank=True, null=True)
    # topics = models.JSONField(default=list)  # TODO - do we use these?
    # organisations = models.JSONField(default=list)  # TODO - how are we going to do orgs?
    "issue_description": "issue_issue_to_be_addressed",
    "those_experiencing_issue": "issue_who_is_experiencing_the_issue",
    "why_improvements_matter": "issue_why_the_issue_is_important__why_are_improvements_needed",
    "who_improvements_matter_to": "issue_who_does_it_matter_to",
    "current_practice": "issue_current_practice",
    "issue_relevance": "issue_what_difference_the_intervention_intends_to_make",
    # Evaluation type (multiselect)
    # "evaluation_type"
    # Studied population - should there be many rows?
    # "studied_population"
    # "eligibility_criteria"
    # "sample_size" - pos int field
    # "sample_size_units"
    # "sample_size_details"
    # Participant recruitment approach
    # "process_for_recruitment"
    # "recruitment_schedule"
    # Ethical considerations
    # "ethics_committee_approval": "ethical_considerations_ethics_committee_approval", #TODO - choices field
    "ethics_committee_details": "ethical_considerations_ethics_committee_details",
    "ethical_state_given_existing_evidence_base": "ethical_considerations_ethical_state_of_study_given_existing_evidence_base",
    "risks_to_participants": "ethical_considerations_risks_to_participants",
    "risks_to_study_team": "ethical_considerations_risks_to_study_team",
    "participant_involvement": "ethical_considerations_participant_involvement",
    "participant_information": "ethical_considerations_participant_information",
    "participant_consent": "ethical_considerations_participant_consent_(if_no,_why_not)",
    "participant_payment": "ethical_considerations_participant_payment_(if_yes,_please_ellaborate)",
    "confidentiality_and_personal_data": "ethical_considerations_confidentiality_and_personal_data",
    "breaking_confidentiality": "ethical_considerations_breaking_confidentiality",
    "other_ethical_information": "ethical_considerations_other_ethical_information",
    # Impact evaluation design
    # "impact_eval_design_name": "impact_evaluation_design_design" TODO - shouldn't be a JSON field
    "impact_eval_design_justification": "impact_evaluation_design_justification_for_design",
    "impact_eval_design_description": "impact_evaluation_design_description",
    "impact_eval_design_features": "impact_evaluation_design_features_to_reflect_real-world_implementation",
    "impact_eval_design_equity": "impact_evaluation_design_equity",
    "impact_eval_design_assumptions": "impact_evaluation_design_assumptions",
    "impact_eval_design_approach_limitations": "impact_evaluation_design_limitations_of_approach",
    # "impact_eval_framework"
    # "impact_eval_basis"
    # "impact_eval_analysis_set"
    # "impact_eval_effect_measure_type"
    # "impact_eval_primary_effect_size_measure"
    # "impact_eval_effect_measure_interval"
    # "impact_eval_primary_effect_size_desc"
    # "impact_eval_interpretation_type"
    # "impact_eval_sensitivity_analysis"
    # "impact_eval_subgroup_analysis"
    # "impact_eval_missing_data_handling"
    # "impact_eval_fidelity" # choices field
    # "impact_eval_desc_planned_analysis"
    # Process evaluation design
    # "process_eval_methods":
    # TODO - fields don't match
    # "process_eval_analysis_description"
    # Economic evaluation design
    # "economic_eval_type"
    # "perspective_costs"
    # "perspective_benefits"
    # "monetisation_approaches"
    # "economic_eval_design_details"
    # Economic evaluation analysis
    # "economic_eval_analysis_description"
    # TODO - add more details
    # Other evaluation design
    # other_eval_design_type
    # other_eval_design_details
    # Other evaluation analysis
    # other_eval_analysis_description
    # TODO - add more
    # Impact evaluation findings
    # impact_eval_comparison
    # impact_eval_outcome
    # impact_eval_interpretation
    # impact_eval_point_estimate_diff
    # impact_eval_lower_uncertainty
    # impact_eval_upper_uncertainty
    # # Economic evaluation findings
    # economic_eval_summary_findings
    # economic_eval_findings
    # # Process evaluation findings
    # process_eval_summary_findings
    # process_eval_findings
    # # Other evaluation findings
    # other_eval_summary_findings
    # other_eval_findings
}


# MANY OF THESE:
# - Evaluation costs and budget
# - Documents
# - Event dates
# - Intervention
# - Outcome measure
# - Other measure
# - Processes and standards


def get_all_upload_data():
    data = pd.read_excel(FULL_PATH, sheet_name=None, header=[0, 1])
    sheet_names = list(data.keys())
    relevant_sheet_names = [i for i in sheet_names if i.isdigit()]
    relevant_data = {n: df for n, df in data.items() if n in relevant_sheet_names}
    return relevant_data


def tidy_column_titles(df):
    df.columns = df.columns.to_flat_index()
    df.columns = ["_".join(col).strip() for col in df.columns.values]
    df.columns = [col.replace("/", " ") for col in df.columns.values]
    df.columns = [col.replace("  ", " ") for col in df.columns.values]
    df.columns = [col.replace(" ", "_") for col in df.columns.values]
    df.columns = [col.lower() for col in df.columns.values]
    assert len(df.columns) == 142
    return df


def get_all_upload_data_df():
    data = get_all_upload_data()
    all_dfs = list(data.values())
    transformed_dfs = [tidy_column_titles(df) for df in all_dfs]
    df = pd.concat(transformed_dfs)
    df = df.replace(INFO_NOT_IDENTIFIED, math.nan)
    df = df[~df["metadata_evaluation_id"].isnull()]
    df["metadata_evaluation_id"] = df["metadata_evaluation_id"].astype("int")
    df["metadata_report_id"] = df["metadata_report_id"].astype("int")
    evaluation_ids = df["metadata_evaluation_id"].unique()
    evaluation_ids = [id for id in evaluation_ids if not math.isnan(id)]
    return evaluation_ids, df


def get_data_for_field(data_for_eval, fieldname_in_rsm):
    """Standard field in evaluation ie one field, may need to aggregate data,
    though in most cases there will only be one value."""
    all_non_null_data = data_for_eval[data_for_eval[fieldname_in_rsm].notnull()][fieldname_in_rsm].unique()
    string_summary = "/n".join(all_non_null_data)
    return string_summary


def get_evaluation_types(data_for_eval):
    evaluation_types = []
    # if "Y" in data_for_eval[""]

    #    'evaluation_information_process', 'evaluation_information_impact',
    #    'evaluation_information_economic',
    #    'evaluation_information_other_evaluation_type_(please_state)',
    # if
    # Check for any Y in columns for process/impact/economic
    # If there is not a N in other evaluation type - add that value

    return evaluation_types


def upload_data_for_id(all_df, rsm_id):
    eval_df = all_df[all_df["metadata_evaluation_id"] == rsm_id]
    evaluation, _ = models.Evaluation.objects.get_or_create(rsm_eval_id=rsm_id)
    evaluation.status = choices.EvaluationStatus.PUBLIC
    # Add standard fields
    for model_field_name, rsm_field_name in EVALUATION_STANDARD_FIELDS_LOOKUP.items():
        value = get_data_for_field(eval_df, rsm_field_name)
        print(f"model_field_name: {model_field_name}")
        print(f"value: {value}")
        setattr(evaluation, model_field_name, value)

    # Add number fields
    # Add organisations
    # Add one-to-many objects
    # Add choice fields
    evaluation.save()


def upload_all_rsm_data():
    evaluation_ids, df = get_all_upload_data_df()
    for id in evaluation_ids:
        upload_data_for_id(df, id)
        print(f"Imported evaluation with id: {id}")


if __name__ == "__main__":
    upload_all_rsm_data()
    print("Done import!")
