from pathlib import Path
import pickle


class MetadataService:

    def __init__(
        self,
        metadata_path: str = "data/hotel_metadata.pkl",
    ):
        self.metadata_path = Path(
            metadata_path
        )

        self.metadata = None

    def load(self):

        if not self.metadata_path.exists():
            raise FileNotFoundError(
                f"Metadata dosyası bulunamadı: "
                f"{self.metadata_path}"
            )

        with open(
            self.metadata_path,
            "rb",
        ) as file:

            self.metadata = pickle.load(
                file
            )

        print(
            "Metadata successfully loaded."
        )

    def get(self, index: int):

        if self.metadata is None:
            raise RuntimeError(
                "Metadata henüz yüklenmedi."
            )

        return self.metadata.iloc[index]
        
        #print("\n========== METADATA DEBUG ==========")
        #print("Metadata type:", type(self.metadata))
        #print("Metadata shape:", getattr(self.metadata, "shape", None))
        #print("Metadata columns:", getattr(self.metadata, "columns", None))

        #result = self.metadata.iloc[index]

        #print("Result type:", type(result))
        #print("Result index:", getattr(result, "index", None))
        #print("Result:")
        #print(result)
        #print("====================================\n")

        #return result

    def get_many(self, indices):

        return [
            self.get(index)
            for index in indices
        ]

    def get_all(self):

        return self.metadata