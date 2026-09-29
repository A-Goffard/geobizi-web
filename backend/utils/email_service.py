import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def enviar_correo_reserva(email_destino: str, actividad: dict, token: str, num_personas: int):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    smtp_from = os.getenv("SMTP_FROM", smtp_user)

    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:8080")
    
    # Enlaces separados para gestión específica
    link_modificar = f"{frontend_url}/reservas/editar?token={token}"
    link_cancelar = f"{frontend_url}/reservas/cancelar?token={token}"

    asunto = f"Confirmación de reserva: {actividad.get('titulo', 'Geobizi')}"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; color: #333333; background-color: #f7f9f6; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #d4e2d4;">
            
            <h2 style="color: #2c5e3b; margin-top: 0; border-bottom: 2px solid #e8f0e8; padding-bottom: 10px;">
                🌿 Geobizi - Reserva Confirmada
            </h2>
            
            <p>¡Hola!</p>
            <p>Hemos registrado correctamente tu inscripción. Aquí tienes los detalles de tu actividad:</p>
            
            <div style="background-color: #f4f8f5; padding: 15px 20px; border-left: 4px solid #2c5e3b; border-radius: 4px; margin: 20px 0;">
                <p style="margin: 8px 0;"><strong>Actividad:</strong> {actividad.get('titulo')}</p>
                <p style="margin: 8px 0;"><strong>Fecha y Hora:</strong> {actividad.get('fecha')} a las {actividad.get('hora')}</p>
                <p style="margin: 8px 0;"><strong>Ubicación:</strong> {actividad.get('ubicacion')}</p>
                <p style="margin: 8px 0;"><strong>Plazas reservadas:</strong> {num_personas}</p>
                <p style="margin: 8px 0; font-size: 14px; color: #555;"><strong>Descripción:</strong> {actividad.get('descripcion', 'Disfruta de esta experiencia única al aire libre.')}</p>
            </div>

            <!-- Recomendaciones básicas -->
            <div style="background-color: #fff8e6; padding: 12px 15px; border-left: 4px solid #d4a373; border-radius: 4px; margin: 20px 0; font-size: 13px;">
                <p style="margin: 0 0 5px 0; font-weight: bold; color: #8c6239;">🎒 Recomendaciones básicas:</p>
                <ul style="margin: 0; padding-left: 20px; color: #555;">
                    <li>Lleva ropa y calzado adecuados para la climatología prevista y el terreno.</li>
                    <li>Trae agua suficiente para mantenerte hidratado/a durante la actividad.</li>
                    <li>Si finalmente no puedes asistir, por favor cancela tu plaza con antelación para que otra persona pueda aprovecharla.</li>
                </ul>
            </div>

            <p>Si necesitas modificar los datos de los asistentes o cancelar tu asistencia, puedes utilizar los siguientes botones:</p>

            <!-- Botones de acción separados -->
            <div style="text-align: center; margin: 25px 0;">
                <a href="{link_modificar}" style="background-color: #2c5e3b; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 13px; margin-right: 10px;">
                    Modificar Datos
                </a>
                <a href="{link_cancelar}" style="background-color: #b85d46; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 13px;">
                    Cancelar Reserva
                </a>
            </div>

            <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #eeeeee; font-size: 11px; color: #999999; text-align: center;">
                Geobizi &bull; Educación ambiental y bio-regeneración.
            </div>
        </div>
    </body>
    </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = smtp_from
    mensaje["To"] = email_destino
    mensaje.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()
            if smtp_user and smtp_password:
                servidor.login(smtp_user, smtp_password)
            servidor.sendmail(smtp_from, email_destino, mensaje.as_string())
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        
def enviar_correo_cancelacion(email_destino: str, actividad: dict, nombre_contacto: str):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    smtp_from = os.getenv("SMTP_FROM", smtp_user)

    asunto = f"Cancelación confirmada: {actividad.get('titulo', 'Actividad Geobizi')}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; color: #333333; background-color: #f7f9f6; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #d4e2d4;">
            
            <h2 style="color: #b85d46; margin-top: 0; border-bottom: 2px solid #fbeae5; padding-bottom: 10px;">
                Reserva Cancelada
            </h2>
            
            <p>Hola, {nombre_contacto}:</p>
            <p>Te confirmamos que la cancelación de tu reserva se ha procesado correctamente. Tus plazas han quedado liberadas para que otras personas puedan aprovecharlas.</p>
            
            <div style="background-color: #fff5f2; padding: 15px 20px; border-left: 4px solid #b85d46; border-radius: 4px; margin: 20px 0;">
                <p style="margin: 6px 0;"><strong>Actividad:</strong> {actividad.get('titulo')}</p>
                <p style="margin: 6px 0;"><strong>Fecha y Hora:</strong> {actividad.get('fecha')} a las {actividad.get('hora')}</p>
                <p style="margin: 6px 0;"><strong>Ubicación:</strong> {actividad.get('ubicacion')}</p>
            </div>

            <p style="font-size: 14px; color: #555;">
                Esperamos verte en futuras actividades y talleres de Geobizi. Puedes consultar el calendario actualizado en cualquier momento en nuestra web.
            </p>

            <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #eeeeee; font-size: 11px; color: #999999; text-align: center;">
                Geobizi &bull; Educación ambiental y bio-regeneración.
            </div>
        </div>
    </body>
    </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = smtp_from
    mensaje["To"] = email_destino
    mensaje.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()
            if smtp_user and smtp_password:
                servidor.login(smtp_user, smtp_password)
            servidor.sendmail(smtp_from, email_destino, mensaje.as_string())
    except Exception as e:
        print(f"Error al enviar correo de cancelación: {e}")


