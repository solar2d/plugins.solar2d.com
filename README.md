# [Solar2D Free Plugin Directory](https://plugins.solar2d.com/)

This directory contains plugins available for Solar2D/CoronaSDK game engine.

## Migration from the old store

This migration can be done easily and automatically by Vlad. If you are a developer of a plugin in the Corona Marketplace, create an issue in this repo with a request to migrate it.

## Structure

Individual plugin descriptions lives in `plugins/` directory.

Plugins should be hosted on GitHub as released assets. Example of the plugin:

```json
{
    "ghAccount": "coronalabs",
    "latest": "v1",
    "plugin": "plugin.admob",
    "publisherId": "com.coronalabs",
    "supported": {
        "2020.3569": [
            "android",
            "iphone",
            "iphone-sim",
            "mac-sim",
            "win32-sim"
        ]
    }
}
```
This will try to download releases from the `https://github.com/${ghAccount}/${publisherId}-${plugin}/releases`. Release tag is stored in `${latest}`. Release assets should be named `${build}-${platform}.tgz`. Full download URL would be:
```
https://github.com/${ghAccount}/${publisherId}-${plugin}/releases/download/${latest}/${build}-${platform}.tgz
https://github.com/coronalabs/com.coronalabs-plugin.unityads/releases/download/v2/2019.3497-android.tgz
```

## Errors

Some vendors choose to run their own store, and host plugins there. For them, they can specify their own custom error message with link to their store. Example is `plugins/tech.scotth_plugin.classKit.json`:
```json
{
    "plugin": "plugin.classKit",
    "publisherId": "tech.scotth",
    "error": "Plugin is not provided by Solar2D Free directory, but can be activated [here](https://solar2dmarketplace.com/plugins?ClassKit_scotth-tech)."
}
```

## Adding plugin to the repo. If you want a link to your plugin or plugin hosted here, feel free to create an issue or pull request to this repo with details.
