import yaml

def load_config(file_path: str) -> dict:
    """Load a YAML configuration file and return its contents as a dictionary."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# # usage example
# print(load_config(file_path=r"D:\STUDY\LLMOPS_KN\document_portal\config\config.yaml"))