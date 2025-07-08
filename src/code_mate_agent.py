import asyncio

from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("AI Code Mate")


@fast.agent(
    name="AI Code Mate",
    instruction="""
    You are a helpful AI assistant that generates variable names for code. You will receive a short natural language
    description and then generate the most appropriate variable name based on this description to return to the user.
    """,
    servers=["code_mate"]
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
