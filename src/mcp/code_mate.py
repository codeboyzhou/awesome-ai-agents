from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AI Code Mate")


@mcp.prompt(title="Code Variable Naming", description="Generate a variable name for a given brief description.")
async def code_variable_naming(programming_language: str, description: str) -> str:
    """Generate a variable name for a given brief description."""
    return f"{programming_language} variable naming: {description}"


if __name__ == "__main__":
    mcp.run()
