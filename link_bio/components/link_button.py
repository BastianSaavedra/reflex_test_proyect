import reflex as rx

from link_bio.styles import styles
from link_bio.styles.styles import Size, Spacing


def link_button(title: str, body: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src="/nvim.jpg",
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=alt,
                ),
                rx.vstack(
                    rx.text(
                        title, size=Spacing.SMALL.value, style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        size=Spacing.VERY_SMALL.value,
                        style=styles.button_body_style,
                    ),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                align="center",
                width="100%",
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
