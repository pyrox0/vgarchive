{
  fetchFromGitHub,
  python3Packages,
  validate-pyproject-schema-store,
}:
python3Packages.buildPythonApplication rec {
  pname = "validate-pyproject";
  version = "0.19";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "abravalheri";
    repo = "validate-pyproject";
    rev = "v${version}";
    hash = "sha256-hO7+i9EDstLVB9y1HLwyd/SvSJonNzUxYrFVEYp/8jg=";
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
