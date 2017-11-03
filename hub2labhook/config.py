"""
Acquire runtime configuration from environment variables (etc).
"""

import os


def getenv(name, default=None, convert=str):
    """
    Fetch variables from environment and convert to given type.
    
    Python's `os.getenv` returns string and requires string default.
    This allows for varying types to be interpolated from the environment.
    """

     # because os.getenv requires string default.
    internal_default = "(none)"
    val = os.getenv(name, internal_default)

    if val == internal_default:
        return default

    if callable(convert):
        return convert(val)

    return val


GITLAB_TIMEOUT = 30

APP_ENVIRON = getenv("APP_ENV", "development")

# Events from GitLab hooks will be authenticated with this token.
GITLAB_SECRET_TOKEN_DEFAULT = "e19c1283c925b3206685ff522acfe3e6"
GITLAB_SECRET_TOKEN = getenv("GITLAB_TOKEN", GITLAB_SECRET_TOKEN_DEFAULT)

GITLAB_API = getenv("GITLAB_API", "https://gitlab.com")
GITLAB_REPO = getenv("GITLAB_REPO", None)
GITLAB_BRANCH = getenv("GITLAB_BRANCH", None)
GITLAB_TRIGGER = getenv("GITLAB_TRIGGER", None)
GITLAB_USER = getenv("GITLAB_USER", None)

GITHUB_CONTEXT = getenv("GITHUB_CONTEXT", "gitlab-ci")
GITHUB_INTEGRATION_ID = getenv("GITHUB_INTEGRATION_ID", "743")
GITHUB_INSTALLATION_ID = getenv("GITHUB_INSTALLATION_ID", "3709")
GITHUB_SECRET_TOKEN = getenv("GITHUB_SECRET_TOKEN", None)

FAILFASTCI_NAMESPACE = getenv("FAILFASTCI_NAMESPACE", "failfast-ci")
FAILFASTCI_API = getenv("FAILFAST_CI_API", "https://jobs.failfast-ci.io")

BUILD_PULL_REQUEST = getenv("BUILD_PULL_REQUEST", "true")
BUILD_PUSH = getenv("BUILD_PUSH", "false")