def enviar_correo_modificacion(email_destino: str, actividad: dict, token: str, num_personas: int, participantes: list):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    smtp_from = os.getenv("SMTP_FROM", smtp_user)

    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:8080")
    link_modificar = f"{frontend_url}/reservas/editar?token={token}"
    link_cancelar = f"{frontend_url}/reservas/cancelar?token={token}"

    asunto = f"Reserva actualizada: {actividad.get('titulo', 'Geobizi')}"

    # Generamos la lista de asistentes en HTML
    items_participantes = "".join([
        f"<li style='margin: 4px 0;'><strong>{p.get('nombre')} {p.get('apellidos')}</strong> ({p.get('edad')} años)</li>"
        for p in participantes
    ])

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; color: #333333; background-color: #f7f9f6; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #d4e2d4;">
            
            <h2 style="color: #2c5e3b; margin-top: 0; border-bottom: 2px solid #e8f0e8; padding-bottom: 10px;">
                🌿 Reserva Modificada con Éxito
            </h2>
            
            <p>¡Hola!</p>
            <p>Los cambios en tu reserva se han guardado correctamente. Estos son los datos actualizados:</p>
            
            <div style="background-color: #f4f8f5; padding: 15px 20px; border-left: 4px solid #2c5e3b; border-radius: 4px; margin: 20px 0;">
                <p style="margin: 6px 0;"><strong>Actividad:</strong> {actividad.get('titulo')}</p>
                <p style="margin: 6px 0;"><strong>Fecha y Hora:</strong> {actividad.get('fecha')} a las {actividad.get('hora')}</p>
                <p style="margin: 6px 0;"><strong>Ubicación:</strong> {actividad.get('ubicacion')}</p>
                <p style="margin: 6px 0;"><strong>Total de plazas asignadas:</strong> {num_personas}</p>
            </div>

            <div style="background-color: #fafafa; border: 1px solid #eee; border-radius: 4px; padding: 15px; margin: 20px 0;">
                <p style="margin: 0 0 8px 0; font-weight: bold; color: #2c5e3b;">Asistentes registrados:</p>
                <ul style="margin: 0; padding-left: 20px; color: #444;">
                    {items_participantes}
                </ul>
            </div>

            <p style="font-size: 13px; color: #666;">
                Si necesitas realizar nuevos ajustes o anular tu asistencia más adelante, conserva estos accesos directos:
            </p>

            <div style="text-align: center; margin: 25px 0;">
                <a href="{link_modificar}" style="background-color: #2c5e3b; color: #ffffff; padding: 10px 18px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 13px; margin-right: 10px;">
                    Modificar Datos
                </a>
                <a href="{link_cancelar}" style="background-color: #b85d46; color: #ffffff; padding: 10px 18px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 13px;">
                    Cancelar Reserva
                </a>
            </div>

            <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #eeeeee; font-size: 11px; color: #999999; text-align: center;">
                Geobizi &bull; Educación ambiental y bio-regeneración.
            </div>
        </div>
    </body>
    </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = smtp_from
    mensaje["To"] = email_destino
    mensaje.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()
            if smtp_user and smtp_password:
                servidor.login(smtp_user, smtp_password)
            servidor.sendmail(smtp_from, email_destino, mensaje.as_string())
    except Exception as e:
        print(f"Error al enviar correo de modificación: {e}")
        
