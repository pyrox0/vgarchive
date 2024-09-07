{ python3Packages, fetchFromGitHub }:
python3Packages.buildPythonApplication rec {
  pname = "validate-pyproject-schema-store";
  version = "2024.08.26";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "henryiii";
    repo = "validate-pyproject-schema-store";
    rev = version;
    hash = "sha256-ymg0OFusy8fBV/hJXulDQwhkyFhOkr3OzhP3bd334AA=";
  };

  build-system = [ python3Packages.hatchling ];
}
