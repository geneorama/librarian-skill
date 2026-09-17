"""
Shared config loader for the librarian scripts.

Looks for config/vaults.yaml next to this scripts/ folder; falls back to
config-sample/vaults.yaml so the scripts still run (against placeholder
paths) before real config exists.
"""
import os
import yaml

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPTS_DIR)
REAL_CONFIG = os.path.join(SKILL_ROOT, "config", "vaults.yaml")
SAMPLE_CONFIG = os.path.join(SKILL_ROOT, "config-sample", "vaults.yaml")


def load(path=None):
    path = path or (REAL_CONFIG if os.path.isfile(REAL_CONFIG) else SAMPLE_CONFIG)
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["_source"] = path
    return cfg


def vault_path(cfg, key):
    return cfg["vaults"][key]["path"]
