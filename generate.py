#!/usr/bin/env python3
import json, os, sys, glob

def getDirs(root):
    for (_, dirs, _) in os.walk(root):
        return filter(lambda d: not d.startswith('.'), dirs)
    return []

def addPluginEntries(pluginDir, entries):
    verRoot = os.path.join(pluginDir, 'plugins')
    release = ""
    try:
        with open(os.path.join(verRoot, 'RELEASE'), 'r') as f:
            release = f.read().strip()
    except:
        pass
    versions = {}
    for ver in getDirs(verRoot):
        verDir = os.path.join(verRoot, ver)
        platforms = list(sorted(p for p in getDirs(verDir) if glob.glob(os.path.join(verDir, p, '*'))))
        if platforms:
            versions[ver] = platforms
    if versions and release:
        entries["r"]=release
        entries["v"]=versions

def addPlugins(root, plugins):
    for github_account in getDirs(root):
        account_plugins = {}
        account_root = os.path.join(root, github_account)
        for provider in getDirs(account_root):
            providerDir = os.path.join(account_root, provider)
            providerPlugins = {}
            for plugin in getDirs(providerDir):
                pluginDir = os.path.join(providerDir, plugin)
                pluginEntries = {}
                addPluginEntries(pluginDir, pluginEntries)
                if pluginEntries:
                    providerPlugins[plugin] = pluginEntries
            if providerPlugins:
                account_plugins[provider] = providerPlugins
        if account_plugins:
            plugins[github_account] = account_plugins

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv)==2 else os.path.dirname(os.path.abspath(__file__))
    print("Scanning for plugins in '{}'".format(root), file=sys.stderr)
    plugins = {}
    addPlugins(root, plugins)
    print(json.dumps(plugins, sort_keys=True, indent=0))

