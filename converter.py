import imageio
import os

clip = os.path.abspath('video.mp4')
# print(clip)

def gifMaker(inputPath, targetFormat):

    outputPath = os.path.splitext(inputPath)[0] + targetFormat #To get the name of file and to put the deired format name to it.
    print(f"Converting {inputPath} \n to {outputPath}")

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps = fps)

    for frames in reader:
        writer.append_data(frames)
        print(f"Frames {frames}")
    print("Done")
    writer.close()

gifMaker(clip,'.gif')
