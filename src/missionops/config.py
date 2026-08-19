import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("MISSIONOPS_MODEL", "gpt-5.6")
    api_key: str | None = os.getenv("OPENAI_API_KEY")

settings = Settings()
