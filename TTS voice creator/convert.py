import tarfile
import hashlib
import os
import subprocess
import sys
import shutil
import glob

# Nederlandse stemopties
voice_options = ["Fenna", "Maarten"]

# Stem kiezen via argument of input
if len(sys.argv) > 1:
    voice = sys.argv[1].capitalize()
else:
    voice = input(f"Kies een stem ({'/'.join(voice_options)}): ").capitalize()

# Controleer of de stem geldig is
if voice not in voice_options:
    raise ValueError(f"Ongeldige stem. Kies uit: {', '.join(voice_options)}.")

current_directory = os.getcwd()
input_folder    = os.path.join(current_directory, voice.lower())
output_folder   = os.path.join(current_directory, f'{voice.lower()}-ogg')
sound_ogg_folder = os.path.join(current_directory, 'sound-ogg')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# WAV bestanden verwerken: normaliseren en converteren naar OGG
for filename in os.listdir(input_folder):
    if filename.endswith('.wav'):
        wav_file = os.path.join(input_folder, filename)
        tmp_file = os.path.join(output_folder, filename.replace('.wav', '_temp.wav'))
        ogg_file = os.path.join(output_folder, filename.replace('.wav', '.ogg'))

        subprocess.run([
            "ffmpeg", "-y",
            "-i", wav_file,
            "-filter:a", "speechnorm=p=0.95:e=2.0:c=2.0:t=0.0:r=0.001",
            tmp_file
        ])
        subprocess.run([
            "oggenc",
            tmp_file,
            "--output", ogg_file,
            "--bitrate", "56",
            "--resample", "16000"
        ])
        os.remove(tmp_file)

# Inhoud van sound-ogg kopiëren (niet-TTS geluiden)
if os.path.exists(sound_ogg_folder):
    for filename in os.listdir(sound_ogg_folder):
        source_file      = os.path.join(sound_ogg_folder, filename)
        destination_file = os.path.join(output_folder, filename)
        shutil.copy(source_file, destination_file)

# Tijdelijke s*.ogg plaatshouders verwijderen
for filepath in glob.glob(os.path.join(output_folder, 's*.ogg')):
    os.remove(filepath)

# Inpakken als tar.gz
tar_gz_filename = os.path.join(current_directory, f'{voice.lower()}-ogg.tar.gz')
with tarfile.open(tar_gz_filename, "w:gz") as tar:
    for filename in os.listdir(output_folder):
        tar.add(os.path.join(output_folder, filename), arcname=filename)

# MD5 hash en bestandsgrootte berekenen
hash_md5 = hashlib.md5()
with open(tar_gz_filename, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)

md5_hash  = hash_md5.hexdigest()
file_size = os.path.getsize(tar_gz_filename)

# Resultaat opslaan in tekstbestand
output_txt_file = tar_gz_filename + '.txt'
with open(output_txt_file, 'w') as f:
    f.write(f"MD5 hash: {md5_hash}\n")
    f.write(f"Bestandsgrootte: {file_size} bytes\n")

print(f"Klaar! MD5: {md5_hash} | Grootte: {file_size} bytes")
