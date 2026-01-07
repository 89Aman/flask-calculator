# Flask Calculator

A modern, web-based calculator application built with Flask and styled with Tailwind CSS. This calculator provides a clean, responsive interface with a dark theme for performing basic arithmetic operations.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Modern UI**: Clean, dark-themed interface using Tailwind CSS
- **Input Validation**: Handles invalid inputs and division by zero errors gracefully
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Calculations**: Instant results displayed after form submission

## Tech Stack

- **Backend**: Flask 3.1.2
- **Frontend**: HTML5, Tailwind CSS
- **Python Version**: 3.13+

## Project Structure

```
flask-calculator/
├── main.py              # Main Flask application with Calculator class
├── templates/
│   └── index.html       # Calculator UI template
├── static/
│   └── style.css        # Custom styles (if any)
├── pyproject.toml       # Project dependencies and configuration
├── uv.lock              # Lock file for dependencies
└── README.md            # Project documentation
```

## Installation

### Prerequisites

- Python 3.13 or higher
- pip or uv package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/89Aman/flask-calculator.git
   cd flask-calculator
   ```

2. **Install dependencies**
   
   Using pip:
   ```bash
   pip install flask
   ```
   
   Or using uv:
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the calculator**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. **Enter Numbers**: Input the first and second numbers in the provided fields
2. **Select Operation**: Choose from addition (+), subtraction (-), multiplication (*), or division (/)
3. **Calculate**: Click the "Calculate" button to see the result
4. **View Result**: The result will be displayed below the calculator form

### Example Calculations

- **Addition**: 10 + 5 = 15
- **Subtraction**: 20 - 8 = 12
- **Multiplication**: 6 * 7 = 42
- **Division**: 100 / 4 = 25

### Error Handling

The calculator handles common errors:
- **Invalid Input**: Non-numeric values will show "Invalid input"
- **Division by Zero**: Attempting to divide by zero will show "Cannot divide by zero"

## Code Overview

The application consists of a `Calculator` class with static methods for each operation:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b
```

## Development

To run the application in debug mode (default when running `main.py`):

```bash
python main.py
```

The debug mode enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available for educational purposes.

## Author

**Aman** - [89Aman](https://github.com/89Aman)

---

*Built with ❤️ using Flask and Tailwind CSS*
