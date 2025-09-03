# GitHub Copilot & MCP Integration Configuration

This directory contains configuration files for enabling GitHub Copilot integration with Model Context Protocol (MCP) for the Mergington High School Activities project.

## Files

- `github-app.json` - GitHub App configuration with required permissions
- `enable-copilot-integration.yml` - Workflow to set up the integration
- `mcp-config.json` - MCP client configuration

## Permissions Enabled

The integration has been configured with the following permissions:

- **Issues**: Read/Write - Allows creating and managing GitHub issues
- **Contents**: Write - Allows reading and modifying repository files
- **Pull Requests**: Write - Allows creating and managing pull requests  
- **Repository Projects**: Write - Allows managing project boards
- **Metadata**: Read - Allows reading repository information

## Setup Instructions

1. The configuration files are now in place
2. Run the workflow to activate the integration:
   - Go to Actions tab in your GitHub repository
   - Find "Enable GitHub Copilot Integration" workflow
   - Click "Run workflow" button

3. The workflow will create a confirmation issue showing the integration is active

## Using MCP Tools

Once set up, you can use MCP tools like:
- `mcp_github_create_issue` - Create GitHub issues
- `mcp_github_create_pull_request` - Create pull requests
- `mcp_github_get_file_contents` - Read repository files
- And many more GitHub operations

## Troubleshooting

If you encounter permission errors:
1. Ensure the workflow has completed successfully
2. Check that the GitHub App has the required permissions
3. Verify your repository has Issues enabled in Settings
