Get-ChildItem -Path:.\*.py -Recurse |
ForEach-Object {
    autopep8 --in-place --aggressive --aggressive $_.FullName
}