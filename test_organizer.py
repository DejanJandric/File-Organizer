import pytest
from pathlib import Path
from auto_moving_files import organize_downloads

def test_organize_files(tmp_path):
    """
    tmp_path is a built-in pytest fixture that creates a 
    temporary folder unique to this test run.
    """
    
    (tmp_path / "test_image.png").touch()
    (tmp_path / "test_doc.pdf").touch()
    (tmp_path / "test_installer.exe").touch()
    (tmp_path / "unknown_file.xyz").touch()


    moved_count = organize_downloads(tmp_path)

    
    assert moved_count == 3  

    
    assert (tmp_path / "Photos" / "test_image.png").exists()
    assert (tmp_path / "Documents" / "test_doc.pdf").exists()
    assert (tmp_path / "Installations" / "test_installer.exe").exists()
    
  
    assert (tmp_path / "unknown_file.xyz").exists()
