# Renderers

- JSON Renderer
- BrowseableAPIRenderer
- XMLRenderer
- YAML Renderer
- JSONP Renderer

You an change the renderers anytime. Where can you set the type of content you want from the API? You do this by setting a header in the HTTP reaquest which is called Accept.

```bash
Accept: application/json
```

Lets say yuo want turn off the BrowsableAPIRendered and only include the JSONRendere

### settings.py

```py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONrenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
```
