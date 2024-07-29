import reflex as rx


# lang
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


# comun
preview = "https://github.com/BastianSaavedra"
meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]

# index
index_title = "NoneDev | Mi primera pagina web con Reflex"
index_description = "Hola mi nombre es Bastian Saavedra. Soy ingeniero informatico, desarrollador freelance full-stack"
meta_index = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
meta_index.extend(meta)

# Courses
courses_title = "NoneDev | Cursos gratis"
courses_description = (
    "Este es un listado con algunos cursos gratis para aprender programacion"
)

meta_courses = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
meta_courses.extend(meta)
