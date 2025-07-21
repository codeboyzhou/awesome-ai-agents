from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server

TEXT_SEPARATOR = " "


async def run_stdio_server(server: Server) -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=server.name,
                server_version=server.version,
                instructions=server.instructions,
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )
