# Flow Cytometry Data Analysis

This project provides a Python script to analyze flow cytometry data. It is designed to load and process data from multiple plates and experiments, leveraging the `FlowCytometryTools` library for transformations and analysis.

---

## Features

- **Flexible Data Input**: Supports loading paths and experiment configurations from CSV files.
- **Automated Data Processing**: Reads data files, applies transformations, and organizes results.
- **Error Handling**: Provides clear error messages for data-loading issues.
- **Extensible Design**: Easy to modify or expand for specific flow cytometry workflows.

---

## Prerequisites

### Python Libraries

Ensure the following Python libraries are installed:
- `pandas`
- `FlowCytometryTools`

Install dependencies using:
```bash
pip install pandas FlowCytometryTools
```

### Input Files

1. **Paths File (`paths.csv`)**:
   Maps plate IDs to file directory paths.  
   Example:
   ```csv
   PlateID,Path
   Plate1,/path/to/plate1
   Plate2,/path/to/plate2
   ```

2. **Experiment File (`experiment.csv`)**:
   Maps samples to associated wells.  
   Example:
   ```csv
   Sample,Wells
   Control,A1,A2,A3
   Test1,B1,B2,B3
   ```

---

## Usage

1. **Prepare Input Files**:
   - Create `paths.csv` and `experiment.csv` with the required formats.

2. **Run the Script**:
   Execute the script:
   ```bash
   python analyze_flow_cytometry.py
   ```

3. **Output**:
   - The script will summarize loaded plates and provide transformation details.

---

## Code Structure

### Main Script

- Loads input files (`paths.csv` and `experiment.csv`).
- Initializes a dictionary for flow cytometry plates.
- Processes each plate:
  - Loads data using `FlowCytometryTools`.
  - Applies a transformation (e.g., `hlog`).
  - Saves processed data for further analysis.

### Key Functions

1. **`load_paths(file_path)`**:
   - Reads a CSV file containing `PlateID` and `Path`.
   - Returns a dictionary mapping `PlateID` to file paths.

2. **`load_experiment(file_path)`**:
   - Reads a CSV file mapping sample names to wells.
   - Returns a dictionary of samples and their associated wells.

---

## Example Output

**Script Log**:
```
Loading paths...
Paths loaded: {'Plate1': '/path/to/plate1', 'Plate2': '/path/to/plate2'}

Loading experiment configuration...
Experiment loaded: {'Control': ['A1', 'A2', 'A3'], 'Test1': ['B1', 'B2', 'B3']}

Loading plate: Plate1 from /path/to/plate1...
Plate Plate1 loaded and transformed successfully.

Summary of Loaded Plates:
- Plate1: 96 samples loaded.

Script completed.
```

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## Contact

For questions or issues, contact the project maintainer at andreagtzq@gmail.com

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
