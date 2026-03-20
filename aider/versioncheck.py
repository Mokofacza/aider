import os
import sys
import time
from pathlib import Path

import packaging.version

import aider
from aider import utils
from aider.dump import dump  # noqa: F401

VERSION_CHECK_FNAME = Path.home() / ".aider" / "caches" / "versioncheck"


def install_from_main_branch(io):
    """
    Install the latest version of aider from the main branch of the GitHub repository.
    """

    return utils.check_pip_install_extra(
        io,
        None,
        "Install the development version of aider from the main branch?",
        ["git+https://github.com/Aider-AI/aider.git"],
        self_update=True,
    )


def install_upgrade(io, latest_version=None):
    """
    Install the latest version of aider from PyPI.
    """

    if latest_version:
        new_ver_text = f"Newer aider version v{latest_version} is available."
    else:
        new_ver_text = "Install latest version of aider?"

    docker_image = os.environ.get("AIDER_DOCKER_IMAGE")
    if docker_image:
        text = f"""
{new_ver_text} To upgrade, run:

    docker pull {docker_image}
"""
        io.tool_warning(text)
        return True

    success = utils.check_pip_install_extra(
        io,
        None,
        new_ver_text,
        ["aider-chat"],
        self_update=True,
    )

    if success:
        io.tool_output("Re-run aider to use new version.")
        sys.exit()

    return


def check_version(io, just_check=False, verbose=False):
    if just_check or verbose:
        io.tool_output("Version checking is disabled in this build.")
    return False
