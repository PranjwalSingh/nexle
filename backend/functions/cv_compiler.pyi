# Compiles a rendered .tex string into PDF bytes by shelling out to pdflatex/xelatex.
# This is the only module that touches the LaTeX engine directly.


class LatexCompileError(RuntimeError):
    log: str
    # Raised when the LaTeX engine fails. The .log attribute holds the last 4000 chars of the compile log.
    def __init__(self, message: str, log: str = "") -> None: ...


# Compiles a .tex source string to PDF bytes in a temp directory. Runs two passes for stability.
# Raises LatexCompileError with the log tail on failure. Always cleans up the temp dir.
def compile_cv_pdf(tex_source: str, engine: str = "pdflatex", timeout: int = 30) -> bytes: ...
