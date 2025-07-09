from mcp.server.fastmcp import FastMCP

from i18n import i18n

_ = i18n()

# Create an MCP server
mcp = FastMCP("AI Code Mate")


@mcp.prompt(
    title=_("Code variable naming"),
    description=_("Give a suitable code variable name based on the specified programming language and the description.")
)
async def code_variable_naming(programming_language: str, description: str) -> str:
    """
    Give a suitable code variable name based on the specified programming language and the description.

    Args:
        programming_language (str): The programming language you are using.
        description (str): The detailed variable description you need to provide.

    Returns:
        The prompt message for AI LLMs, which is fixed format.
    """
    return f"{programming_language} {_("variable naming")}: {description}"


if __name__ == "__main__":
    mcp.run()
