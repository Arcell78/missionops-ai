from __future__ import annotations
import time
from openai import OpenAI

from .config import settings
from .prompts import SYSTEM_INSTRUCTIONS
from .schemas import IncidentTriage

def get_client() -> OpenAI:
    if not settings.api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env or export "
            "OPENAI_API_KEY in your environment."
        )
    return OpenAI(api_key=settings.api_key)

def triage_incident(
    incident_description: str,
    *,
    client: OpenAI | None = None,
    model: str | None = None,
) -> tuple[IncidentTriage, float]:
    if not incident_description.strip():
        raise ValueError("incident_description cannot be empty")

    client = client or get_client()
    model = model or settings.model
    started = time.perf_counter()

    response = client.responses.parse(
        model=model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=incident_description.strip(),
        text_format=IncidentTriage,
    )

    elapsed = time.perf_counter() - started

    if response.output_parsed is None:
        raise RuntimeError("The response did not contain parsed structured output.")

    return response.output_parsed, elapsed
