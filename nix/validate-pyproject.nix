{
  fetchFromGitHub,
  python3Packages,
  validate-pyproject-schema-store,
}:
python3Packages.buildPythonApplication rec {
  pname = "validate-pyproject";
  version = "0.22";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "abravalheri";
    repo = "validate-pyproject";
    rev = "v${version}";
    hash = "sha256-NJUAzWu+g+5f2I0ucdNCeSTLxDCqgRI2GLpuT0lfAXE=";
  };

  build-system = [ python3Packages.setuptools-scm ];

  dependencies = [ python3Packages.fastjsonschema ];

  optional-dependencies = {
    all = with python3Packages; [
      packaging
      tomli
      trove-classifiers
    ];
    store = [ validate-pyproject-schema-store ];
  };

  doCheck = false;

  pythonImportsCheck = [ "validate_pyproject" ];
}
