"""Create experiment records with useful run metadata."""

from datetime import datetime, timezone
import platform
import uuid
from typing import Any


def create_experiment_record(
    *,
    task_name: str,
    task_version: str,
    model: str,
    prompt_version: str,
    config: dict[str, Any],
    code_version: str,
    results: dict[str, Any],
) -> dict[str, Any]:
    """Create a timestamped experiment record with environment details."""

    text_fields = {
        "task_name": task_name,
        "task_version": task_version,
        "model": model,
        "prompt_version": prompt_version,
        "code_version": code_version,
    }

    for field, value in text_fields.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} must be a non-empty string")

    if not isinstance(config, dict):
        raise TypeError("config must be a dictionary")

    if not isinstance(results, dict):
        raise TypeError("results must be a dictionary")

    if not results:
        raise ValueError("results must not be empty")

    return {
        "experiment_id": str(uuid.uuid4()),
        "task_name": task_name,
        "task_version": task_version,
        "model": model,
        "prompt_version": prompt_version,
        "config": config,
        "code_version": code_version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "python_version": platform.python_version(),
            "operating_system": platform.platform(),
        },
        "results": results,
    }
