# Functions for selecting, tailoring, and stamping CV content before template rendering.


# Calls the LLM to select and rewrite the most relevant experiences and projects for a given job.
# Returns a cv_json dict with tailored bullets aligned to the job description.
def cv_selector(job: dict, user_profile: dict) -> dict: ...

# Recursively strips all "id" keys from a dict or list. Used before re-stamping.
def strip_ids(obj: object) -> object: ...

# Stamps stable UUIDs onto every field in cv_json so the frontend can track edits per field.
# Also injects contact info from the user profile if provided.
def stamp_cv_ids(cv: dict, profile: dict | None = None) -> dict: ...
