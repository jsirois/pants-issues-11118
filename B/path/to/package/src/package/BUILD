python_library(
    sources = ["*.py", "!package.py"]
)

pex_binary(
    name="main",
    sources = ["package.py"],
    compatibility = ">=3.6",
)
