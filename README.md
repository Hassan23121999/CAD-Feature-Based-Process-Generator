# CAD-Feature-Based-Process-Generator
Tool for analyzing CAD models based on features and generating corresponding manufacturing process information. It allows users to input model details and saves the suggested manufacturing processes to an Excel file



## Project Description
This project provides a tool for analyzing CAD models (STEP files) and generating corresponding manufacturing process information. The tool uses a graphical user interface (GUI) to let users input details about the CAD model and then suggests manufacturing processes based on these inputs. Users can also add additional processes. The resulting information is saved to an Excel file.

## Features
- **STEP File Selection:** Choose a STEP file for analysis.
- **User Input for Model Details:** Input details such as whether the model has holes and whether it is symmetrical or asymmetrical.
- **Process Suggestion:** Automatically suggests manufacturing processes based on the input details.
- **Additional Processes:** Allows users to add additional manufacturing processes.
- **Excel Output:** Saves the process information to an Excel file.

## Installation

### Prerequisites
- Python 3.x
- pandas
- tkinter
- python-occ (OCC)
- threading

You can install the required packages with pip:
```bash
pip install pandas tk python-occ
```

### Setup
Clone this repository to your local machine:
```bash
git clone https://github.com/Hassan23121999/CAD-Feature-Based-Process-Generator.git
cd CAD-Feature-Based-Process-Generator
```

## Usage
Run the script to open the GUI:
```bash
python CAD_Feature_based.py
```
Follow the GUI prompts to select a STEP file, input model details, and specify additional processes. The script will generate an Excel file with the suggested manufacturing processes.

## Support
For technical support or troubleshooting, please contact the support team via email at:
2016n1770@gmail.com

