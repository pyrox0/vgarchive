{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    pre-commit-hooks.url = "github:cachix/git-hooks.nix";
    pre-commit-hooks.inputs.nixpkgs.follows = "nixpkgs";
  };
  outputs =
    {
      self,
      nixpkgs,
      pre-commit-hooks,
      ...
    }:
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
          validate-pyproject = pkgs.callPackage ./nix/validate-pyproject.nix {
            inherit validate-pyproject-schema-store;
          };
          validate-pyproject-schema-store = pkgs.callPackage ./nix/validate-pyproject-schema-store.nix { };
          default = vgarchive;
        }
      );
      devShells = eachSystem (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
          validate-pyproject = self.packages.${system}.validate-pyproject;
        in
        {
          default = pkgs.mkShell {
            inherit (self.checks.${system}.pre-commit-check) shellHook;
            buildInputs =
              with pkgs;
              [
                (python3.withPackages (
                  ps: with ps; [
                    brotli
                    fonttools
                    tinycss2
                    uharfbuzz
                    zopfli
                  ]
                ))
                caddy
                djlint
                just
                lightningcss
                nixfmt-rfc-style
                nodejs
                pre-commit
                ruff
                uv
                validate-pyproject
                sqlite
              ]
              ++ self.checks.${system}.pre-commit-check.enabledPackages
              ++ validate-pyproject.optional-dependencies.all
              ++ validate-pyproject.optional-dependencies.store;
          };
        }
      );
      checks = eachSystem (system: {
        pre-commit-check = pre-commit-hooks.lib.${system}.run {
          src = ./.;
          hooks = {
            # pre-defined hooks
            check-added-large-files.enable = true;
            check-executables-have-shebangs.enable = true;
            check-shebang-scripts-are-executable.enable = true;
            check-symlinks.enable = true;
            end-of-file-fixer.enable = true;
            nixfmt-rfc-style.enable = true;
            pyright.enable = true;
            pyright.excludes = [ "^.*migrations/" ];
            ruff-format.enable = true;
            ruff-format.excludes = [ "^.*migrations/" ];
            ruff.enable = true;
            # Custom hooks
            djlint-django = {
              enable = true;
              name = "djLint Linting for Django";
              entry = "djlint --profile=django";
              language = "python";
              types = [ "html" ];
            };
            djlint-reformat-django = {
              enable = true;
              name = "djLint Linting for Django";
              entry = "djlint --reformat --profile=django";
              language = "python";
              types = [ "html" ];
            };
          };
        };
      });
    };
}
