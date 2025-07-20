from mcp.server.fastmcp import FastMCP

from i18n import i18n, get_system_locale

_ = i18n()

# Create an MCP server
mcp = FastMCP("AI Code Mate")


@mcp.prompt(
    title=_("Name your code variables"),
    description=_("Generate the most appropriate variable name based on the description you have provided.")
)
async def code_variable_naming(description: str) -> str:
    """
    Create an MCP prompt to generate the prompt message for naming your code variables.

    Args:
        description (str): The detailed variable description you need to provide, required.

    Returns:
        The prompt message for AI LLMs, which is fixed format.
    """
    return f"""
        You are now an AI assistant skilled in programming. I will provide you with a piece of text
        description, and you will generate the most appropriate variable name based on my description.
        You should provide the answer in three naming styles: Pascal Case, Camel Case, and Snake Case.
    
        The description you have currently received is: {description}.
    
        Please start now and answer me in {get_system_locale()} language.
    """


if __name__ == "__main__":
    mcp.run()
