{ python3Packages, fetchFromGitHub }:
python3Packages.buildPythonApplication rec {
  pname = "validate-pyproject-schema-store";
  version = "2024.11.22";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "henryiii";
    repo = "validate-pyproject-schema-store";
    rev = version;
    hash = "sha256-WtcUln23SyvZTm/GF3XIiSDVinMWvAhB/SZdb1Masrw=";
  };

  build-system = [ python3Packages.hatchling ];
}
