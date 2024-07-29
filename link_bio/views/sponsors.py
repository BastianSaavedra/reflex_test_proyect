import reflex as rx

import link_bio.constants as const
from link_bio.components.link_sponsor import link_sponsor
from link_bio.components.title import title
from link_bio.styles.styles import Spacing


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor("nvim.jpg", const.GITHUB_URL, "Logotipo de github"),
            link_sponsor("nvim.jpg", const.SPOTIFY_URL, "Logotipo de Spotify"),
            spacing=Spacing.BIG.value,
            flex_direction=["column", "row"],
        ),
        width="100%",
        align_items="start",
        spacing=Spacing.MEDIUM_BIG.value,
    )