def enviar_correo_oferta_plaza(email_destino: str, actividad: dict, token: str, num_personas: int, fecha_limite_texto: str, nombre_contacto: str):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    smtp_from = os.getenv("SMTP_FROM", smtp_user)

    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:8080")
    link_aceptar = f"{frontend_url}/reservas/confirmar-espera?token={token}"
    link_rechazar = f"{frontend_url}/reservas/cancelar?token={token}"

    asunto = f"¡Plazas disponibles para tu grupo!: {actividad.get('titulo', 'Geobizi')}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; color: #333333; background-color: #f7f9f6; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #d4e2d4;">
            
            <h2 style="color: #2c5e3b; margin-top: 0; border-bottom: 2px solid #e8f0e8; padding-bottom: 10px;">
                🎉 ¡Hay plazas disponibles para ti!
            </h2>
            
            <p>Hola, {nombre_contacto}:</p>
            <p>Se han liberado plazas para la actividad <strong>{actividad.get('titulo')}</strong> y por tu turno en la lista de espera tienes la oportunidad de reservarlas para tu grupo ({num_personas} plazas).</p>
            
            <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; border-radius: 4px; margin: 20px 0;">
                <p style="margin: 0; color: #7a5200; font-weight: bold; font-size: 15px;">
                    ⏰ Plazo para responder: tienes hasta el {fecha_limite_texto}.
                </p>
                <p style="margin: 6px 0 0 0; color: #555; font-size: 13px;">
                    Si no confirmas antes de esa hora, entenderemos que no podéis acudir y las plazas se ofrecerán a la siguiente persona en lista.
                </p>
            </div>

            <div style="background-color: #f4f8f5; padding: 15px 20px; border-left: 4px solid #2c5e3b; border-radius: 4px; margin: 20px 0;">
                <p style="margin: 4px 0;"><strong>Fecha y Hora:</strong> {actividad.get('fecha')} a las {actividad.get('hora')}</p>
                <p style="margin: 4px 0;"><strong>Ubicación:</strong> {actividad.get('ubicacion')}</p>
                <p style="margin: 4px 0;"><strong>Plazas reservadas temporalmente:</strong> {num_personas}</p>
            </div>

            <p style="text-align: center; margin-top: 25px; font-weight: bold;">
                ¿Deseas confirmar vuestra asistencia?
            </p>

            <div style="text-align: center; margin: 20px 0;">
                <a href="{link_aceptar}" style="background-color: #50963b; color: #ffffff; padding: 12px 22px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 14px; margin: 5px;">
                    ✅ Sí, confirmar mi reserva
                </a>
                <a href="{link_rechazar}" style="background-color: #b85d46; color: #ffffff; padding: 12px 22px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 14px; margin: 5px;">
                    ❌ No puedo ir / Ceder turno
                </a>
            </div>

            <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #eeeeee; font-size: 11px; color: #999999; text-align: center;">
                Geobizi &bull; Educación ambiental y bio-regeneración en Enkarterri.
            </div>
        </div>
    </body>
    </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = smtp_from
    mensaje["To"] = email_destino
    mensaje.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()
            if smtp_user and smtp_password:
                servidor.login(smtp_user, smtp_password)
            servidor.sendmail(smtp_from, email_destino, mensaje.as_string())
    except Exception as e:
        print(f"Error al enviar oferta de plaza: {e}")
        
def enviar_correo_turno_expirado(email_destino: str, actividad_titulo: str, nombre_contacto: str):
    # Correo breve avisando de que el plazo expiró y las plazas pasaron al siguiente
    ...