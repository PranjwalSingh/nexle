# Async pipeline — scoring, CV gen, cover letter gen, and future auto-apply.
# Each task runs independently per dashboard config via a Celery queue.

# Scores a single user_job using the configured scoring flags.
def score_user_job(user_job_id: str, dashboard_config_id: str) -> dict: ...

# Generates and saves a tailored CV PDF for a user_job that passed the score threshold.
def generate_cv_for_user_job(user_job_id: str) -> dict: ...

# Generates and saves a cover letter PDF for a user_job that passed the score threshold.
def generate_cover_letter_for_user_job(user_job_id: str) -> dict: ...

# Runs the full pipeline — score, then CV/CL gen if above threshold — for all jobs in a dashboard.
def run_pipeline_for_dashboard(dashboard_config_id: str, user_id: str) -> None: ...

# Auto-applies to a job on behalf of the user. Planned feature, not yet implemented.
def auto_apply_for_user_job(user_job_id: str) -> dict: ...
