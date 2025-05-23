#!/usr/bin/env python3
from tuda_workspace_scripts.build import clean_logs, clean_packages
from tuda_workspace_scripts.print import print_workspace_error
from tuda_workspace_scripts.workspace import get_workspace_root, PackageChoicesCompleter
from helpers.remove_packages_from_env import *
import argcomplete
import argparse


if __name__ == "__main__":
    workspace_root = get_workspace_root()
    parser = argparse.ArgumentParser(
        prog="clean", description="Clean the workspace or specific packages."
    )
    packages_arg = parser.add_argument(
        "packages", nargs="*", help="If specified only these packages are cleaned."
    )
    packages_arg.completer = PackageChoicesCompleter(workspace_root)
    parser.add_argument("--force", default=False, action="store_true")
    parser.add_argument(
        "--logs",
        default=False,
        action="store_true",
        help="If specified only the logs are cleaned",
    )

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    if workspace_root is None:
        print_workspace_error()
        exit(1)

    if args.logs:
        exit(clean_logs(workspace_root, args.packages or [], force=args.force))
    else:
        exit(clean_packages(workspace_root, args.packages or [], force=args.force))
