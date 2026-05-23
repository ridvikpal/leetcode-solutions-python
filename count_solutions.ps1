Get-ChildItem -Path . -File -Recurse |
    Where-Object { $_.FullName -notmatch '\.git|README\.md|count_solutions|.gitignore|LICENSE' } |
    Measure-Object | Select-Object -ExpandProperty Count
