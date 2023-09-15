"""video_classification_dataset dataset."""

import pathlib
import tensorflow_datasets as tfds
from tensorflow_datasets.core import utils
from typing import Iterator, Tuple, Dict, Optional, Any

_DESCRIPTION = """
  A simple classification dataset for video
"""

# TODO(video_classification_dataset): BibTeX citation
_CITATION = """
"""


class VideoClassificationDataset(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({
            'video': tfds.features.Video(shape=(None, 320, 240,3)),
            'label': tfds.features.ClassLabel(names=['PlayingGuitar', 'PlayingViolin', 'PlayingCello']),
        }),
        supervised_keys=('video', 'label'),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract('https://santiagxf.blob.core.windows.net/public/datasets/UCF-3.zip')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'path': extracted_path },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'path': extracted_path },
        )
    ]

  def _generate_examples(self, path):
    for video_path in path.glob('*/*.avi'): # video_path: PosixPath
      yield video_path.name, {
          'video': video_path,
          'label': str(video_path.parent.name),
      }