from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    ):

        self.model_name = model_name

        self.model = SentenceTransformer(
            model_name
        )

    def encode(
        self,
        text: str,
    ) -> np.ndarray:

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype(
            np.float32
        )

    def encode_many(
        self,
        texts: List[str],
    ) -> np.ndarray:

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

        return embeddings.astype(
            np.float32
        )