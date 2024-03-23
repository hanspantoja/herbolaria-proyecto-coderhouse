
from openai import OpenAI
from env import API_KEY

client = OpenAI(api_key=API_KEY)

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

if __name__ == "__main__":
    nombre_planta = "flor de jamaica"
    descripcion_planta = obtener_descripcion_planta(nombre_planta)
    print(f"descripcion planta es: {descripcion_planta}")


