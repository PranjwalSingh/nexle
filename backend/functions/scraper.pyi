# Scraper uses a convex-hull strategy — aggregates all active dashboard configs,
# builds a broad search matrix, scrapes once, then filters per user underneath.


# Fuzzy similarity ratio between two job description strings. Used for deduplication.
def desc_similarity(a: str, b: str) -> float: ...

# Fetches all active dashboard configs from Supabase to drive the search matrix.
def fetch_all_dashboard_configs() -> list[dict]: ...

# Builds union sets of all skills, fields, locations, and job types across all configs.
def build_sets(configs: list[dict]) -> tuple[set[str], set[str], set[str], set[str]]: ...

# Counts how many configs share each (field, location) pair — used to prioritize scrape depth.
def compute_votes(configs: list[dict]) -> dict[tuple[str, str], int]: ...

# Returns how many pages deep to scrape for a given field+location combo based on vote count.
def get_depth(superset: str, country: str, votes: dict[tuple[str, str], int]) -> int: ...

# Builds the full matrix of (field, location, job_type) combos to scrape, weighted by demand.
def build_search_matrix(
    fields: set[str],
    locations: set[str],
    job_types: set[str],
    votes: dict[tuple[str, str], int],
) -> list[tuple[str, str, str]]: ...

# Builds the global union of skills and fields across all active configs for LLM context.
def _build_global_sets_skills_n_fields() -> tuple[set[str], set[str]]: ...

# Filters a batch of scraped jobs against all dashboard configs. Returns matched (job, config) pairs.
def match_jobs_to_configs(batch: list[dict], configs: list[dict]) -> list[dict]: ...

# Layer 1 — checks if any known field keyword appears in the job title. Fast pre-filter.
def layer1_fields_in_title(fields: set[str], title_lower: str) -> bool: ...

# Layer 2 — deduplicates a job against already-seen titles/descriptions using fuzzy matching.
def layer2_dedup(
    title: str,
    description: str,
    seen_titles: set[str],
    seen_descs: list[str],
) -> bool: ...

# Attempts to extract salary info (type, min, max) from raw job text.
def extract_salary(combined: str) -> dict | None: ...

# Layers 3+4 — parses raw scraped HTML into a structured job dict. Extracts skills, fields, duration, salary.
def layer3_and_4_extract_metadata(
    card: object,
    search_field: str,
    search_location: str,
    job_type: str,
    season: str,
    global_skills: set[str],
    global_fields: set[str],
) -> dict | None: ...

# Inserts a batch of jobs into Supabase. Skips duplicates by URL. Returns count inserted and inserted rows.
def layer5_insert_jobs(batch: list[dict]) -> tuple[int, list[dict]]: ...

# Replaces an existing job row if the new one has richer data (more skills, longer description).
def layer5_replace(existing: dict, new_job: dict) -> bool: ...

# Merges new job data into an existing row — appends new skills, locations, fields without overwriting.
def layer5_merge(existing: dict, new_job: dict) -> dict: ...

# Fetches the full job description and skills from a LinkedIn job detail page.
def fetch_job_detail(job_id: str) -> tuple[str, list[str]]: ...

# Main entry point — builds the search matrix, scrapes LinkedIn, filters, dedupes, and inserts jobs.
def run() -> None: ...
