from datetime import datetime
from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router: APIRouter


class SalaryConfig(BaseModel):
    type: str
    min: Optional[float]
    max: Optional[float]

class DateRange(BaseModel):
    start: Optional[str]
    end: Optional[str]

class LocationConfig(BaseModel):
    mode: str
    includes: list[str]
    excludes: list[str]
    radius: Optional[dict]

class DashboardConfigCreate(BaseModel):
    name: str
    description: Optional[str]
    job_types: list[str]
    include_fields: list[str]
    exclude_fields: list[str]
    include_skills: list[str]
    exclude_skills: list[str]
    location: Optional[LocationConfig]
    include_companies: list[str]
    exclude_companies: list[str]
    company_mode: str
    salary: Optional[SalaryConfig]
    seasons: list[str]
    work_term_duration: Optional[str]
    date_range: Optional[DateRange]

class DashboardConfigPatch(BaseModel):
    name: Optional[str]
    description: Optional[str]
    job_types: Optional[list[str]]
    include_fields: Optional[list[str]]
    exclude_fields: Optional[list[str]]
    include_skills: Optional[list[str]]
    exclude_skills: Optional[list[str]]
    location: Optional[LocationConfig]
    include_companies: Optional[list[str]]
    exclude_companies: Optional[list[str]]
    company_mode: Optional[str]
    salary: Optional[SalaryConfig]
    seasons: Optional[list[str]]
    work_term_duration: Optional[str]
    date_range: Optional[DateRange]
    active: Optional[bool]


# Returns the full list of supported skills from the local skills.json file.
async def get_skills() -> list: ...

# Returns top-level job field/domain category names.
async def get_fields() -> list[str]: ...

# Returns cities grouped by country for the location picker.
async def get_locations() -> list[dict]: ...

# Searches the Redis-cached companies list by name. Returns up to 20 matches.
async def get_companies(search: str = "") -> list[dict]: ...

# Returns skills filtered to the requested field categories, or all skills if none specified.
async def get_skills_by_fields(fields: str = "") -> list[str]: ...


# Returns all dashboard configs belonging to the current user, newest first.
async def list_dashboard_configs(current_user: dict = Depends(...)) -> list[dict]: ...

# Returns a single dashboard config by ID, scoped to the current user.
async def get_dashboard_config(config_id: UUID, current_user: dict = Depends(...)) -> dict: ...

# Same as get, but strips internal fields (user_id, timestamps) for sharing/export.
async def export_dashboard_config(config_id: UUID, current_user: dict = Depends(...)) -> dict: ...

# Creates a new dashboard config for the current user. Starts inactive.
async def create_dashboard_config(payload: DashboardConfigCreate, current_user: dict = Depends(...)) -> dict: ...

# Partially updates an existing dashboard config. Ownership checked first.
async def update_dashboard_config(config_id: UUID, payload: DashboardConfigPatch, current_user: dict = Depends(...)) -> dict: ...

# Deletes a dashboard config. The Master config cannot be deleted.
async def delete_dashboard_config(config_id: UUID, current_user: dict = Depends(...)) -> dict: ...

# Sets a dashboard config to active=True so the scraper starts targeting it.
async def launch_dashboard_config(config_id: UUID, current_user: dict = Depends(...)) -> dict: ...


# Checks if a job matches a dashboard config's filters, skills, fields, locations, etc.
def apply_config_filters(job: dict, config: dict) -> bool: ...

# Pulls new jobs from the jobs table since last sync and inserts matching ones into user_jobs.
async def sync_jobs_for_config(config_id: UUID, current_user: dict = Depends(...)) -> dict: ...

# Returns paginated user_jobs for a dashboard, joined with job details. Filterable by status.
async def get_jobs_for_config(
    config_id: UUID,
    current_user: dict = Depends(...),
    limit: int = 50,
    offset: int = 0,
    status: Optional[str] = None,
) -> dict: ...
