param(
  [string]$Volume = "geobizi-web_backend_data",
  [switch]$CopyToHost,
  [string]$OutDir = ".\backup"
)

$pwd = (Get-Location).Path
Write-Output "Inspeccionando volumen Docker: $Volume"
Write-Output "Listado /data dentro del volumen:"
docker run --rm -v "$Volume:/data" alpine sh -c "ls -la /data || true; echo '--- tamaños ---'; du -sh /data/* 2>/dev/null || true"

Write-Output "Buscando ficheros .db dentro del volumen:"
docker run --rm -v "$Volume:/data" alpine sh -c "find /data -type f -iname '*.db' -maxdepth 3 -print || true"

if ($CopyToHost) {
  if (!(Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }
  $absOut = Resolve-Path $OutDir
  Write-Output "Copiando ficheros .db del volumen $Volume a $absOut ..."
  docker run --rm -v "$Volume:/data" -v "$absOut:/backup" alpine sh -c "cp /data/*.db /backup/ 2>/dev/null || true; ls -la /backup || true"
  Write-Output "Operación completada. Revisa $absOut"
}