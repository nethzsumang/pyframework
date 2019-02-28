import sys
import os
from framework.Data.File.JSONFile import JSONFile


def version_check():
    a_packages = get_packages()
    python_ver_check(a_packages)
    package_check(a_packages)


def package_check(a_packages):
    a_dependencies = a_packages["dependencies"]

    for package_name, version in list(a_dependencies.items()):
        package_version_checker(package_name, version)


def package_version_checker(s_packagename, s_version):
    from pkg_resources import get_distribution, DistributionNotFound

    s_package_version = ""
    try:
        s_package_version = get_distribution(s_packagename).version
    except DistributionNotFound:
        install_package(s_packagename)

    a_req_version = s_version.split(".")
    a_sys_version = s_package_version.split(".")

    if a_sys_version[0] < a_req_version[0]:
        update_package_version(s_packagename)

    if a_sys_version[1] < a_req_version[1]:
        update_package_version(s_packagename)

    if len(a_sys_version) > 2:
        if a_sys_version[2] < a_req_version[2]:
            update_package_version(s_packagename)


def update_package_version(s_packagename):
    import pip

    pip.main(["install", "--upgrade", s_packagename])


def install_package(s_packagename):
    import pip

    pip.main(["install", s_packagename])


# PYTHON VERSION CHECKER
def python_ver_check(a_packages):
    [major, minor, micro] = get_python_version()
    s_pythonreq = a_packages["PYTHON_VERSION"]
    a_split_python_req = s_pythonreq.split(".")
    major_req = int(a_split_python_req[0])
    minor_req = int(a_split_python_req[1])
    micro_req = int(a_split_python_req[2])

    if major < major_req:
        display_python_version_error(a_split_python_req)

    if minor < minor_req:
        display_python_version_error(a_split_python_req)

    if micro < micro_req:
        display_python_version_error(a_split_python_req)


def get_python_version():
    a_pyversion = sys.version_info
    i_major = a_pyversion[0]
    i_minor = a_pyversion[1]
    i_micro = a_pyversion[2]

    return [i_major, i_minor, i_micro]


def get_packages():
    s_file_path = "config" + os.sep + "packages.json"
    return JSONFile(s_file_path, "r").read()


def display_python_version_error(a_req):
    print(
        "Your system's Python version does not match. App's Python version requirement is "
        + str(a_req[0])
        + "."
        + str(a_req[1])
        + "."
        + str(a_req[2])
    )
    exit(1)
