# Video & Audio Downloader with Merging Feature

## 📌 Overview
This application allows users to download videos and audio from various platforms including YouTube, Spotify, and Facebook. Additionally, it merges video and audio files into a single file when necessary.

## 🚀 Features
- Download YouTube videos in different resolutions (with or without audio)
- Download YouTube audio files (MP3 format)
- Download and merge video and audio streams for better quality
- Download entire YouTube playlists
- Download songs from Spotify
- Download videos from Facebook
- GUI developed using **PySide6**

## 🛠️ Installation
### 1️⃣ Install Python Dependencies
Ensure you have **Python 3.9+** installed, then install required packages:
```sh
pip install -r requirements.txt
```

### 2️⃣ Required External Libraries
Make sure **UniConvertor** is installed for handling **cairosvg**:
- Download and install UniConvertor from: [https://sk1project.net/uc2/](https://sk1project.net/uc2/)
- Add `C:/Program Files/UniConvertor-2.0rc5/dlls` to your system PATH manually if needed

## 🎬 How to Use
1. **Run the application**
   ```sh
   python main.py
   ```
2. **Select the platform** (YouTube, Spotify, or Facebook)
3. **Enter the video/audio URL**
4. **Choose the download resolution (for YouTube videos)**
5. **Select the output folder**
6. **Click the download button**
7. **Wait for the process to complete**

## 🎵 YouTube Video & Audio Merging
- If the selected YouTube video format doesn't have audio, the program downloads the best available **video** and **audio** separately.
- It then merges them using `moviepy` and saves the final output.

## 🔧 Configuration
Modify the API keys for Spotify in the `spotify_download` function if needed:
```python
obj = Spotdl(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", no_cache=True)
```

## ❗ Troubleshooting
- **Error: `libcairo-2.dll not found`**
  - Ensure that the **UniConvertor** library is installed and the DLL path is correctly set.

- **YouTube video download fails**
  - The selected resolution might not be available. Try another resolution.

- **Spotify download issues**
  - Ensure the correct `client_id` and `client_secret` are set.

- **Facebook videos not downloading**
  - Ensure the provided link is correct and public.

## 📝 License
This project is licensed under the MIT License. Feel free to use and modify it!

