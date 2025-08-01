import argparse
from pieces.base_command import BaseCommand
from pieces.urls import URLs
from pieces.settings import Settings


class ConfigCommand(BaseCommand):
    """Command to configure Pieces CLI settings."""

    def get_name(self) -> str:
        return "config"

    def get_help(self) -> str:
        return "Configure settings"

    def get_description(self) -> str:
        return "Configure various Pieces CLI settings including default editor and other preferences"

    def get_examples(self) -> list[str]:
        return [
            "pieces config",
            "pieces config --editor subl",
            "pieces config --editor nvim",
            "pieces config --editor vim",
            "pieces config --editor code",
        ]

    def get_docs(self) -> str:
        return URLs.CLI_CONFIG_DOCS.value

    def add_arguments(self, parser: argparse.ArgumentParser):
        """Add config-specific arguments."""
        parser.add_argument(
            "--editor",
            "-e",
            dest="editor",
            type=str,
            help="Set the default code editor",
        )

    def execute(self, **kwargs) -> int:
        """Execute the config command."""

        editor = kwargs.get("editor")
        if editor:
            Settings.cli_config.editor = editor
            Settings.logger.print(f"Editor set to: {editor}")
        else:
            Settings.logger.print("Current configuration:")
            Settings.logger.print(f"Editor: {Settings.cli_config.editor or 'Not set'}")
        return 0
