# Copilot Agent Demo - Simple Calculator

A simple Python calculator application demonstrating basic arithmetic operations.

## Features

- **Add**: Add two numbers together
- **Subtract**: Subtract one number from another
- **Multiply**: Multiply two numbers
- **Divide**: Divide one number by another with zero-division protection
- **User-friendly interface**: Interactive command-line menu
- **Error handling**: Includes validation for invalid inputs and division by zero

## Project Structure

```
copilot-agent-demo/
├── main.py          # Main calculator application
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maran27mani/copilot-agent-demo.git
   cd copilot-agent-demo
   ```

2. No external dependencies are required. The project uses only Python standard library.

## Usage

Run the calculator:

```bash
python main.py
```

Then follow the on-screen menu:
1. Select an operation (Add, Subtract, Multiply, or Divide)
2. Enter two numbers when prompted
3. View the result
4. Repeat or select Exit to quit

## Example

```
========================================
         Simple Calculator
========================================

Operations:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Enter operation (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

## Error Handling

The calculator includes protection against:
- **Division by zero**: Returns an error message instead of crashing
- **Invalid input**: Prompts the user to enter valid numbers
- **Invalid operation**: Warns the user and asks to try again

## Requirements

- Python 3.6 or higher

## License

MIT License - Feel free to use and modify this project.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
