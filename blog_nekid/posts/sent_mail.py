from django.core.mail import send_mail


def send_message_to_mail(email, username, author, post_id):
    "Отправка письма с уникальным кодом новому пользователю."
    send_mail(
        subject='Новый пост',
        message=f'Здравствуйте {author}!'
                f'У блогера {username} появился новый пост!'
                f'Ссылка на пост "posts/{post_id}"',
        from_email='mail-service@yambd.qwerty',
        recipient_list=[email],
    )
