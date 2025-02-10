# MCP Image Placeholder Server

This is a Model Context Protocol (MCP) server that provides a tool for generating placeholder images from different providers.

## Features

- Generates placeholder images from supported providers
- Supports two image providers:
  - [`placehold`](https://placehold.co/): Provides simple placeholder images
  - [`lorem-picsum`](https://picsum.photos/): Provides real images as placeholder images
- Validates input parameters
- Returns image URLs for immediate use

## Requirements

- Python 3.9+
- `uv` package manager

## Installation

1. Clone this repository
2. [Set up the configuration for MCP server](#configuration)

## Usage

The server exposes one tool:

### `image_placeholder`

Generate a placeholder image URL based on specified parameters.

**Parameters:**
- `provider`: The image provider to use (`placehold` or `lorem-picsum`)
- `width`: The width of the image (1-10000)
- `height`: The height of the image (1-10000)

**Returns:**
- URL string of the generated image

**Example Usage:**
```python
# Generate a 300x200 placeholder image
url = image_placeholder(provider="placehold", width=300, height=200)

# Generate a 500px square lorem-picsum image
url = image_placeholder(provider="lorem-picsum", width=500)
```

## Configuration

### To connect this server to Claude for Desktop:

1. Add the following to your `claude_desktop_config.json`:
   ```json
   {
       "mcpServers": {
           "image-placeholder": {
               "command": "uv",
               "args": [
                   "--directory",
                   "/ABSOLUTE/PATH/TO/PROJECT",
                   "run",
                   "main.py"
               ]
           }
       }
   }
   ```
2. Restart Claude for Desktop

### To connect this server to Cursor:

1. Open Cursor Settings
2. Head to the `Features` section
3. Scroll down to the `MCP Servers` section
4. Click on the `Add new MCP server` button
5. Enter the following information:
   - Name: `image-placeholder`
   - Type: `command`
   - Server URL: `uv --directory /ABSOLUTE/PATH/TO/PROJECT run main.py`
6. Click on the `Add ↵` button


## Troubleshooting

If the tool is not detected, use absolute path of the `uv` command, e.g.
```
/ABSOLUTE/PATH/TO/uv --directory /ABSOLUTE/PATH/TO/PROJECT run main.py
```

## Example Usage and Output (Cursor)

Prompt:
```
Create a new directory named "example" and a file named output.html.

Then create a single modern looking page using tailwindcss: https://unpkg.com/@tailwindcss/browser@4

Show a nice header, content, and footer, showing a photo gallery.

Save this into output.html
```

![Screenshot of Cursor Agent](example/cursor-agent.png)

Output:
[Example Output (Cursor)](example/output.html)

## License

[MIT License](LICENSE)
