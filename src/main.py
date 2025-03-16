import yaml
import json
import argparse
import subprocess
import sys
import os

def validate_json(json_file, schema_file):
    try:
        result = subprocess.run([
            "check-jsonschema", "--schemafile", schema_file, json_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Validation successful: {json_file} conforms to {schema_file}")
            return True
        else:
            print(f"Validation failed for {json_file} against {schema_file}:")
            print(result.stdout)
            return False
    except FileNotFoundError:
        print("Error: check-jsonschema is not installed. Install it using `pip install check-jsonschema`.")
        sys.exit(1)

def yaml_to_json(yaml_file, json_file, schema_file=None):
    with open(yaml_file, 'r') as y_file:
        yaml_data = yaml.safe_load(y_file)
    
    if schema_file:
        temp_json_file = "temp_output.json"
        try:
            with open(temp_json_file, 'w') as j_file:
                json.dump(yaml_data, j_file, indent=4)
            
            if not validate_json(temp_json_file, schema_file):
                print("YAML to JSON conversion aborted due to validation failure.")
                sys.exit(1)
            else:
                with open(json_file, 'w') as j_file:
                    json.dump(yaml_data, j_file, indent=4)
                print(f"Converted {yaml_file} to {json_file}")
        finally:
            if os.path.exists(temp_json_file):
                os.remove(temp_json_file)
    else:
        with open(json_file, 'w') as j_file:
            json.dump(yaml_data, j_file, indent=4)
        print(f"Converted {yaml_file} to {json_file}")

def json_to_yaml(json_file, yaml_file, schema_file=None):
    if schema_file:
        if not validate_json(json_file, schema_file):
            print(f"Skipping conversion: {json_file} did not pass validation.")
            sys.exit(1)
    
    with open(json_file, 'r') as j_file:
        json_data = json.load(j_file)
    
    with open(yaml_file, 'w') as y_file:
        yaml.dump(json_data, y_file, default_flow_style=False, sort_keys=False)
    
    print(f"Converted {json_file} to {yaml_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert YAML to JSON and JSON back to YAML with optional validation.")
    parser.add_argument("--yaml-to-json", nargs=2, metavar=("YAML_FILE", "JSON_FILE"),
                        help="Convert YAML to JSON")
    parser.add_argument("--json-to-yaml", nargs=2, metavar=("JSON_FILE", "YAML_FILE"), 
                        help="Convert JSON to YAML")
    parser.add_argument("--validate", nargs=2, metavar=("JSON_FILE", "SCHEMA_FILE"), 
                        help="Validate JSON against a schema")
    parser.add_argument("--schema", metavar="SCHEMA_FILE", 
                        help="Specify a schema file for validation during conversion")
    
    args = parser.parse_args()
    
    if args.yaml_to_json:
        yaml_file, json_file = args.yaml_to_json
        yaml_to_json(yaml_file, json_file, args.schema)
    elif args.json_to_yaml:
        json_file, yaml_file = args.json_to_yaml
        if args.schema:
            validate_json(json_file, args.schema)
        json_to_yaml(json_file, yaml_file)
    elif args.validate:
        validate_json(*args.validate)
    else:
        print("Error: No valid arguments provided.")
        sys.exit(1)

if __name__ == "__main__":
    main()
