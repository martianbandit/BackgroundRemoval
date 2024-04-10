import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Supprime Arriêre-plan")

st.write("## Cet outils supprime l'arrière plan d'une image que vous télécharger")
st.write(
    ":dog: Essayez de télécharger une image pour voir l’arrière-plan supprimé comme par magie. Des images en pleine qualité peuvent être téléchargées 
    à partir de la barre latérale. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("télécharger votre image sans arrière plan", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("téléchargé une image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("Le fichier téléchargé est trop volumineux. Veuillez télécharger une image inférieure à 5 Mo.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")
