#!/usr/bin/env python3
import requests
import argparse
import sys
import os
import subprocess
import textwrap
from time import sleep
from typing import Optional

class MateAICoder:
    def __init__(self):
        self.api_url = "https://text.pollinations.ai"
        self.session_history = []
        self.setup_colors()
        
    def setup_colors(self):
        # Color codes for terminal output
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bright_cyan': '\033[1;96m',
            'reset': '\033[0m'
        }
        
    def colorize(self, text, color):
        return f"{self.colors.get(color, self.colors['reset'])}{text}{self.colors['reset']}"
    
    def display_banner(self):
        banner = r"""
██╗  ██████╗ ███████╗███████╗██████╗ ██╗  ██╗   ██╗     ██████╗ ██████╗ ██████╗ ███████╗
╚██╗ ██╔══██╗██╔════╝██╔════╝██╔══██╗██║  ╚██╗ ██╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ╚██╗██║  ██║█████╗  █████╗  ██████╔╝██║   ╚████╔╝     ██║     ██║   ██║██║  ██║█████╗  
 ██╔╝██║  ██║██╔══╝  ██╔══╝  ██╔═══╝ ██║    ╚██╔╝      ██║     ██║   ██║██║  ██║██╔══╝  
██╔╝ ██████╔╝███████╗███████╗██║     ███████╗██║       ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                  
        """
        colored_banner = ""
        for i, line in enumerate(banner.split('\n')):
            color = list(self.colors.keys())[i % (len(self.colors) - 2)]
            colored_banner += self.colorize(line, color) + '\n'
        
        print(colored_banner)
        print(self.colorize("Mate AI Coding Assistant (by RandomCatUser)", "bright_cyan"))
        print(self.colorize("Assisting with coding tasks and development", "yellow"))
        print(self.colorize("Type '/help' for available commands", "green"))
        print()
    
    def show_help(self):
        help_text = """
Available Commands:
  /help         - Show this help message
  /clear        - Clear the screen
  /history      - Show your query history
  /vscode       - Open last response in VS Code
  /save [file]  - Save last response to a file
  /exit or /quit - Exit the program

Enter your coding question or request to get assistance.
        """
        print(self.colorize(help_text, "cyan"))
    
    def animate_thinking(self):
        frames = ["|", "/", "-", "\\"]
        for i in range(12):
            print(self.colorize(f"{frames[i % len(frames)]} Processing your request", "yellow"), end='\r')
            sleep(0.1)
        print(" " * 40, end='\r')  # Clear the line
    
    def get_code_response(self, prompt: str) -> Optional[str]:
        """Get response from Pollinations AI API"""
        try:
            # Animate thinking process
            self.animate_thinking()
            
            # Call the API
            response = requests.get(f"{self.api_url}/{prompt}", timeout=30)
            
            if response.status_code == 200:
                return response.text
            else:
                print(self.colorize(f"API Error: {response.status_code}", "red"))
                return None
                
        except requests.exceptions.RequestException as e:
            print(self.colorize(f"Network Error: {e}", "red"))
            return None
        except Exception as e:
            print(self.colorize(f"Unexpected Error: {e}", "red"))
            return None
    
    def format_output(self, text):
        """Format the output in a clean box"""
        width = min(80, os.get_terminal_size().columns - 4)
        lines = text.split('\n')
        wrapped_lines = []
        
        for line in lines:
            if len(line) > width:
                wrapped_lines.extend(textwrap.wrap(line, width=width))
            else:
                wrapped_lines.append(line)
        
        # Create the box
        border = self.colorize("┌" + "─" * (width + 2) + "┐", "blue")
        bottom_border = self.colorize("└" + "─" * (width + 2) + "┘", "blue")
        
        print(border)
        for line in wrapped_lines:
            padded_line = line.ljust(width)
            print(self.colorize(f"│ {padded_line} │", "white"))
        print(bottom_border)
    
    def open_in_vscode(self, content, filename=None):
        """Open content in VS Code"""
        try:
            if not filename:
                filename = "mateai_response.txt"
            
            with open(filename, 'w') as f:
                f.write(content)
            
            # Try to open with VS Code
            subprocess.run(["code", filename], check=True)
            print(self.colorize(f"Opened in VS Code: {filename}", "green"))
            
        except FileNotFoundError:
            print(self.colorize("VS Code not found. Is 'code' command in your PATH?", "red"))
        except Exception as e:
            print(self.colorize(f"Error opening VS Code: {e}", "red"))
    
    def save_to_file(self, content, filename):
        """Save content to a file"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(self.colorize(f"Saved to: {filename}", "green"))
        except Exception as e:
            print(self.colorize(f"Error saving file: {e}", "red"))
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_banner()
    
    def run(self):
        """Main CLI loop"""
        self.clear_screen()
        last_response = None
        
        while True:
            try:
                user_input = input(self.colorize("Query: ", "green")).strip()
                
                if not user_input:
                    continue
                    
                # Add to history
                self.session_history.append(user_input)
                
                # Handle commands
                if user_input.startswith('/'):
                    if user_input == '/':
                        self.show_help()
                        continue
                    if user_input in ['/exit', '/quit']:
                        print(self.colorize("Session ended. Happy coding!", "bright_cyan"))
                        break
                    elif user_input == '/help':
                        self.show_help()
                    elif user_input == '/clear':
                        self.clear_screen()
                    elif user_input == '/history':
                        for i, item in enumerate(self.session_history[-10:]):
                            print(self.colorize(f"{i+1}: {item}", "cyan"))
                    elif user_input == '/vscode':
                        if last_response:
                            self.open_in_vscode(last_response)
                        else:
                            print(self.colorize("No previous response to open in VS Code", "red"))
                    elif user_input.startswith('/save'):
                        parts = user_input.split(' ', 1)
                        filename = parts[1] if len(parts) > 1 else "mateai_output.txt"
                        if last_response:
                            self.save_to_file(last_response, filename)
                        else:
                            print(self.colorize("No previous response to save", "red"))
                    else:
                        print(self.colorize("Unknown command. Type /help for available commands", "red"))
                    continue
                
                # Get response from API
                response = self.get_code_response(user_input)
                
                if response:
                    last_response = response
                    print()
                    print(self.colorize("Response:", "bright_cyan"))
                    self.format_output(response)
                    print()
                    
                    # Offer to open in VS Code if it looks like code
                    if any(keyword in response for keyword in ['def ', 'class ', 'import ', 'function ', 'const ', 'let ', 'var ']):
                        print(self.colorize("Tip: Use '/vscode' to open this in VS Code or '/save filename' to save to a file", "yellow"))
                else:
                    print(self.colorize("Unable to process your request. Please try again.", "red"))
                    
            except KeyboardInterrupt:
                print("\n" + self.colorize("Session ended. Happy coding!", "bright_cyan"))
                break
            except EOFError:
                print("\n" + self.colorize("Session ended. Happy coding!", "bright_cyan"))
                break

def main():
    parser = argparse.ArgumentParser(description='Mate AI CLI Coder')
    parser.add_argument('prompt', nargs='?', help='Direct prompt (optional)')
    parser.add_argument('--vscode', action='store_true', help='Open response in VS Code')
    parser.add_argument('--output', '-o', help='Save response to file')
    
    args = parser.parse_args()
    
    mate_ai = MateAICoder()
    
    # If direct prompt provided
    if args.prompt:
        response = mate_ai.get_code_response(args.prompt)
        if response:
            mate_ai.format_output(response)
            if args.output:
                mate_ai.save_to_file(response, args.output)
    else:
        # Start interactive modeinteractive mode
        mate_ai.run()

if __name__ == "__main__":
    main()