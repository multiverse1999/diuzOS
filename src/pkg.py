# SPDX-License-Identifier: BSD 3-Clause License
'''*
   * diuz/version 0.2/pkg.py
   *
   * Copyright (C) 2025, multiverse1999
   *
   * this file is package manager
   *'''
import os
import shutil
import subprocess
from pathlib import Path

PKG_MANAGER_DIR = os.path.join(os.environ["USERPROFILE"], ".pkg_manager")
PACKAGES_DIR = os.path.join(PKG_MANAGER_DIR, "packages")
INSTALLED_PACKAGES_FILE = os.path.join(PKG_MANAGER_DIR, "installed_packages.txt")

os.makedirs(PACKAGES_DIR, exist_ok = True)


def clone_repo(repo_url, install_dir):
    if os.path.exists(install_dir):
        print(f"Package already installed at {install_dir}")
        return
    try:
        subprocess.run(["git", "clone", repo_url, install_dir], check = True)
        print(f"Successfully cloned {repo_url} to {install_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_url}: {e}")
    except FileNotFoundError:
        print("Git is not installed. Please install Git from https://git-scm.com/")


def install_package(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    install_dir = os.path.join(PACKAGES_DIR, repo_name)

    clone_repo(repo_url, install_dir)

    with open(INSTALLED_PACKAGES_FILE, "a") as f:
        f.write(f"{repo_name}\n")
    print(f"Installed {repo_name}")


def uninstall_package(package_name):
    """Uninstall a package by deleting its directory."""
    install_dir = os.path.join(PACKAGES_DIR, package_name)
    if not os.path.exists(install_dir):
        print(f"Package {package_name} is not installed")
        return

    shutil.rmtree(install_dir)
    print(f"Uninstalled {package_name}")

    if os.path.exists(INSTALLED_PACKAGES_FILE):
        with open(INSTALLED_PACKAGES_FILE, "r") as f:
            packages = f.read().splitlines()
        with open(INSTALLED_PACKAGES_FILE, "w") as f:
            for pkg in packages:
                if pkg != package_name:
                    f.write(f"{pkg}\n")


def list_installed_packages():
    if not os.path.exists(INSTALLED_PACKAGES_FILE):
        print("No packages installed")
        return

    with open(INSTALLED_PACKAGES_FILE, "r") as f:
        packages = f.read().splitlines()
    if not packages:
        print("No packages installed")
    else:
        print("Installed packages:")
        for pkg in packages:
            print(f"- {pkg}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple Package Manager for Windows")
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install", help="Install a package from GitHub")
    install_parser.add_argument("repo_url", help="GitHub repository URL")

    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall a package")
    uninstall_parser.add_argument("package_name", help="Name of the package to uninstall")

    subparsers.add_parser("list", help="List installed packages")

    args = parser.parse_args()

    if args.command == "install":
        install_package(args.repo_url)
    elif args.command == "uninstall":
        uninstall_package(args.package_name)
    elif args.command == "list":
        list_installed_packages()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
