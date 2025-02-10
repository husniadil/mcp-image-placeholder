from typing import Literal
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("image-placeholder")


@mcp.tool()
def image_placeholder(
    provider: Literal["placehold", "lorem-picsum"],
    width: int,
    height: int,
) -> str:
    """
    Generate a placeholder image based on a provider, width, and height.
    Use this tool to generate a placeholder image for testing or development purposes.

    Args:
        provider: The provider to use for the image, must be either `placehold` or `lorem-picsum`.
        width: The width of the image, must be a positive integer between 1 and 10000.
        height: The height of the image, must be a positive integer between 1 and 10000.
    """
    # if provider is not in the list of providers, raise a ValueError
    if provider not in ["placehold", "lorem-picsum"]:
        raise ValueError(f"Invalid provider: {provider}")

    # if width is not a positive integer between 1 and 10000, raise a ValueError
    if width <= 0 or width > 10000:
        raise ValueError(
            f"Invalid width: {width}. Width must be a positive integer between 1 and 10000"
        )

    # if height is not a positive integer between 1 and 10000, raise a ValueError
    if height <= 0 or height > 10000:
        raise ValueError(
            f"Invalid height: {height}. Height must be a positive integer between 1 and 10000"
        )

    # if provider is placehold, return the placehold image
    if provider == "placehold":
        return (
            f"https://placehold.co/{width}x{height}"
            if height is not None
            else f"https://placehold.co/{width}"
        )
    # if provider is lorem-picsum, return the lorem-picsum image
    elif provider == "lorem-picsum":
        return (
            f"https://picsum.photos/{width}/{height}"
            if height is not None
            else f"https://picsum.photos/{width}"
        )


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
