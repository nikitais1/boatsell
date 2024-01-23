from django.core.mail import send_mail

from config import settings
from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        subject='Заявки на покупку лодки',
        message=f'{order_item.name} ({order_item.email}) хочет купить вашу лодку {order_item.boat}. Вот сообщение: {order_item.message}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order_item.boat.owner.email]
    )
