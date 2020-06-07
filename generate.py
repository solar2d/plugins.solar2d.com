#!/usr/bin/env python3
import json
import sys


def add_plugin(plugin_json, c):
    with open(plugin_json, "r", encoding='utf-8') as f:
        plugin = json.load(f)
    if not plugin:
        print("ERROR: unable to read from", plugin_json, file=sys.stderr)
    c = c.setdefault(plugin["ghAccount"] or '-', {})
    c = c.setdefault(plugin["publisherId"], {})
    c = c.setdefault(plugin["plugin"], {})
    if "latest" in plugin:
        c["r"] = plugin["latest"]
    if "supported" in plugin:
        c["v"] = plugin["supported"]
    if "error" in plugin:
        c["e"] = plugin["error"]


if __name__ == "__main__":
    plugins = {}
    for plugin in sys.argv[1:]:
        add_plugin(plugin, plugins)
    print(json.dumps(plugins, sort_keys=True, indent=0))
