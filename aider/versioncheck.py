import os
import sys
import time
from pathlib import Path

import packaging.version

import aider
from aider import utils
from aider.dump import dump  # noqa: F401

VERSION_CHECK_FNAME = Path.home() / ".cisicode" / "caches" / "versioncheck"


def install_from_main_branch(io):
    """
    Install the latest version of cisicode from the main branch of the GitHub repository.
    """

    return utils.check_pip_install_extra(
        io,
        None,
        "Zainstalować wersję deweloperską cisicode z głównej gałęzi (main)?",
        ["git+https://github.com/Aider-AI/aider.git"],
        self_update=True,
    )


def install_upgrade(io, latest_version=None):
    """
    Install the latest version of aider from PyPI.
    """

    if latest_version:
        new_ver_text = f"Dostępna jest nowsza wersja cisicode v{latest_version}."
    else:
        new_ver_text = "Zainstalować najnowszą wersję cisicode?"

    docker_image = os.environ.get("AIDER_DOCKER_IMAGE")
    if docker_image:
        text = f"""
{new_ver_text} Aby zaktualizować, uruchom:

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
        io.tool_output("Uruchom cisicode ponownie, aby użyć nowej wersji.")
        sys.exit()

    return


def check_version(io, just_check=False, verbose=False):
    if just_check or verbose:
        io.tool_output("Sprawdzanie wersji jest wyłączone w tym przebiegu.")
    return False
