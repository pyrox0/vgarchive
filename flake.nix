{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };
  outputs =
    { nixpkgs, ... }:
    let
      eachSystem = nixpkgs.lib.genAttrs [ "x86_64-linux" ];
    in
    {
      packages = eachSystem (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        rec {
          vgarchive = pkgs.callPackage ./nix/package.nix { };
          default = vgarchive;
        }
      );
      devShells = eachSystem (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              (python3.withPackages (ps: [
                ps.pip
                ps.cookiecutter
              ]))
              caddy
              djlint
              just
              nixfmt-rfc-style
              nodejs
              ruff
              uv
              sqlite
            ];
          };
        }
      );
    };
}
