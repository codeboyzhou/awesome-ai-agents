import asyncio

from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("Awesome AI Agents")


@fast.agent(
    name="AI Code Mate",
    instruction="You are an AI assistant skilled in programming.",
    servers=["mcp_server_code_mate"]
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
