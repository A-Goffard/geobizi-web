$vols = docker volume ls -q
foreach ($v in $vols) {
  Write-Output "=== Volume: $v ==="
  docker run --rm -v "${v}:/data" alpine sh -c "find /data -type f -iname '*.db' -print -exec ls -l {} \; 2>/dev/null || true"
}
