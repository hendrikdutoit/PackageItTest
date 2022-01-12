import sys

sys.path.insert(
    0, 'C:\\Users\\hendr\\AppData\\Local\\Temp\\packageit_jhmzh30z\\PackageItTest\\src'
)
project = 'PackageItTest'
copyright = '2022, Ann Other'
author = 'Ann Other'
version = '0'
release = '0.0.1'
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "hendrikdutoit",  # Username
    "github_repo": "PackageItTest",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
language = 'en'
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
