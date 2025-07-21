import asyncio

from mcp.server.lowlevel import Server
from mcp.types import Prompt, PromptArgument, GetPromptResult, PromptMessage, TextContent

import common
from i18n import i18n, get_system_locale

_ = i18n()


####################################################### Prompts ########################################################

def code_variable_naming_prompt_definition() -> Prompt:
    return Prompt(
        name="code_variable_naming",
        title=_("Name your code variables"),
        description=_("Generate the most appropriate variable name based on the description you have provided."),
        arguments=[
            PromptArgument(
                name="description",
                description=_("The detailed variable description you need to provide, required."),
                required=True
            )
        ]
    )


def code_variable_naming_prompt_result(description: str) -> GetPromptResult:
    if description is None:
        result = "[CANCELLED] Invalid Prompt Argument: 'description' is empty."
    else:
        result = ("You are now an AI assistant skilled in programming. I will provide you with a piece of text "
                  "description, and you will generate the most appropriate variable name based on my description. "
                  "You should provide the answer in three naming styles: Pascal Case, Camel Case, and Snake Case. "
                  f"The description you have currently received is: {description}. "
                  f"Please start now and answer me in {get_system_locale()} language.")

    return GetPromptResult(
        description=_("Generate the most appropriate variable name based on the description you have provided."),
        messages=[PromptMessage(role="user", content=TextContent(type="text", text=result))]
    )


####################################################### Server #########################################################

# Create an MCP server
server = Server(name="AI Code Mate", version="0.1.0", instructions="You are an AI assistant skilled in programming.")


@server.list_prompts()
async def list_prompts() -> list[Prompt]:
    return [
        code_variable_naming_prompt_definition()
    ]


@server.get_prompt()
async def get_prompt(name: str, arguments: dict[str, str]) -> GetPromptResult | None:
    if name == "code_variable_naming":
        return code_variable_naming_prompt_result(arguments.get("description", None))
    # should never happen
    return None


if __name__ == "__main__":
    asyncio.run(common.run_stdio_server(server))
