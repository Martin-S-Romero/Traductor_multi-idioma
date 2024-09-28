import gradio as gr
# https://www.gradio.app/
"""Gradio es una libreria que permite crear interfaces de usuario web, no es en si un framework de desarrollo web, 
es mas bien una herramienta para crear interfaces de usuario web de manera rapida y sencilla, 
sin necesidad de tener conocimientos de desarrollo web, ya que se encarga de todo el proceso de creación de la interfaz web, 
solo se necesita definir la logica de la aplicación y gradio se encarga de crear la interfaz web."""
import whisper
# https://github.com/openai/whisper
"""Whisper es un modelo de IA que convierte voz a texto desarrollado por openAI,
esta libreria permite usar el modelo de IA de whisper de manera local, hay una version que puede usar la API para que el proceso sea mas 
rapido, pero en esta ocacion usaremos la version local, ya que es mas sencillo de usar y no requiere de una cuenta en openAI para usarlo."""
from translate import Translator
# https://pypi.org/project/translate/
"""Translate es una libreria que permite traducir texto de un idioma a otro, esto lo hace sin necesidad de una API, usa el traductor de 
google para realizar la traducción, es una libreria muy sencilla de usar y no requiere de una cuenta para usarla."""
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
# https://github.com/elevenlabs/elevenlabs-python
"""ElevenLabs es una libreria que permite usar la API de elevenlabs para generar audio a partir de texto, esta bien documentada y es 
muy sencilla de usar."""

"""NOTA: para usar la libreria de translate se necesita una API_KEY, una buena practica es usar un .env para guardar la API_KEY
TRADUCTOR_API_KEY = "dkjalkjvblkjsableiulkjdbsckbalkkj321dsad"
se puede usar la libreria python-dotenv para cargar las variables de entorno desde un archivo .env y asi nuestra KEY no esta expuesta"""
from dotenv import dotenv_values
# https://pypi.org/project/python-dotenv/
config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["APIKEY_elevenlabs"]



def translator(audio_file):
    # 1. Tasformar el audio a texto con IA
    # https://www.assemblyai.com/ esta es una alternativa
    # En esta ocacion usaremo whisper.ai
    try:
        # en la documentacion se muestran varios tipos de modelos que se pueden usar, en este caso usaremos el modelo base
        model = whisper.load_model("base")
        # aqui se pararia el audio a texto y le decimos el idioma del audio, en mi paso y por ahora solo se puede usar el idioma español
        # esto sera una futura modificacion para que el usuario pueda elegir el idioma 
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error transcribiendo el texto: {str(e)}")

    print(f"Texto original: {transcription}")

    # 2. Traducir el texto a otro idioma
    # en este caso se traducira el texto a ingles con el parametro de to_lang="en"

    try:
        en_transcription = Translator(
            from_lang="es", to_lang="en").translate(transcription)
        it_transcription = Translator(
            from_lang="es", to_lang="it").translate(transcription)
        fr_transcription = Translator(
            from_lang="es", to_lang="fr").translate(transcription)
        ja_transcription = Translator(
            from_lang="es", to_lang="ja").translate(transcription)
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error traduciendo el texto: {str(e)}")

    print(f"Texto traducido a Inglés: {en_transcription}")
    print(f"Texto traducido a Italiano: {it_transcription}")
    print(f"Texto traducido a Francés: {fr_transcription}")
    print(f"Texto traducido a Japonés: {ja_transcription}")

    # 3. Generar audio en base al texto traducido
    # https://elevenlabs.io/  esta si usa una API para generar el audio, tiene una version gratuita con ciertas limitaciones
    # https://elevenlabs.io/docs/api-reference/getting-started Esta seria la documentacion
    en_save_file_path = text_to_speach(en_transcription, "en")
    it_save_file_path = text_to_speach(it_transcription, "it")
    fr_save_file_path = text_to_speach(fr_transcription, "fr")
    ja_save_file_path = text_to_speach(ja_transcription, "ja")
    

    return en_save_file_path, it_save_file_path, fr_save_file_path, ja_save_file_path


def text_to_speach(text: str, language: str) -> str:

    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        # Para entender los parametros de la funcion convert se puede ver la documentacion de la libreria elevenlabs
        response = client.text_to_speech.convert(
            voice_id="GBv7mTt0atIp3Br8iCZE",  # Thomas (Legacy)
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
        # Damos la ruta donde se guardara el archivo de audio
        save_file_path = f"./audios/{language}.mp3"
        # al ser un archivo de audio se guarda en binario por eso la B, y al ser binario se guarda por chunks que son partes del archivo
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error creando el audio: {str(e)}")

    return save_file_path


web = gr.Interface(
    # nombre de la función que tiene la logica
    fn=translator,
    inputs=gr.Audio(
        # se define que proviene de un microfono
        sources=["microphone"],
        # se define que el tipo es solo la dirección del archivo
        type="filepath",
        # se define el label del input para que el user entienda que es lo que se espera
        label="Español"
    ),
    outputs=[
        gr.Audio(label="Inglés"), #salida de la traducción en ingles
        gr.Audio(label="Italiano"), #salida de la traducción en italiano
        gr.Audio(label="Francés"), #salida de la traducción en francés
        gr.Audio(label="Japonés") #salida de la traducción en japonés
    ],
    # se define el titulo de la interfaz
    title="Traductor de voz",
    # se define la descripción de la interfaz
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()