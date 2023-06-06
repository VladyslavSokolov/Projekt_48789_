def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)