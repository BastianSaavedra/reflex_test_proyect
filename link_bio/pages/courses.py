import reflex as rx

import link_bio.styles.styles as styles
import link_bio.views.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.routes import Route
from link_bio.views.header import header
from link_bio.views.links import links


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    meta=utils.meta_courses,
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT.value,
                padding=styles.Size.BIG.value,
            ),
        ),
        rx.center(
            footer(),
        ),
    )
