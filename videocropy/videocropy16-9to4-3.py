import sys
import os.path
from moviepy.editor import VideoFileClip

def get_video_resolution(input_file):
    # ビデオファイルを読み込む
    video = VideoFileClip(input_file)

    # 解像度を取得する
    resolution = video.size

    return resolution

def get_output_filename(input_file):
    # 入力ファイル名から拡張子を除いた部分を取得
    file_name, file_ext = os.path.splitext(input_file)

    # 出力ファイル名を設定する
    output_file = f"{file_name}-0{file_ext}"

    return output_file

def crop_video(input_file, output_file):
    # 入力動画の解像度を取得
    input_resolution = get_video_resolution(input_file)
    input_xpx, input_xpy = input_resolution

    # ビデオファイルを読み込む
    video = VideoFileClip(input_file)

    # 16:9から4:3にクロップする
    x1 = (input_xpx - input_xpy * 4/3) / 2
    x2 = x1 + input_xpy * 4/3
    cropped_video = video.crop(x1=x1, x2=x2)

    # 出力ファイル名を取得
    if output_file is None:
        output_file = get_output_filename(input_file)

    # エクスポートする
    cropped_video.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    # コマンドライン引数から入力ファイル名を取得
    if len(sys.argv) != 2:
        print("Usage: cropvideo.py [input_filename]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = None  # 出力ファイル名は自動的に設定する

    crop_video(input_file, output_file)
