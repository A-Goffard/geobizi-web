Guía rápida: WireGuard VPS (wg0) — Panel admin privado

1) En el VPS (ej. Debian/Ubuntu)
- Instalar:
  sudo apt update
  sudo apt install -y wireguard iptables

- Generar claves (puedes usar el script generate_keys.sh o manual):
  wg genkey | tee server_private.key | wg pubkey > server_public.key

- Copia el contenido de server_private.key en server_wg0.conf -> PrivateKey y guarda en /etc/wireguard/wg0.conf

- Habilitar IP forwarding:
  sudo sysctl -w net.ipv4.ip_forward=1
  # Para persistente: editar /etc/sysctl.conf y setear net.ipv4.ip_forward=1

- Abrir puerto UDP en firewall (ufw ejemplo):
  sudo ufw allow 51820/udp

- Iniciar:
  sudo systemctl enable wg-quick@wg0
  sudo systemctl start wg-quick@wg0
  sudo wg show

2) En cliente (Windows/Mac/Linux)
- Instala WireGuard client oficial.
- Genera par de claves (o usa script). Rellena client_wg0.conf con CLIENT_PRIVATE_KEY y SERVER_PUBLIC_KEY y Endpoint.
- Importa .conf en la app WireGuard y conecta.
- Verifica que puedes hacer ping a 10.14.0.1 (VPS) y acceder a servicios internos (ej. http://10.14.0.1:5000 o al backend si lo expone en esa IP interna).

3) Añadir/quitar peers
- Para añadir cliente, añade un bloque [Peer] en /etc/wireguard/wg0.conf con PublicKey del cliente y AllowedIPs = 10.14.0.X/32; luego sudo wg-quick down wg0 && sudo wg-quick up wg0 o usar wg set.
- Para revocar, elimina el Peer del server config y recarga wg.

4) Notas de seguridad
- No subas private keys ni ADMIN_API_KEY al repo.
- Si el panel va a ser accesible por varios administradores, distribuye claves cliente y revócalas cuando no sean necesarias.
- Considera usar AllowedIPs = 10.14.0.0/24 en server y AllowedIPs puntuales per-client, evita 0.0.0.0/0 si no quieres enrutar todo el tráfico del cliente por el VPS.

