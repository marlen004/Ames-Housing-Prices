from pathlib import Path
import logging

def setup_logging():
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        handlers = [
            logging.FileHandler( log_dir / "project.log"),
            logging.StreamHandler()
        ]
    )