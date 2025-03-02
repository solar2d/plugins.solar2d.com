#!/usr/bin/env python

import os
import json
import argparse
import json_from_repo
import glob


def process_plugins(plugins_dir):
    for plugin in glob.glob(os.path.join(plugins_dir, "*.json")):

        with open(plugin, "r") as f:
            plugin_data = json.load(f)

        if not plugin_data.get("error"):
            repo = f"{plugin_data['ghAccount']}/{plugin_data['publisherId']}-{plugin_data['plugin']}"
            json_from_repo.fetch(repo, plugins_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create plugin JSON")
    parser.add_argument("--plugins-dir", help="output directory", required=True)
    args = parser.parse_args()
    process_plugins(args.plugins_dir)
