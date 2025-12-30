from typing import List, Dict, Tuple, Any
from transformers.modeling_utils import PreTrainedModel
from transformers.modeling_utils import BaseImageProcessor

import cv2
import numpy as np
import tqdm as tqdm
import torch

def load_video_frames(video_path: str) -> np.ndarray:
    """
    Carga los frames de un video en un array de NumPy.
    
    Args:
        video_path: Ruta al video.
    
    Returns:
        Un array de NumPy con los frames del video de deimensiones (frames, channels, height, width)
    """
    
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    
    # Utilizamos `np.moveaxis` ya que Torch espera las imagenes que sean channel first.
    # (frames, 3, 406, 720) -> (frames, 3, 406, 720)
    return np.moveaxis(np.asarray(frames), 3, 1)

def embed_video(image_processor: BaseImageProcessor, model: PreTrainedModel, frames: np.ndarray, chunk_size: int = 16, stride: int = 8) -> torch.Tensor:
    embedding_sequence = []
    
    for i in tqdm(range(0, len(frames) - chunk_size + 1, stride)):
        chunk = frames[i : i + chunk_size]
        
        inputs = image_processor(list(chunk), return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model(**inputs)
            chunk_embedding = outputs.last_hidden_state.mean(dim=1)
            embedding_sequence.append(chunk_embedding)

    return torch.cat(embedding_sequence, dim=0)

def classify_video(image_processor: BaseImageProcessor, model: PreTrainedModel, frames: np.ndarray, chunk_size: int = 16, stride: int = 8) -> List[Dict[str, Any]]:
    """
    Classifies the video
  
    Args:
      image_processor: The image processor
      model: The model
      frames: The frames of the video, in channel first format
      chunk_size: The amount of frames the model can process at once
      stride: The stride to use to move across the frames for segmenting 
        the video. If `stride < chunk_size`, then a rolling window will be used.
  
    Returns:
      A list of dictionaries
  
    Example:
      >>> classify_video(image_processor, model, frames, chunk_size=16, stride=8)
    """
    predictions = []
    
    for i in tqdm(range(0, len(frames) - chunk_size + 1, stride)):
        chunk = frames[i : i + chunk_size]
        
        inputs = image_processor(list(chunk), return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_prob = torch.nn.functional.softmax(torch.max(logits), dim=-1).item()
            predicted_label = logits.argmax(-1).item()
        
        predictions.append({
            "frames": [i, i + chunk_size],
            "class": predicted_label,
            "probability": predicted_prob,
            "label": model.config.id2label[predicted_label]
        })

    return predictions
