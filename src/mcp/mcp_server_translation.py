import asyncio

from mcp.server.lowlevel import Server
from mcp.types import Prompt, PromptArgument, GetPromptResult, PromptMessage, TextContent

import common
from i18n import i18n, get_system_locale

_ = i18n()


####################################################### Prompts ########################################################

def translate_text_prompt_definition() -> Prompt:
    return Prompt(
        name="translate_text",
        title=_("Translate text content"),
        description=_("Translate text content to a specified language."),
        arguments=[
            PromptArgument(
                name="text",
                description=_("The text content you want to translate, required."),
                required=True
            ),
            PromptArgument(
                name="target_language",
                description=_(
                    "The target language you expected. "
                    "You can describe it in any way that LLMs can understand, dialect is also supported. "
                    "This argument is optional, if not specified, the LLM will detect it automatically."
                ),
                required=False
            )
        ]
    )


def translate_text_prompt_result(text: str, target_language: str) -> GetPromptResult:
    if text is None:
        result = "[CANCELLED] Invalid Prompt Argument: 'text' is empty."
    else:
        result = [
            "You are now an AI assistant skilled in language translation.",
            "I will provide you with a piece of text content, and you should translate it.",
            f"The text content you have currently received is: {text}."
        ]

        if target_language is None:
            result.append("The target language is not specified now,")
            result.append("you should detect the language of the text content first.")
            result.append(f"If it's {get_system_locale()} language, you should translate it to English.")
            result.append(f"If it's English, you should translate it to {get_system_locale()} language.")
        else:
            result.append(f"The target language you expected is: {target_language}.")

        result.append("Please start now.")

    return GetPromptResult(
        description=_("Translate text content to a specified language."),
        messages=[PromptMessage(role="user", content=TextContent(type="text", text=common.TEXT_SEPARATOR.join(result)))]
    )


####################################################### Server #########################################################

# Create an MCP server
server = Server(name="AI Translation", version="0.1.0", instructions="You are an AI assistant skilled in translation.")


@server.list_prompts()
async def list_prompts() -> list[Prompt]:
    return [
        translate_text_prompt_definition()
    ]


@server.get_prompt()
async def get_prompt(name: str, arguments: dict[str, str]) -> GetPromptResult | None:
    if name == "translate_text":
        return translate_text_prompt_result(arguments.get("text", None), arguments.get("target_language", None))
    return None


if __name__ == "__main__":
    asyncio.run(common.run_stdio_server(server))
