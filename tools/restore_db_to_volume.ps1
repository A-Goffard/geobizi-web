param(
  [Parameter(Mandatory=$true)][string]$BackupFile,  # ruta relativa o absoluta al .db en host
  [string]$Volume = "geobizi-web_backend_data",
  [switch]$Overwrite
)

$pwd = (Get-Location).Path
$absBackup = (Resolve-Path $BackupFile).ProviderPath
Write-Output "Restaurando $absBackup -> volumen $Volume ..."

# comprobar que el backup existe
if (!(Test-Path $absBackup)) {
  Write-Error "Backup no encontrado: $absBackup"
  exit 1
}

# copiar al volumen (montamos la carpeta del backup como /backup dentro del contenedor)
$backupDir = Split-Path -Path $absBackup -Parent
$backupName = Split-Path -Path $absBackup -Leaf

# Si no queremos sobreescribir, comprobar primero
if (-not $Overwrite) {
  Write-Output "Comprobando si ya existe fichero .db en el volumen..."
  $exists = docker run --rm -v "$Volume:/data" alpine sh -c "ls /data/*.db 2>/dev/null || true"
  if ($exists) {
    Write-Warning "Se han encontrado ficheros .db en el volumen:"
    Write-Output $exists
    Write-Warning "Si quieres forzar la restauración añade -Overwrite"
    exit 1
  }
}

# copiar
docker run --rm -v "$Volume:/data" -v "$backupDir:/backup" alpine sh -c "cp /backup/$backupName /data/ && ls -la /data || true"

Write-Output "Restauración completada. Reinicia contenedores y comprueba logs."
