import glob
import librosa
import os
import tqdm
import shutil

def split_wav(input_folder, output_folder, threshold):
    shutil.rmtree(output_folder, ignore_errors=True)
    os.makedirs(output_folder, exist_ok=True)
    search_path = os.path.join(input_folder, "*.wav")
    for idx, file_path in tqdm.tqdm(enumerate(glob.glob(search_path))):
        wav, sr = librosa.load(file_path, sr=None)
        intervals = librosa.effects.split(wav, top_db=threshold)
        sub_wav = [wav[itv[0]:itv[1]] for itv in intervals]
        for i, wav in enumerate(sub_wav):
            out_path = os.path.join(output_folder, "{}.{}.wav".format(idx, i))
            librosa.output.write_wav(out_path, sub_wav[i], sr)

if __name__=='__main__':
    split_wav("./public-data/jsut-book_ver1/wav", "./clean_data",threshold=60)