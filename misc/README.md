# Various tools

## `publish.yml`

GitHub actions example, which creates a release from plugins found in `plugins` of the repo. Plugins must follow following structure in the repo: `plugins/<min build number>/<platform>/<plugin files>.

It publishes release automatically when `plugins/**` is pushed. Sometimes it fails. It is possible to publish release manually with repo dispatch, for example
```bash
curl -H "Authorization: token $PAT" -X POST --data '{"event_type":"build"}' https://api.github.com/repos/coronalabs/com.coronalabs-plugin.gpgs/dispatches
```
`PAT` is set to GitHub's [personal acess token](https://github.com/settings/tokens).

