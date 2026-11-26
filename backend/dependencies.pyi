from supabase import Client
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

supabase: Client
supabase_admin: Client
bearer_scheme: HTTPBearer
redis_client: object | None


# Fetches and caches Supabase's public JWKS keys used to verify JWTs.
def get_jwks() -> dict: ...

# Verifies a Supabase JWT and returns the decoded payload, or None if invalid.
def verify_supabase_jwt(token: str) -> dict | None: ...

# FastAPI dependency — extracts and validates the Bearer token, returns the user's profile dict.
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict: ...

# FastAPI dependency — fetches a user_job row and verifies the current user owns it.
def get_owned_user_job(
    user_job_id: str,
    current_user: dict = Depends(get_current_user),
) -> dict: ...

# Fetches the user's Master dashboard config, or returns None if not found.
def get_master_config(user_id: str) -> dict | None: ...
