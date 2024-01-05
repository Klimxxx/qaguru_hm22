from pathlib import Path

import android_wikipedia_tests


def abs_path_from_project(relative_path: str):
    return (
        Path(android_wikipedia_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )


def project():
    return Path(android_wikipedia_tests.__file__).parent.parent


def env(file):
    return str(project().joinpath(f"{file}"))


def apk_app_alpha_universal_release():
    return str(project().joinpath(f"resources/apk/app-alpha-universal-release.apk"))

