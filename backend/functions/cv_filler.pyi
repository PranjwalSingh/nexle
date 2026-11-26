# Template engine that fills a LaTeX .tex template with cv_json data.
# This is the only place LaTeX syntax exists — everything before and after deals in cv_json.


# Loads a .tex template file by name from the templates directory.
def load_template(template_name: str) -> str: ...

# Sanitizes unicode characters that LaTeX can't handle (smart quotes, dashes, etc).
def _sanitize_latex_text(text: str) -> str: ...

# Escapes LaTeX special characters like &, %, $, _, #, {, } in a string.
def _escape_latex(text: str) -> str: ...

# Extracts and escapes a value from either a plain string or a stamped {id, value} dict.
def _val(field: object) -> str: ...

# Finds the matching %%END_FOR%% for a %%FOR_EACH%% block, handling nested loops.
def _find_matching_end(text: str, start: int) -> int: ...

# Substitutes <<var.key>> labels in a template block with values from the item dict.
def _substitute_labels(text: str, var: str, item: dict) -> str: ...

# Recursively renders a template block for a single item, handling nested FOR_EACH loops.
def _render_template(text: str, var: str, item: dict) -> str: ...

# Normalizes skills into a list of row dicts regardless of whether input is a string, dict, or list.
def _build_skill_rows(skills_raw: object) -> list: ...

# Main entry — fills a .tex template with all cv_json fields and returns the rendered LaTeX string.
def fill_template(cv_json: dict, profile: dict, template_name: str = "cv_temp1") -> str: ...
