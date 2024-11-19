import pandas as pd
from FlowCytometryTools import FCPlate

# ========================
# Utility Functions
# ========================

def load_paths(file_path):
    """
    Load paths from a CSV file where each row maps a plate ID to a directory path.
    
    Args:
        file_path (str): Path to the CSV file containing PlateID and Path columns.
        
    Returns:
        dict: Dictionary mapping PlateIDs to directory paths.
    """
    try:
        df = pd.read_csv(file_path)
        return dict(zip(df['PlateID'], df['Path']))
    except Exception as e:
        print(f"Error loading paths: {e}")
        return {}

def load_experiment(file_path):
    """
    Load experiment mapping from a CSV file where each row maps a sample name to one or more wells.
    
    Args:
        file_path (str): Path to the CSV file containing Sample and Wells columns.
        
    Returns:
        dict: Dictionary mapping samples to lists of wells.
    """
    try:
        df = pd.read_csv(file_path)
        experiment = {}
        for _, row in df.iterrows():
            experiment[row['Sample']] = row['Wells'].split(",")  # Assuming Wells are comma-separated
        return experiment
    except Exception as e:
        print(f"Error loading experiment data: {e}")
        return {}

# ========================
# Main Analysis Code
# ========================

if __name__ == "__main__":
    # 1. Load Paths and Experiment Configurations
    paths_file = 'paths.csv'
    experiment_file = 'experiment.csv'

    # Load paths mapping
    print("Loading paths...")
    paths = load_paths(paths_file)
    print(f"Paths loaded: {paths}")

    # Load experiment mapping
    print("Loading experiment configuration...")
    my_exp = load_experiment(experiment_file)
    print(f"Experiment loaded: {my_exp}")

    # 2. Initialize Plate Dictionary
    plates = {}

    # 3. Load and Process Each Plate
    for plate_id, path in paths.items():
        try:
            print(f"Loading plate: {plate_id} from {path}...")
            plate = FCPlate.from_dir(ID=plate_id, path=path, parser="name")

            # Apply transformation (modify channels as needed for your data)
            plate = plate.transform(
                "hlog",
                channels=("FITC - Area", "Alexa Fluor 647 - Area")
            )

            # Save the plate to the dictionary
            plates[plate_id] = plate
            print(f"Plate {plate_id} loaded and transformed successfully.")
        except Exception as e:
            print(f"Error loading plate {plate_id}: {e}")

    # 4. Output Results Summary
    print("\nSummary of Loaded Plates:")
    for plate_id in plates:
        print(f"- {plate_id}: {len(plates[plate_id])} samples loaded.")

    print("\nScript completed.")