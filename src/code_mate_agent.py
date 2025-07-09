import asyncio

from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("AI Code Mate")


@fast.agent(
    name="AI Code Mate",
    instruction="You are an AI code assistant that can help developers name variables in code.",
    servers=["code_mate"]
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
