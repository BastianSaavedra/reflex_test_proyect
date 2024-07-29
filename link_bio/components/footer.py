import datetime

import reflex as rx

from link_bio.styles.colors import TextColor
from link_bio.styles.styles import Size, Spacing


def footer() -> rx.Component:
    return rx.vstack(
        rx.center(rx.image(src="favicon.ico"), width="100%"),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        f"© {datetime.date.today().year} Nonedev by",
                        font_size=Size.MEDIUM.value,
                    ),
                    rx.link(
                        "Bastian Saavedra.",
                        href="https://github.com/BastianSaavedra",
                        is_external=True,
                        font_size=Size.MEDIUM.value,
                    ),
                ),
            ),
            width="100%",
            margin_bottom=Size.ZERO.value,
        ),
        rx.text(
            "BUILDING DREAMS WITH ❤ FROM SANTIAGO TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.MEDIUM_BIG.value,
        color=TextColor.FOOTER.value,
    )
