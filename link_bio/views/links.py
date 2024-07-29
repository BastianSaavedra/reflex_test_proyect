import reflex as rx

import link_bio.constants as url
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Github", "mis proyectos", url.GITHUB_URL, "Github button"),
        link_button("Youtube", "premium oooh yeah", url.YOUTUBE_URL, "Youtube button"),
        title("Recursos"),
        link_button(
            "Dotfiles",
            "Mis archivos configurados de las herramientas que utilizo",
            url.DOTFILES,
            "Dotfiles button",
        ),
        link_button("Youtube", "premium oooh yeah", url.YOUTUBE_URL, "Youtube button"),
        width="100%",
    )
