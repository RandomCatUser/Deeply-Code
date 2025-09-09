![img1](https://github.com/RandomCatUser/Deeply-Code/blob/main/ascii-art-text%20(1).png?raw=true)

A professional command-line coding assistant that leverages the Pollinations AI API to help developers with coding tasks, featuring VS Code integration and a clean, professional interface.

## Features

- 🤖 AI-powered coding assistance using Pollinations AI API
- 💼 Professional, clean interface without emojis
- 🖥️ Boxed output formatting for better readability
- 🔗 VS Code integration for seamless workflow
- 💾 Save responses to files with custom names
- 📝 Session history to track your queries
- 🎨 Color-coded interface for better user experience
- ⚡ Fast and lightweight command-line tool

## Installation

### Method 1: Using Python directly

1. Ensure you have Python 3.8 or higher installed
2. Install the required dependencies:
   ```bash
   pip install requests
   ```
3. Download the `mate_ai.py` script
4. Run the script:
   ```bash
   python mate_ai.py
   ```

### Method 2: Using the executable

1. Download the pre-built executable from the releases page
2. Place the executable in your desired location
3. Add the directory to your system PATH for global access
4. Run the executable from any terminal:
   ```bash
   mate_ai
   ```

## Building from Source

If you want to build the executable yourself:

1. Install the required dependencies:
   ```bash
   pip install requests cx_Freeze
   ```

2. Download the source files:
   - `main.py` (main script)

## Usage

### Interactive Mode

Run the application without arguments to enter interactive mode:

```bash
main.py
```

### Direct Query Mode

Pass your query directly as an argument:

```bash
mate_ai "Write a Python function to calculate fibonacci sequence"
```

### Additional Options

```bash
# Open response in VS Code
mate_ai "Create a React component" --vscode

# Save response to a file
mate_ai "Python data analysis script" --output analysis.py

# Combine options
mate_ai "HTML template" --vscode --output template.html
```

## Available Commands (Interactive Mode)

- `/help` - Show help message
- `/clear` - Clear the screen
- `/history` - Show query history
- `/vscode` - Open last response in VS Code
- `/save [filename]` - Save last response to a file
- `/exit` or `/quit` - Exit the program

## API Information

This tool uses the Pollinations AI API:
- No API key required
- Rate limits may apply

## Requirements

- Python 3.8+ (if running the script directly)
- Windows, macOS, or Linux
- VS Code (optional, for the VS Code integration feature)
- Internet connection (for API access)

## Troubleshooting

### Common Issues

1. **VS Code not found error**: 
   - Ensure VS Code is installed
   - Make sure the `code` command is in your PATH

2. **Network errors**:
   - Check your internet connection
   - Verify the Pollinations AI API is accessible

3. **Colors not displaying**:
   - Some terminals may not support ANSI color codes
   - Try using a different terminal emulator

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed
2. Ensure you're using a supported Python version
3. Verify your internet connection is working

## License

This project is developed by RandomCatUser and is available for educational and personal use.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests to improve the functionality of this tool.

## Disclaimer

This tool is provided as-is without any warranties. The AI-generated code should be reviewed and tested before use in production environments.
