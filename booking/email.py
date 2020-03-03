import string
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def booking_confirmation_business(booking):
    subject = f"Új időpontfoglalás - {booking.customer_name}: {booking.package} - {booking.headcount} - {booking.date} "
    from_email = 'noreply@bestpubcrawlbudapest.com'
    to = 'info@bestpubcrawlbudapest.com'
    html_content = render_to_string('booking/booking_confirmation_to_business.html', {'booking': booking})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def booking_confirmation_business(booking):
    subject = f"Your Memories Pub Crawl booking was successful. Your greatest night is coming soon!"
    from_email = 'noreply@bestpubcrawlbudapest.com'
    to = booking.customer_name
    html_content = render_to_string('booking/booking_confirmation_to_customer.html', {'booking': booking})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def failed_transaction(booking, transaction, customer):
    subject = f"Memories Pub Crawl - Egy tranzakció nem sikerült!"
    from_email = 'noreply@bestpubcrawlbudapest.com'
    to = booking.customer_name
    html_content = render_to_string('booking/failed_transaction.html', {'booking': booking, 'transaction': transaction, 'customer':customer})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
