from pathlib import Path

import faiss
import numpy as np


class VectorSearchService:

    def __init__(
        self,
        index_path: str = "data/hotel_multilingual_faiss.index",
    ):
        self.index_path = Path(index_path)
        self.index = None

    def load(self):
        if not self.index_path.exists():
            raise FileNotFoundError(
                f"FAISS index bulunamadı: "
                f"{self.index_path}"
            )

        self.index = faiss.read_index(
            str(self.index_path)
        )

        print(
            f"FAISS index loaded: "
            f"{self.index.ntotal} vectors"
        )

    def search(
        self,
        query_vector: np.ndarray,
        top_k: int = 10,
    ):
        if self.index is None:
            raise RuntimeError(
                "FAISS index henüz yüklenmedi."
            )

        query_vector = np.asarray(
            query_vector,
            dtype=np.float32,
        )

        if query_vector.ndim == 1:
            query_vector = query_vector.reshape(
                1, -1
            )

        # Dataset'in normalize edilmiş
        # embedding kullandığını varsayıyoruz.
        scores, indices = self.index.search(
            query_vector,
            top_k,
        )

        return scores[0], indices[0]