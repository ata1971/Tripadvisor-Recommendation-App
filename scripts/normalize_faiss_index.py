from pathlib import Path

import faiss
import numpy as np


SOURCE_PATH = Path(
    "data/hotel_multilingual_faiss.index"
)

TARGET_PATH = Path(
    "data/hotel_multilingual_faiss_normalized.index"
)

BATCH_SIZE = 10_000


if TARGET_PATH.exists():
    raise FileExistsError(
        f"Hedef dosya zaten mevcut: {TARGET_PATH}"
    )


print("Eski FAISS indeksi yükleniyor...")

source_index = faiss.read_index(
    str(SOURCE_PATH)
)

print("Vektör sayısı:", source_index.ntotal)
print("Embedding boyutu:", source_index.d)


normalized_index = faiss.IndexFlatL2(
    source_index.d
)


for start in range(
    0,
    source_index.ntotal,
    BATCH_SIZE,
):
    count = min(
        BATCH_SIZE,
        source_index.ntotal - start,
    )

    vectors = source_index.reconstruct_n(
        start,
        count,
    )

    vectors = np.ascontiguousarray(
        vectors,
        dtype=np.float32,
    )

    faiss.normalize_L2(vectors)

    normalized_index.add(vectors)

    print(
        f"{start + count:,} / "
        f"{source_index.ntotal:,} tamamlandı"
    )


print("Yeni indeks kaydediliyor...")

faiss.write_index(
    normalized_index,
    str(TARGET_PATH),
)

print("İşlem tamamlandı.")
print("Yeni dosya:", TARGET_PATH)
print(
    "Yeni vektör sayısı:",
    normalized_index.ntotal,
)