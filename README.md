# Traductor Multi-idioma de Voz

Este proyecto se enfoca en el procesamiento de audio en español, proporcionando la capacidad de traducirlo a varios idiomas, incluyendo inglés, italiano, francés y japonés. El sistema devuelve el resultado traducido en formato de audio, generado mediante inteligencia artificial de voz, ofreciendo una experiencia eficiente y precisa en la conversión de texto a voz.

## Librerias

Para ejecutar este proyecto, es necesario configurar varias variables de entorno, las cuales son:

`gradio`
`openai-whisper`
`translate`
`python-dotenv`
`elevenlabs`

A continuación, se proporcionan los enlaces a los sitios oficiales de las herramientas utilizadas, aunque también se mencionan brevemente en la documentación del código:

- [Gradio](https://gradio.app)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Translate](https://pypi.org/project/translate/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [Elevenlabs](https://www.elevenlabs.io)

## Capturas de Pantalla

![WEB](https://github.com/user-attachments/assets/11378186-cad9-42ef-a71b-43d0ba8d7938)


## Ejecución Local

Clona el proyecto:

```powershell
git clone https://github.com/Martin-S-Romero/Traductor_multi-idioma.git
```

Accede al directorio del proyecto:

```powershell
cd Traductor_multi-idioma
```

Crea un entorno virtual:

```powershell
python -m venv {nombre-del-entorno-virtual}
```

Inicia el entorno virtual:

```powershell
.\{nombre-del-entorno-virtual}\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r .\requirements.txt
```

**¡Listo!**

_NOTA: Es posible que necesites instalar ffmpeg._

## Lección Aprendida

El mayor reto durante la realización de este proyecto fue comprender y dominar las diversas herramientas involucradas. En particular, tuve la oportunidad de conocer **Gradio**, una biblioteca de Python que facilita la creación de interfaces web interactivas sin la necesidad de recurrir a frameworks de desarrollo web tradicionales. Esto me permitió simplificar el proceso de construcción de la interfaz y enfocar mis esfuerzos en otras áreas del proyecto. Además, fue especialmente enriquecedor explorar las capacidades de la inteligencia artificial aplicada a la conversión de texto a voz, lo que añadió un elemento innovador y dinámico a la solución. A lo largo del desarrollo, pude profundizar en la integración de tecnologías avanzadas para ofrecer una experiencia fluida y efectiva al usuario.

## Futuras Mejoras

- Despliegue en la nube.
- Selección de idiomas adicionales.
- Carga de archivos de audio.
- Corrección de ortografía en los comentarios del código.
- Visualización de la traducción.

## Autores

- [@mouredev](https://github.com/mouredev)
- [@Martin-S-Romero](https://github.com/Martin-S-Romero)  
  (La base del código es de otro autor, pero con las actualizaciones me he ganado el crédito de "autor" 😄)

## Agradecimientos

- [mouredev/voice_translator.py - GitHub Gist](https://gist.github.com/mouredev/0ea42112751f0187d90d5403d1f333e2)
- [Traductor de Voz con PYTHON e IA en 100 líneas - YouTube](https://youtu.be/oxLvf2nDCvQ)
- [Create a Simple Voice-to-Voice Translation App with Python - Medium (Artículo original)](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Feedback

Si tienes alguna retroalimentación, no dudes en contactarme al correo: martin.sh.romero@gmail.com
