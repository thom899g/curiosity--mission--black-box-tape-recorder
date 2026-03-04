"""
Black Box Tape Recorder Configuration
Centralized configuration management with validation and type hints.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Dict, List
from datetime import datetime
import logging
from pathlib import Path
import json

@dataclass
class BlackBoxConfig:
    """Configuration for the Black Box Tape Recorder system."""
    
    # Core system configuration
    collection_interval_seconds: int = 5
    buffer_size_mb: int = 100
    output_directory: str = "/var/log/blackbox"
    
    # Cryptographic settings
    dna_hash_version: str = "v1.3"
    core_dna_hash: str = field(default_factory=lambda: os.getenv("CORE_DNA_HASH", ""))
    
    # Firebase configuration
    firebase_project_id: str = field(default_factory=lambda: os.getenv("FIREBASE_PROJECT_ID", ""))
    firestore_collection: str = "blackbox_sessions"
    
    # Data collection