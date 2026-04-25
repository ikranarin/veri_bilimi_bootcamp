# utils.py
def generate_message(content):
    if not content:
        raise ValueError("Bildirim içeriği boş olamaz!")
    return content