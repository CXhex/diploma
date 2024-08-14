# Earthworks Volume Calculator

The program automates the calculation process, ensuring high accuracy and efficiency. The application is designed using the MVC (Model-View-Controller) architecture, which separates the logic, user interface, and control, making the program flexible, maintainable, and extensible.

![Earthworks Volume Calculator](/assets/screenshot.png)

## Features

- **Automated Volume Calculation:** Calculates the volumes of cut and fill sections.
- **Dynamic Input Parameters:** Allows users to input various parameters such as section length, initial and final elevations, width of the base platform, slope indicators, and the number of tracks.
- **MVC Architecture:** Utilizes the Model-View-Controller design pattern for clean separation of concerns.
- **User-Friendly Interface:** Provides a simple and intuitive interface for inputting data and displaying results.
- **Additional Calculations:** Includes calculations for drainage prisms, slope placements, and cuvette volumes.
- **Output Flexibility:** Outputs results in a format that can be easily copied and used in reports.

## Download

Download the portable version from the [latest release](https://github.com/CXhex/diploma/releases/latest).

Run the executable you downloaded to run Earthworks Volume Calculator.

Requirements: Windows 10 and newer.

## Development environment

This part will walk you through setting up a development environment so you can build binaries yourself or make changes to the code.

### Prerequisites

- Python 3.11 (or higher)
- Virtual Environment (`venv`)
- Required dependencies listed in `requirements.txt`

### Setting Up the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/CXhex/diploma.git
    cd diploma
    ```
2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv 
    .\venv\Scripts\activate
    ```
3. Install Dependencies:

    Ensure you have a `requirements.txt` file in the root of your project directory containing all necessary dependencies. 
    
    Install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Building the Executable

Use PyInstaller to create a standalone executable. Make sure to run this command from the root directory of your project while the virtual environment is active.
```bash
pyinstaller --noconfirm -F --clean --windowed --add-data "venv/Lib/site-packages/customtkinter;customtkinter/" --add-data "venv/Lib/site-packages/CTkMessagebox;CTkMessagebox/" --add-data "venv/Lib/site-packages/tksheet;tksheet/" --add-data "venv/Lib/site-packages/win32;win32/" --add-data "components/icon.ico;components" -i components/icon.ico main.py
```

### Running the Executable

After running the PyInstaller command, the executable will be located in the `dist` directory.

## License

Earthworks Volume Calculator is released under the [MIT license](https://github.com/CXhex/diploma/blob/main/LICENSE).
