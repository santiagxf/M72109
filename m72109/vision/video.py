from typing import List, Dict, Tuple, Any
from transformers.modeling_utils import PreTrainedModel
from transformers.modeling_utils import BaseImageProcessor

import numpy as np
import tqdm as tqdm
import torch

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
            predicted_prob = torch.nn.functional.softmax(logits, dim=1)[0]
            predicted_label = logits.argmax(-1).item()
        
        predictions.append({
            "frames": [i, i + chunk_size],
            "class": predicted_label,
            "probability": predicted_prob,
            "label": model.config.id2label[predicted_label]
        })

    return predictions
