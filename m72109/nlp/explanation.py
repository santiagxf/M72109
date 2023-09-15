from typing import Tuple, List
from eli5.base import Explanation, TargetExplanation, FeatureWeights, FeatureWeight, WeightedSpans, DocWeightedSpans

import numpy as np

def locate_token(token: str, token_idx: int, tokenized_text: List[str]) -> List[Tuple[int, int]]:
    str_to_token = ' '.join(tokenized_text[:token_idx + 1]).replace(" ##", '')
    str_to_token = str_to_token.replace("[CLS] ", '')
    striped_token = token.replace("##", '')

    return [tuple([len(str_to_token) - len(striped_token) - 1, len(str_to_token) - 1])]

def get_explanation_from_grads(estimator_name: str,
                               estimator_description: str,
                               text: str,
                               tokens: List[str],
                               grads: np.ndarray,
                               probas: np.ndarray,
                               labels: List[str],
                               force_weights: bool = False):
    """
    Gets the explanation for a text instance from the gradients

    Parameters
    ----------
    estimator_name : str
        Name of the estimator
    estimator_description : str
        Description of the estimator
    text : str
        Text you want to explain
    tokens : List[str]
        Tokens of the text indicated.
    grads : np.ndarray
        Gradients of the output with respect to each token
    probas : np.ndarray
        Probablities for each class
    labels : List[str]
        Labels for each class

    Returns
    -------
    Explanation
        The explanation
    """
    if force_weights:
        weights = FeatureWeights(pos=[FeatureWeight(token, grads[idx]) for idx, token in enumerate(tokens)], neg=[])
    else:
        weights = FeatureWeights(pos=[FeatureWeight("Highlighted in text", weight=np.array(grads).sum(), value=0)], neg=[])
    return Explanation(estimator=estimator_name,
                       description=estimator_description,
                       targets=[
                           TargetExplanation(target=labels[probas.argmax()],
                                             feature_weights=weights,
                                             proba=probas.max(),
                                             weighted_spans=WeightedSpans(
                                                 [ DocWeightedSpans(text, 
                                                                    spans=[(token, locate_token(token, idx, tokens), grads[idx]) for idx, token in enumerate(tokens)])
                                                 ]
                                            ))])