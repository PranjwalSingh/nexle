from datetime import datetime
from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router: APIRouter
VALID_STATUSES: set[str]


class JobPatch(BaseModel):
    status: Optional[str]
    notes: Optional[str]
    next_event: Optional[datetime]
    applied_at: Optional[datetime]

    # Raises 400 if status is not in VALID_STATUSES.
    def validate_status(self) -> None: ...

    # Raises 400 if notes exceed 1000 characters.
    def validate_notes(self) -> None: ...


# Fetches a user_job row scoped to the given user. 404s if missing or not owned.
def _get_owned_user_job(user_job_id: UUID, user_id: str) -> dict: ...

# Returns the user_job and the underlying job details joined together.
async def get_user_job(user_job_id: UUID, current_user: dict = Depends(...)) -> dict: ...

# Partially updates a user_job — status, notes, next_event, applied_at.
async def patch_user_job(user_job_id: UUID, patch: JobPatch, current_user: dict = Depends(...)) -> dict: ...

# Deletes a user_job row. Only succeeds if the row belongs to the current user.
async def delete_user_job(user_job_id: UUID, current_user: dict = Depends(...)) -> dict: ...
