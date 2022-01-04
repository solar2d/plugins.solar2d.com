#!/usr/bin/env python3

import sys
import glob
import subprocess
import os
import json
import urllib.request
import urllib.parse

def get_dirs(root):
    for (_, dirs, _) in os.walk(root):
        return filter(lambda d: not d.startswith('.'), dirs)
    return []


def create_plugin_json(account, publisher, plugin, plugin_dir, destination_dir):
    tag_query = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'],
                               stderr=subprocess.DEVNULL,
                               stdout=subprocess.PIPE,
                               check=False,
                               cwd=plugin_dir)
    release = tag_query.stdout.decode('utf-8').strip()
    if tag_query.returncode != 0:
        print("Unable to find release for", plugin_dir, file=sys.stderr)
    versions = {}
    versions_root = os.path.join(plugin_dir, 'plugins')
    for ver in get_dirs(versions_root):
        ver_dir = os.path.join(versions_root, ver)
        platforms = list(sorted(p for p in get_dirs(ver_dir) if any(os.path.isfile(f) for f in glob.glob(os.path.join(ver_dir, p, '**'), recursive=True))))
        if platforms:
            versions[ver] = platforms
    
    homepage = "None"
    description = "None"
    githubInfoUrl = 'https://api.github.com/repos/'+account+'/'+publisher+"-"+plugin
    githubReq = urllib.request.urlopen(githubInfoUrl)
    if(githubReq):
      githubInfo = json.loads(githubReq.read().decode('utf-8'))
      homepage = githubInfo["homepage"])
      description = githubInfo["description"])
    
    if versions and release:
        output = {
            "latest": release,
            "supported": versions,
            "plugin": plugin,
            "homepage": homepage,
            "description": description,
            "publisherId": publisher,
            "ghAccount": account
        }
        output_file = os.path.join(destination_dir, f"{publisher}_{plugin}.json")
        orig = {}
        if os.path.isfile(output_file):
            with open(output_file, "r", encoding='utf-8') as f:
                orig = json.load(f)
        if not (output.items() <= orig.items()):
            for k, v in output.items():
                orig[k] = v
            with open(output_file, "w", encoding="utf8") as f:
                json.dump(orig, f, sort_keys=True, indent=4)


if __name__ == "__main__":
    owner, repo = sys.argv[1].split('/', 1)
    publisher, plugin = repo.split('-', 1)
    create_plugin_json(owner, publisher, plugin, 'current-plugin', 'plugins')
