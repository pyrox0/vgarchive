{ lib, python3Packages }:
let
  fs = lib.fileset;
in
python3Packages.buildPythonApplication rec {
  pname = "vgarchive";
  version = "0.1.0";
  pyproject = true;

  src = fs.toSource {
    root = ../.;
    fileset = fs.unions [
      .././pyproject.toml
      .././README.md
      .././vgarchive
      .././uv.lock
    ];
  };

  build-system = with python3Packages; [ setuptools ];

  dependencies = with python3Packages; [
    django_5
    django-allauth
    docutils
    pillow
  ];

  meta = {
    changelog = "https://git.pyrox.dev/pyrox/archive-run/releases/${version}";
    description = "Charity Marathon VOD search site";
    homepage = "https://vgarchive.pyrox.dev";
    license = lib.licenses.free;
    maintainers = with lib.maintainers; [ pyrox0 ];
  };
}
