import os
import unittest
import subprocess

SCHEMA_FILE = "./schema.json"
VALID_JSON = "tests/valid.json"
MISSING_REQUIRED_JSON = "tests/missing_required.json"
INVALID_PROPERTIES_JSON = "invalid_properties.json"


class TestJSONValidation(unittest.TestCase):

    def run_validation(self, json_file, should_pass):
        """Helper function to run validation and check the expected result."""
        result = subprocess.run(
    ["python", "main.py", "--validate", json_file, os.path.abspath(SCHEMA_FILE)],
    capture_output=True,
    text=True
)

        
        if should_pass:
            self.assertEqual(result.returncode, 0, f"Validation should pass for {json_file}, but failed:\n{result.stdout}")
        else:
            self.assertNotEqual(result.returncode, 0, f"Validation should fail for {json_file}, but passed:\n{result.stdout}")

    def test_valid_json(self):
        """Test that a valid JSON file passes validation."""
        self.run_validation(VALID_JSON, should_pass=True)

    def test_missing_required_fields(self):
        """Test that a JSON file missing required properties fails validation."""
        self.run_validation(MISSING_REQUIRED_JSON, should_pass=False)

    def test_invalid_extra_properties(self):
        """Test that a JSON file with extra invalid properties fails validation."""
        self.run_validation(INVALID_PROPERTIES_JSON, should_pass=False)


if __name__ == "__main__":
    unittest.main()
