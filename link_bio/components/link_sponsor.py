import reflex as rx

from link_bio.styles.styles import Size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(src=imagen, height="3.5em", aspect_ratio="5 / 2", alt=alt),
        href=url,
        is_external=True,
    )


# def link_sponsor(imagen: str, url: str) -> rx.Component:
#     return rx.link(
#         rx.image(height=Size.BIG.value, src=imagen, width="auto"),
#         href=url,
#         is_external=True,
#     )
