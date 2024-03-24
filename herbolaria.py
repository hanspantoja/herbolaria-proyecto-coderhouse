import os 
import streamlit    as st 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),)

def obtener_descripcion_planta(nombre_planta):
    prompt = f"genera un parrafo con la descripcion de la planta, un parrafo con sus caracteristicas, un parrafo con sus beneficios a la salud y un parrafo con su modo de uso {nombre_planta}:"
    
    response = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )

    descripcion_planta = response.choices[0].message.content

    return descripcion_planta

st.write("# Herbolaria") 

name = st.text_input(label="", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Nombre de planta", disabled=False, label_visibility="visible")

if st.button(label="info", key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False):
    st.write(obtener_descripcion_planta(name))

