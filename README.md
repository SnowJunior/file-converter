# File Converter
This is a file converter that allows for a user to be able to convert json and yaml files.
The tool handles validation of the files and does convertion with a schema defined for validation.

## Getting started
Please ensure that you have a python version ```3.7.0``` or higher to be able to use this tool.

Run ```pip install -r requirements.txt```. This will install all the required dependencies.

Once this completes you will be good to go 

## Usage
The project requires 2 input the json/yaml file and the schema
I the project there is a MAKEFILE setup to make the executio easy but the command can be run in the terminal

- Execution (yaml to json)

  Run ```python main.py --yaml_to_json input.yaml output.json --schema schema.yaml```
  Main files are the input.yaml file and schema.yaml
  - The input.yaml is the yaml file that the users wishes to convert.
  - The schema.yaml is the schema validation file that is used to validate the file before and after conversion.

- Execution validation

  As a user you can just decide to validate the files without having to convert the file. This has been handled as well.
    - Run ```python main.py --validate output.json schema.yaml```
    - This is you define the file that you wish to validate and the schema file that is going to be used for validation.
    - In this example the file is output.json and the schema is schema.yaml