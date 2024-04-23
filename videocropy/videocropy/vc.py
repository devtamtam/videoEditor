import sys
from moviepy.editor import VideoFileClip

def get_video_resolution(input_file):
    # ビデオファイルを読み込む
    video = VideoFileClip(input_file)

    # 解像度を取得する
    resolution = video.size

    return resolution

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

    # エクスポートする
    cropped_video.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    # コマンドライン引数から入力ファイル名と出力ファイル名を取得
    if len(sys.argv) != 3:
        print("Usage: cropvideo.py [input_filename] [output_filename]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    crop_video(input_file, output_file)
