"""Bash-specific completion tester."""

import subprocess
import tempfile
import os
from typing import List, Tuple

from .conftest import CompletionTester


class BashCompletionTester(CompletionTester):
    """Bash-specific completion tester."""

    def __init__(self):
        super().__init__("bash")

    def run_completion_test(self, command_line: str) -> Tuple[bool, List[str], str]:
        """Run Bash completion test using subprocess."""
        # Create a test script that sources completions and runs COMPREPLY
        with tempfile.NamedTemporaryFile(mode="w", suffix=".sh", delete=False) as f:
            f.write(f"""#!/bin/bash
# Provide a minimal _init_completion function for testing
_init_completion() {{
    local exclude flag outx errx inx OPTIND=1

    while getopts "n:e:o:i:s" flag "$@"; do
        case $flag in
            n) exclude+=$OPTARG ;;
            e) errx=$OPTARG ;;
            o) outx=$OPTARG ;;
            i) inx=$OPTARG ;;
            s) split=false ;;
        esac
    done

    # Set cur, prev, words, and cword
    cur="${{COMP_WORDS[COMP_CWORD]}}"
    prev="${{COMP_WORDS[COMP_CWORD-1]}}"
    words=("${{COMP_WORDS[@]}}")
    cword=$COMP_CWORD

    # Handle redirection operators
    case "$prev" in
        ">"|"<"|">>"|"&>"|"2>"|"2>&1")
            return 1
            ;;
    esac

    # Handle = in variable assignments
    if [[ $cur == *=* ]]; then
        prev=${{cur%%=*}}
        cur=${{cur#*=}}
    fi

    return 0
}}

# Provide _filedir function for file completion
_filedir() {{
    local IFS=$'\\n'
    
    # Simple file/directory completion
    if [[ -z "$1" ]]; then
        # Complete with files and directories
        COMPREPLY=( $(compgen -f -- "$cur") )
    else
        # Complete with specific extension
        COMPREPLY=( $(compgen -f -X '!*'"$1" -- "$cur") )
    fi
    
    # Mark directories with trailing slash
    for ((i=0; i < ${{#COMPREPLY[@]}}; i++)); do
        if [[ -d "${{COMPREPLY[i]}}" ]]; then
            COMPREPLY[i]+="/"
        fi
    done
}}

# Source the completion file
source {self.completion_file}

# Parse command line into words array
IFS=' ' read -ra COMP_WORDS <<< "{command_line}"

# Set up the completion environment
COMP_CWORD=$(($(echo "{command_line}" | wc -w) - 1))
if [[ "{command_line}" == *" " ]]; then
    # If command line ends with space, we're completing a new word
    COMP_WORDS+=("")
    COMP_CWORD=$((COMP_CWORD + 1))
fi
COMP_LINE="{command_line}"
COMP_POINT=${{#COMP_LINE}}

# Clear COMPREPLY
COMPREPLY=()

# Call the completion function
_pieces_completion

# Output completions
for reply in "${{COMPREPLY[@]}}"; do
    echo "$reply"
done
""")
            script_path = f.name

        try:
            # Make script executable
            os.chmod(script_path, 0o755)

            # Run the Bash script
            result = subprocess.run(
                ["bash", script_path], capture_output=True, text=True, timeout=5
            )

            if result.returncode != 0:
                return False, [], f"Bash error: {result.stderr}"

            # Parse completions
            completions = []
            for line in result.stdout.strip().split("\n"):
                if line:
                    completions.append(line)

            return True, completions, ""

        except subprocess.TimeoutExpired:
            return False, [], "Completion timed out"
        except Exception as e:
            return False, [], f"Error running completion: {e}"
        finally:
            os.unlink(script_path)

