# LLM-powered functions for parsing CVs, parsing job postings, and generating cover letters.


# Parses raw CV text (extracted from PDF) into a structured JSON dict using the LLM.
def cv_parser(cv_information: str) -> dict: ...

# Parses a raw job posting string into a structured JSON dict using the LLM.
def job_parser(job_description: str) -> dict: ...

# Generates a cover letter from a user's stored cv_json and a job dict.
# Used when the user already has a generated CV for the job.
def cover_letter_generator(job: dict, cv_json: dict) -> str: ...

# Generates a cover letter from the user's full profile dict and a job dict.
# Used when no custom CV has been generated yet.
def cover_letter_generator_for_new_job(job: dict, user_profile: dict) -> str: ...
