#!/usr/bin/env python

import requests
import os
import json
import argparse
import bisect


def fetch(repo, out_dir):
    GITHUB_API_URL = f"https://api.github.com/repos/{repo}/releases/latest"
    TOKEN = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    response = requests.get(GITHUB_API_URL, headers=headers)
    response.raise_for_status()
    release_data = response.json()

    owner, plugin_data = repo.split("/", 1)
    plugin_publisher, plugin_name = plugin_data.split("-", 1)
    output = {
        "ghAccount": owner,
        "latest": release_data["tag_name"],
        "plugin": plugin_name,
        "publisherId": plugin_publisher,
        "supported": {},
    }

    assets = [a["name"].removesuffix(".tgz") for a in release_data["assets"]]
    for asset in assets:
        version, platform = asset.split("-", 1)
        bisect.insort(output["supported"].setdefault(version, []), platform)

    filename = f"{plugin_publisher}_{plugin_name}.json"
    with open(os.path.join(out_dir, filename), "w") as f:
        json.dump(output, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create plugin JSON")
    parser.add_argument("--repo", help="Repo in format owner/repo", required=True)
    parser.add_argument("--out-dir", help="output directory", required=True)
    args = parser.parse_args()
    fetch(args.repo, args.out_dir)
