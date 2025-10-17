param(
  [string]$User = "tu_usuario",
  [string]$Host = "vps.example.com",
  [int]$RemotePort = 5000,
  [int]$LocalPort = 5000,
  [int]$SshPort = 22,
  [string]$IdentityFile = ""  # ruta a private key (opcional)
)

# Ejemplo de uso:
# .\open_ssh_tunnel.ps1 -User geobizi -Host 1.2.3.4 -IdentityFile "C:\Users\you\.ssh\id_rsa"
# Abre túnel local:LocalPort -> remoto:RemotePort vía SSH

$identityArg = if ($IdentityFile -ne "") { "-i `"$IdentityFile`"" } else { "" }
$cmd = "ssh -L ${LocalPort}:localhost:${RemotePort} -p ${SshPort} $identityArg $User@$Host"

Write-Output "Ejecutando: $cmd"
Write-Output "Presiona Ctrl+C para cerrar el túnel."
# Ejecutar el comando (mantiene la sesión)
Start-Process -NoNewWindow -Wait -FilePath "ssh" -ArgumentList "-L","${LocalPort}:localhost:${RemotePort}","-p","${SshPort}",($IdentityFile -ne "" ? "-i" : ""), $IdentityFile, "$User@$Host"
