$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$venvPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'

try {
    if (-not (Test-Path -LiteralPath $venvPython)) {
        Write-Host 'Caut Python 3.14...'
        $created = $false
        foreach ($candidate in @('py', 'python')) {
            if (-not (Get-Command $candidate -ErrorAction SilentlyContinue)) { continue }
            $versionArgs = @()
            if ($candidate -eq 'py') { $versionArgs += '-3.14' }
            try {
                & $candidate @versionArgs -c "import sys; sys.exit(0 if sys.version_info[:2] == (3, 14) else 1)"
                if ($LASTEXITCODE -ne 0) { continue }
                & $candidate @versionArgs -m venv .venv
                if ($LASTEXITCODE -ne 0) { throw 'Crearea mediului virtual a esuat.' }
                $created = $true
                break
            } catch {
                Write-Host "Nu am putut folosi $candidate."
            }
        }
        if (-not $created) { throw 'Instaleaza Python 3.14 cu launcher-ul py sau cu python disponibil in PATH, apoi reincearca.' }
    } else {
        Write-Host 'Pastrez mediul virtual existent.'
    }

    & $venvPython -c "import sys; sys.exit(0 if sys.version_info[:2] == (3, 14) else 1)"
    if ($LASTEXITCODE -ne 0) { throw '.venv trebuie sa foloseasca Python 3.14. Mediul existent nu a fost sters.' }

    Write-Host 'Instalez dependentele din invicta/requirements.txt...'
    & $venvPython -m pip install -r invicta/requirements.txt
    if ($LASTEXITCODE -ne 0) { throw 'Instalarea dependentelor a esuat. Verifica mesajele de mai sus si conexiunea la internet.' }

    if (Test-Path -LiteralPath 'invicta/.env') {
        Write-Host 'Pastrez invicta/.env existent, fara modificari.'
    } else {
        $template = [System.IO.File]::ReadAllText((Join-Path $PSScriptRoot 'invicta/.env.example'))
        $secret = & $venvPython -c "import secrets; print(secrets.token_urlsafe(64))"
        if ($LASTEXITCODE -ne 0) { throw 'Generarea SECRET_KEY a esuat.' }
        $config = $template.Replace('SECRET_KEY=', "SECRET_KEY=$secret")
        [System.IO.File]::WriteAllText((Join-Path $PSScriptRoot 'invicta/.env'), $config, (New-Object System.Text.UTF8Encoding($false)))
        Write-Host 'Am creat invicta/.env cu o cheie aleatoare. Completeaza EMAIL_MAIL si EMAIL_PASSWORD in acest fisier.'
    }

    Write-Host 'Verific configuratia Django...'
    & $venvPython invicta/manage.py check
    if ($LASTEXITCODE -ne 0) { throw 'Verificarea Django a esuat.' }
    Write-Host 'Setup terminat. Pentru email, completeaza sau verifica EMAIL_MAIL si EMAIL_PASSWORD in invicta/.env.'
    Write-Host 'Baza de date nu a fost modificata. Porneste aplicatia cu run.bat.'
} catch {
    Write-Host "EROARE: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
