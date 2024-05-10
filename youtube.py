from pytube import YouTube

#url = 'https://www.youtube.com/live/_HLkBMSBumg?si=twIvVF0LgRqyDKZt'
def download_video(url, output_path=None):
    try:
        print("Downloading video...")
        yt = YouTube(url)

        # Seleciona a melhor resolução disponível
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if output_path is None:
            output_path = video_stream.default_filename

        video_stream.download(output_path)
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)

if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    download_video(video_url)