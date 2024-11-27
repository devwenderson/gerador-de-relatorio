# Render PDF imports
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Email imports
from django.core.mail import EmailMessage
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Enviar email com anexo
def send_email_with_attachment(subject, message, recipient_list, file):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach(filename="Orçamento.pdf", content=file.content, mimetype="application/pdf")
    mail.send()



