import os
import requests
import zipfile
from pathlib import Path

def download_data():
    """Download sample TREC data for AURA pipeline"""
    
    data_dir = Path("data")
    
    # Check if data already exists
    if data_dir.exists() and any(data_dir.iterdir()):
        print(" Data already present! No download needed.")
        return
    
    print(" Downloading AURA sample data from GitHub Releases...")
    
    download_url = "https://github.com/anitaxokojie/AURA-Legal-Framework/releases/download/v1.0-data/aura_sample_data.zip""
    
    zip_path = Path("aura_sample_data.zip")
    
    print(" Downloading...")
    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    progress = (downloaded / total_size) * 100
                    print(f"Progress: {progress:.1f}%", end='\r')
        
        print("\n Extracting files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        zip_path.unlink()
        
        print(" Data setup complete!")
        print(f"   └─ Created data/ folder with {len(list(data_dir.glob('*')))} matter folders")
    
    except Exception as e:
        print(f" Error downloading data: {e}")
        print("\nManual download instructions:")
        print("1. Visit: https://github.com/anitaxokojie/AURA-Legal-Framework/releases")
        print("2. Download aura_sample_data.zip")
        print("3. Extract it in this directory")

if __name__ == "__main__":
    download_data()
