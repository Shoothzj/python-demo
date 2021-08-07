from pathlib import Path

import yaml


def read_hc_config():
    home = str(Path.home()) + "/.sh/hc.yaml"
    with open(home) as f:
        data_map = yaml.safe_load(f)
        return data_map
