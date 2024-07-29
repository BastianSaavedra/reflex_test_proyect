import reflex as rx

import link_bio.styles.styles as styles
from link_bio.components.ant_components import float_button
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "none",
                rx.text.span("dev", color=Color.SECONDARY.value),
                as_="span",
                color=Color.PRIMARY.value,
            ),
            style=styles.navbar_title_style,
        ),
        # float_button(icon=rx.image(src="/nvim.jpg"), href="https://google.com"),
        float_button(icon=rx.image(src="/nvim.jpg"), url="https://google.com"),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
