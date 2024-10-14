from pathlib import Path
import os


PROJECT_DIR = os.path.abspath(os.path.join(os.getcwd()))
MEDIA_PATH = os.path.join(PROJECT_DIR, 'media')
TEMP_PATH = os.path.join(PROJECT_DIR, 'temp')
VCF_PATH = os.path.join(MEDIA_PATH, 'vcf')
HOST = "https://qrconnecta.com"