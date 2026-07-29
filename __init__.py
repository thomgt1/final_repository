# Importar las funciones principales para facilitar el acceso
from .emotion_detection import emotion_detector, emotion_predictor

# Definir qué se exporta cuando se usa "from package import *"
__all__ = ['emotion_detector', 'emotion_predictor']
