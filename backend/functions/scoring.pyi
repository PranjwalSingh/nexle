from dataclasses import dataclass
from typing import Optional
from groq import Groq
from fastapi import APIRouter, Depends
from pydantic import BaseModel


@dataclass
class JobData:
    job_id: str
    job_title: str
    job_description: str
    job_skills: list[str]
    job_fields: list[str]
    job_location: str
    job_company: str

@dataclass
class ScoringConfig:
    include_skills: list[str]
    include_fields: list[str]
    include_locations: list[str]
    include_companies: list[str]
    exclude_skills: list[str]
    exclude_fields: list[str]

class ScoringSettings(BaseModel):
    run_s1s2: bool
    run_llm: bool

router: APIRouter
SKILL_ALIASES: dict[str, str]


# Lowercases and strips a skill string, then maps it to its canonical alias if one exists.
def _normalize_skill(skill: str) -> str: ...

# Normalizes a full list of skill strings into a deduplicated set.
def normalize_skills(skills: list[str]) -> set[str]: ...

# Returns the intersection of two normalized skill sets.
def skill_intersection(a: set[str], b: set[str]) -> set[str]: ...


# Score 1 — how well the user's skills cover what the job is asking for.
# Returns score 0-100 plus coverage, utilization, matched and missing skill breakdowns.
def cv_to_job(job_skills_raw: list[str], user_skills_raw: list[str]) -> dict: ...

# Score 2 — how well the job matches what the user actually wants based on their dashboard config.
# Returns score 0-100 plus a breakdown by skills, fields, location, and company signals.
def job_to_cv(job_data: JobData, scoringconfig: ScoringConfig) -> dict: ...

# Simple average of Score 1 and Score 2.
def match_score(s1: int, s2: int) -> int: ...


# Builds the LLM prompt for holistic scoring from job data, candidate context, and algo scores.
def build_llm_scoring_prompt(
    job_data: JobData,
    candidate_context: str,
    cv_to_job: int,
    job_to_cv: int,
) -> str: ...

# Builds a plain-text summary of a user's experiences, projects, and education for LLM context.
def _build_candidate_context(profile: dict) -> str: ...

# Score 3 — LLM holistic score. Captures narrative fit and semantic alignment beyond keyword matching.
# Returns score 0-100 plus a one-sentence rationale.
def llm_score(
    job_data: JobData,
    candidate_context: str,
    cv_to_job_score: int,
    job_to_cv_score: int,
    groq_client: Optional[Groq] = None,
) -> dict: ...


# Orchestrates all scoring for a single job+user pair. Runs whichever scores are flagged.
# Fetches job, profile, and config data from Supabase, then returns a combined result dict.
def score_job(
    job_id: str,
    user_id: str,
    scoring_config_id: str,
    run_s1s2: bool = False,
    run_llm: bool = False,
    groq_client: Optional[Groq] = None,
) -> dict: ...

# API endpoint — runs scoring for a job and writes the results back to the user_jobs row.
def run_scoring(
    job_id: str,
    scoring_config_id: str,
    scoring_settings: ScoringSettings,
    current_user: str = Depends(...),
) -> dict: ...
