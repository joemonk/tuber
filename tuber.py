import sys
import subprocess

def print_help():
    help_text = """
    Usage: python tuber.py <url> [options]

    Options:
    --audio-only       Download only the audio in MP3 format.
    --help             Show this help message and exit.

    Examples:
    python tuber.py https://www.youtube.com/playlist?list=PL1234567890
    python tuber.py https://www.youtube.com/playlist?list=PL1234567890 --audio-only
    """
    print(help_text)

def download(url, audio_only=False):
    # Define the base command
    command = ['yt-dlp']

    # Add format options based on audio_only flag
    if audio_only:
        command += ['-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3']
        output_template = '-o', '%(title)s.%(ext)s'
    else:
        command += ['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4']
        output_template = '-o', '%(playlist_index)s - %(title)s.%(ext)s'

    # Add URL to the command
    command += [output_template, url]

    # Run the command
    subprocess.run(command)

if __name__ == '__main__':
    if len(sys.argv) < 2 or '--help' in sys.argv:
        print_help()
        sys.exit(1)

    url = sys.argv[1]
    audio_only = '--audio-only' in sys.argv

    download(url, audio_only)

