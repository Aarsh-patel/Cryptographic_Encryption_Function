import flet as ft
from Message import *
from ChatMessage import *
import time
from LogisticMap import *
from ChaoticEncryption import ChaoticEncryption
import warnings

def main(page: ft.Page):
    page.horizontal_alignment = "stretch"
    page.title = "Flet Chat"

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.", message_type="login_message"))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            encrypted_message = ChaoticEncrypt(new_message.value)
            page.pubsub.send_all(Message(page.session.get("user_name"), encrypted_message, message_type="chat_message"))
            new_message.value = ""
            new_message.focus()
            page.update()


    def ChaoticEncrypt(message: str) -> str:
        cur_time = int(time.time())
        chaotic_sequence = logistic_map( cur_time % 2.1, cur_time % 3.9, len(message))
        shuffled_result = shuffle_text(message, chaotic_sequence)
        enc = ChaoticEncryption(0.01, 3.95, shuffled_result)
        message = enc.encryption(shuffled_result)
        print("Encrypted Message -->",message)
        message = enc.decryption(message)
        message = reshuffle_text(message,chaotic_sequence)
        print("Decrypted Message -->",message)
        return message
    

    def ChaoticDecrypt(message: str) -> str:
        cur_time = int(time.time())
        chaotic_sequence = logistic_map( cur_time % 2.1, cur_time % 3.9, len(message))
        # shuffled_result = shuffle_text(message, chaotic_sequence)
        enc = ChaoticEncryption(0.01, 3.95, message)
        # message = enc.encryption(shuffled_result)
        message = enc.decryption(message)
        message = reshuffle_text(message,chaotic_sequence)
        return message



    def on_message(message: Message):
        if message.message_type == "chat_message":
            decrypted_message = ChaoticDecrypt(message.text)
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # A dialog asking for a user display name
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )
warnings.filterwarnings("ignore")
ft.app(port=8550, target=main, view=ft.WEB_BROWSER)