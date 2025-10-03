 if (-not $Session) {
        Add-Content -Path $logFile -Value "ERROR: Failed to create PSSession for $sAMAccountName. $($sessionError[0].Exception.Message)"
    }
