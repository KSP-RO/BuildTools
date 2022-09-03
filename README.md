# Workflow snippets for KSP-RO CI/CD
This repository contains [reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows) and [composite actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) referenced in other KSP-RO projects.

## Reusable workflows
Reusable workflows are stored in the [.github/workflows](https://github.com/StonesmileGit/BuildTools/tree/main/.github/workflows) folder. These are used at the `jobs` level.
### check-secret.yml
Checks if the password for the assemblies needed to build the mods is present
```yml
uses: StonesmileGit/BuildTools/.github/workflows/check-secret.yml@main
secrets:
  # Github secret with password to the zip with assemblies
  # Required: true
  KSP_ZIP_PASSWORD: ''
```
### validate-cfg-files.yml
Validates the cfg files using the [KSPMMCfgParser](https://github.com/KSP-CKAN/KSPMMCfgParser) by HebaruSan / CKAN
```yml
uses: StonesmileGit/BuildTools/.github/workflows/validate-cfg-files.yml@main
with:
  # Path to file with list of cfg files to ignore while running the validator
  blacklist_path: ''
```


## Composite actions
Composite actions are stored in separate folders. These are used at the `steps` level.
### download-assemblies
Downloads assemblies for the build process
```yml
uses: StonesmileGit/BuildTools/download-assemblies@main
with:
  # Github secret with password to the zip with assemblies
  # Required: true
  KSP_ZIP_PASSWORD: ''
```
### process-changelog
Creates a kerbalConfig node from the release notes and pre-pends that to an existing config file
```yml
uses: StonesmileGit/BuildTools/process-changelog@main
with:
  # Tag of the release, must be greater than last release and use semVer [major.minor.patch.build]
  # Required: true
  tag: ''
  # Body of the release notes
  # Required: true
  body: ''
  # Path to the config file to add the generated changelog node to
  # Required: true
  path: ''
```
### update-assembly-info
Uses bash to replace placeholder `@version@` in assemblyInfo file
```yml
uses: StonesmileGit/BuildTools/update-assembly-info@main
with:
  # Path to assemblyInfo
  # Required: true
  path: ''
  # Tag of the release uses semVer [major.minor.patch.build]
  # Required: true
  tag: ''
```
### update-version-in-readme
Replaces `compare/version...master` with `compare/new_version...master` in readme
```yml
uses: StonesmileGit/BuildTools/update-version-in-readme@main
with:
  # Path to readme
  # Required: true
  path: ''
  # Tag of the release uses semVer [major.minor.patch.build]
  # Required: true
  tag: ''
```