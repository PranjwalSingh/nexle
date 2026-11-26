from typing import Optional
from fastapi import FastAPI, Depends, UploadFile
from pydantic import BaseModel

app: FastAPI


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class EducationEntry(BaseModel):
    id: Optional[str]
    institution: str
    degree: str
    field: str
    gpa: Optional[str]
    start_date: str
    end_date: str
    details: list[str]

class ExperienceEntry(BaseModel):
    id: Optional[str]
    company: str
    role: str
    location: str
    start_date: str
    end_date: str
    responsibilities: list[str]

class ProjectsEntry(BaseModel):
    id: Optional[str]
    name: str
    description: list[str]
    start_date: str
    end_date: str
    links: list[str]
    tech_stack: list[str]

class UpdateEntryRequest(BaseModel):
    section: str
    id: str
    data: dict

class BulkUpdateRequest(BaseModel):
    updates: list[UpdateEntryRequest]

class NewEntryRequest(BaseModel):
    section: str
    data: dict

class BulkAddRequest(BaseModel):
    adds: list[NewEntryRequest]

class DeleteEntryRequest(BaseModel):
    section: str
    id: str

class EditCoverLetterRequest(BaseModel):
    mode: str
    content: Optional[str]

class ProfileUpdateRequest(BaseModel):
    display_name: Optional[str]
    current_role: Optional[str]
    bio: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    location: Optional[str]
    links: Optional[list[str]]

class RefreshRequest(BaseModel):
    refresh_token: str


# Stamps a uuid on any list entry that's missing one.
def stamp_ids(entries: list) -> list: ...

# Health check — returns a simple HTML confirmation the API is up.
def root() -> str: ...

# Creates a new user in Supabase Auth, inserts a profile row, and returns a JWT.
def create_user(user: UserCreate) -> dict: ...

# Signs in with email/password and returns a JWT + refresh token.
def approve_login(user: UserLogin) -> dict: ...

# Returns basic info about the currently logged-in user.
def get_me(current_user: dict = Depends(...)) -> dict: ...

# Exchanges a refresh token for a new JWT.
def refresh_token(body: RefreshRequest) -> dict: ...

# Returns all editable profile fields for the profile settings page.
def get_profile(current_user: dict = Depends(...)) -> dict: ...

# Updates whichever profile fields are provided. Skips fields left as None.
def update_profile(body: ProfileUpdateRequest, current_user: dict = Depends(...)) -> dict: ...


# Returns the user's structured CareerTwin data — education, experience, projects, skills.
def get_careertwin_info(current_user: dict = Depends(...)) -> dict: ...

# Adds new entries to one or more CareerTwin sections in bulk.
def add_careertwin_info(body: BulkAddRequest, current_user: dict = Depends(...)) -> dict: ...

# Updates existing entries in one or more CareerTwin sections by ID.
def update_careertwin_info(body: BulkUpdateRequest, current_user: dict = Depends(...)) -> dict: ...

# Deletes a single entry from a CareerTwin section by ID.
def delete_careertwin_info(body: DeleteEntryRequest, current_user: dict = Depends(...)) -> dict: ...


# Returns all user_jobs for the current user joined with job info. Used by the master dashboard.
def get_all_user_jobs(current_user: dict = Depends(...)) -> dict: ...

# Updates the application status on a user_job. Sets applied_at if status is "applied".
def update_user_job_status(user_job_id: str, new_status: str, current_user: dict = Depends(...)) -> dict: ...


# Accepts a CV PDF, extracts text, parses it with the LLM, and saves structured data to the profile.
async def upload_cv(file: UploadFile, current_user: dict = Depends(...)) -> dict: ...

# Returns the user's current CV structured data — education, experience, projects, skills.
async def get_cv(current_user: dict = Depends(...)) -> dict: ...

# Bulk-updates sections of the user's stored CV data by entry ID.
async def update_cv(body: BulkUpdateRequest, current_user: dict = Depends(...)) -> dict: ...


# Generates a tailored cv_json for a specific job using the LLM, compiles to PDF, saves to storage.
def cv_generator(user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...

# Returns the saved cv_json and PDF URL for a specific user_job.
def cv_get(user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...

# Accepts a modified cv_json, recompiles it to PDF, and updates the user_job.
def cv_edit(cv_json: dict, user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...


# Generates a cover letter for a job using the stored cv_json, renders to PDF, saves to storage.
async def cl_generator(user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...

# Returns the stored cover letter HTML and PDF URL for a user_job.
def cl_get(user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...

# Regenerates or updates the cover letter. Mode is either "regenerate" or "html".
def cl_edit(data: EditCoverLetterRequest, user_job: dict = Depends(...), current_user: dict = Depends(...)) -> dict: ...

# Legacy endpoint — uploads a job PDF, parses it, inserts a job + user_job, generates a cover letter.
async def new_job_add(file: UploadFile, current_user: dict = Depends(...)) -> dict: ...

# Startup task — loads the companies CSV into Redis cache for fast company search.
async def load_companies_cache() -> None: ...
