{ python3Packages, fetchFromGitHub }:
python3Packages.buildPythonApplication rec {
  pname = "validate-pyproject-schema-store";
  version = "2024.10.21";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "henryiii";
    repo = "validate-pyproject-schema-store";
    rev = version;
    hash = "sha256-uK7UvxG7k8vT1YPheg+eyLSye2NP5pogtQ+qnK+V4w0=";
  };

  build-system = [ python3Packages.hatchling ];
}
