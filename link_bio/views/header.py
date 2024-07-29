import reflex as rx

import link_bio.constants as url
from link_bio.components.info_text import info_text
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="BS",
                size="8",
                src="avatar.png",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                radius="full",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading("Bastian Saavedra", size="7", color=TextColor.HEADER.value),
                rx.text(
                    "@NoneDev",
                    padding_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon("/nvim.jpg", url.GITHUB_URL, "Logotipo github"),
                    link_icon("/nvim.jpg", url.INSTAGRAM_URL, "Logotipo instagram"),
                    link_icon("/nvim.jpg", url.YOUTUBE_URL, "Logotipo youtube"),
                    link_icon("/nvim.jpg", url.SPOTIFY_URL, "Logotipo spotify"),
                    link_icon("/nvim.jpg", url.LINKEDIN_URL, "Logotipo Linkedin"),
                ),
                align_items="start",
            ),
            gap=Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("+1", "Experience years"),
            rx.spacer(),
            info_text("+100", "Juegos"),
            rx.spacer(),
            info_text("-99", "Vida"),
            width="100%",
        ),
        rx.text(
            """
            Soy un programador recien titulado y quiero realizar 
            soluciones a multiples negocios y small empresas
            Soy un programador recien titulado y quiero realizar 
            soluciones a multiples negocios y small empresas
            Soy un programador recien titulado y quiero realizar 
            soluciones a multiples negocios y small empresas
            """,
            color=TextColor.BODY.value,
        ),
        gap=Size.BIG.value,
        align_items="start",
    )
