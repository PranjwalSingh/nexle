# Renders cover letters as HTML and converts them to PDF using WeasyPrint.


# Builds a styled HTML cover letter string from plain text and candidate contact info.
def build_cover_letter_html(
    cover_letter_text: str,
    candidate_name: str,
    candidate_email: str,
    candidate_phone: str,
    candidate_location: str = "",
    candidate_links: list = [],
) -> str: ...

# Converts an HTML string to PDF bytes using WeasyPrint with letter-size page settings.
def html_to_pdf(html_string: str) -> bytes: ...

# End-to-end — builds the HTML then converts straight to PDF bytes.
def generate_cover_letter_pdf(
    cover_letter_text: str,
    candidate_name: str,
    candidate_email: str,
    candidate_phone: str,
    candidate_location: str = "",
    candidate_links: list = [],
) -> bytes: ...

# Same as build_cover_letter_html — convenience alias for returning HTML only without converting.
def get_cover_letter_html(
    cover_letter_text: str,
    candidate_name: str,
    candidate_email: str,
    candidate_phone: str,
    candidate_location: str = "",
    candidate_links: list = [],
) -> str: ...
