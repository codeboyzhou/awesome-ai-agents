from mcp.server.fastmcp import FastMCP

from i18n import i18n, get_system_locale

_ = i18n()

# Create an MCP server
mcp = FastMCP("AI Translation Service")


@mcp.prompt(
    title=_("Translate text content"),
    description=_("Translate text content to a specified language."),
)
async def translate_text(text: str, target_language: str) -> str:
    """
    Create an MCP prompt to generate the prompt message for translating the text content.

    Args:
        text (str): The text content you want to translate, required.
        target_language (str): The target language you expected, you can describe it in any way that LLM can understand, dialect is also supported, optional.

    Returns:
        The prompt message for AI LLMs, which is fixed format.
    """
    return f"""
        You are now an AI assistant skilled in language translation. I will provide you with a piece of text content,
        and you will translate it to {target_language}. If the target language is not specified, you should detect
        the language of the text content first, if it's {get_system_locale()} language, you should translate it to
        English, and if it's English, you should translate it to {get_system_locale()} language.
        
        The text content you have currently received is: {text}.
        
        Please start now.
    """


if __name__ == "__main__":
    mcp.run()
