import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging
from typing import Dict

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def enviar_email(destinatario: str, asunto: str, cuerpo_html: str):
    """Función base para enviar emails usando SendGrid."""
    sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
    from_email = os.getenv("SENDER_EMAIL")  

    if not sendgrid_api_key or not from_email:
        logger.error("SENDGRID_API_KEY o SENDER_EMAIL no están configurados en las variables de entorno.")
        return False

    message = Mail(
        from_email=from_email,
        to_emails=destinatario,
        subject=asunto,
        html_content=cuerpo_html
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        if 200 <= response.status_code < 300:
            logger.info(f"Email enviado correctamente a {destinatario} a través de SendGrid. Status Code: {response.status_code}")
            return True
        else:
            logger.error(f"Error enviando email a {destinatario} a través de SendGrid: {response.body}")
            return False
    except Exception as e:
        logger.error(f"Error al enviar email con SendGrid: {e}")
        return False

def enviar_email_nueva_reserva(admin_email: str, reserva_data: Dict):
    """Enviar notificación al administrador de nueva reserva"""
    asunto = f"Nueva reserva #{reserva_data['id_reserva']} - {reserva_data['nombre_cliente']}"
    
    cuerpo_html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
            <h2 style="color: #2c5530; text-align: center;">Nueva Reserva Recibida</h2>
            
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <p><strong>ID Reserva:</strong> {reserva_data['id_reserva']}</p>
                <p><strong>Cliente:</strong> {reserva_data['nombre_cliente']}</p>
                <p><strong>Email:</strong> {reserva_data['email_cliente']}</p>
                <p><strong>Teléfono:</strong> {reserva_data['telefono']}</p>
                <p><strong>Actividad ID:</strong> {reserva_data['actividad_id']}</p>
                <p><strong>Número de personas:</strong> {reserva_data['numero_personas']}</p>
                <p><strong>Fecha de reserva:</strong> {reserva_data['fecha_reserva']}</p>
                {f"<p><strong>Mensaje:</strong> {reserva_data['mensaje']}</p>" if reserva_data.get('mensaje') else ""}
            </div>
            
            <p style="text-align: center; margin-top: 30px;">
                <strong>Accede al panel de administración para gestionar esta reserva.</strong>
            </p>
            
            <hr style="margin: 30px 0;">
            <p style="font-size: 12px; color: #666; text-align: center;">
                Este es un email automático de GeoBizi - Sistema de Gestión de Reservas
            </p>
        </div>
    </body>
    </html>
    """
    
    return enviar_email(admin_email, asunto, cuerpo_html)

def enviar_confirmacion_reserva(cliente_email: str, reserva_data: Dict):
    """Enviar confirmación de reserva al cliente"""
    asunto = f"Confirmación de reserva #{reserva_data['id_reserva']} - GeoBizi"

    cuerpo_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                <h2 style="color: #2c5530; text-align: center;">¡Reserva Confirmada!</h2>
                <div style="background-color: #f0f8f0; padding: 20px; border-radius: 5px; margin: 20px 0;">
                    <p>Su reserva ha sido confirmada con los siguientes detalles:</p>
                    <p>Estimado/a {reserva_data['nombre_cliente']},</p>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin: 8px 0;"><strong>Número de reserva:</strong> {reserva_data['id_reserva']}</li>
                        <li style="margin: 8px 0;"><strong>Actividad:</strong> {reserva_data['actividad_nombre']}</li>
                        <li style="margin: 8px 0;"><strong>Fecha:</strong> {reserva_data['actividad_fecha']}</li>
                        <li style="margin: 8px 0;"><strong>Hora:</strong> {reserva_data['actividad_hora']}</li>
                        <li style="margin: 8px 0;"><strong>Número de personas:</strong> {reserva_data['numero_personas']}</li>
                        <li style="margin: 8px 0;"><strong>Precio total:</strong> {reserva_data['precio_total']}€</li>
                    </ul>
                </div>
                
                <p style="margin: 0;">
                    Si tiene alguna pregunta, no dude en contactarnos en cualquier momento.
                </p>
                <p style="margin: 0;">
                    El equipo de GeoBizi<br>
                </p>
                <p style="margin: 0;"><strong>Saludos cordiales,</strong><br></p>
                
                <div style="margin-top: 30px; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
                    <p>Gracias por elegir GeoBizi para su experiencia de turismo activo.</p>
                    <p><strong>Importante:</strong> Nos pondremos en contacto con usted próximamente con más detalles sobre el punto de encuentro y recomendaciones para la actividad.</p>
                </div>
            </div>
        </body>
        </html>
    """
    
    return enviar_email(cliente_email, asunto, cuerpo_html)
