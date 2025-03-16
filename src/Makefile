yaml:
	python main.py --to-json go-vise.bluto.yaml output.json --schema schema.json
json:
	python main.py --to-yaml output.json output.yaml --schema schema.json
validate:
	python main.py --validate output.json schema.json

test: 
	python -m unittest tests/test_main.py