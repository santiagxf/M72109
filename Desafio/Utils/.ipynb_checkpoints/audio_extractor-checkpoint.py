```
ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
M72109: Analisis de datos no estructurados
Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
Año: 2020
Profesor: Facundo Santiago
```

import moviepy
import moviepy.editor

def extract_audio_from_videos(root_dir, target_dir):
    """Extrae el audio en formato wav de un conjunto de videos almacenados en el directorio especificado. Los audios son almacenados
    bajo el mismo nombre de cada archivo en un subdirectorio en target_dir llamado audios."""
    for file_ in os.listdir(root_dir):
        video = moviepy.editor.VideoFileClip(os.path.join(root_dir, file_))
        basename = os.path.splitext(os.path.basename(os.path.join(root_dir, file_)))[0]
        video.audio.write_audiofile(os.path.join(target_dir, 'audios', basename + ".wav"), codec='pcm_s16le', verbose=False) # codec='pcm_s16le' para formato wav
        video.close()