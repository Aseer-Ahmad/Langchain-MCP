{
    "mcpServers": {
        "terminal": {
            "command": "/Users/theailanguage/.local/bin/uv",
            "args": [
                "--directory", "SERVER_DIRECTORY",
                "run", 
                "terminal_server.py"
            ]
        }
    }
}

{
    "mcpServers": {
      "terminal_server": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "--init",
          "-e", "DOCKER_CONTAINER=true",
          "-v", "WORKSPACE_DIRECTORY:/root/mcp/workspace",
          "terminal_server_docker"
        ]
      }
    }
}