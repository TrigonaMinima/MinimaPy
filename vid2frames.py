import sys
import cv2 as cv

from pathlib import Path
from itertools import repeat
from concurrent.futures import ProcessPoolExecutor


cpu_count = cv.getNumberOfCPUs()
data_dir = Path("./data/")
vid_f = data_dir / "vid1.mp4"
frames_dir = Path("./frames/")


def vid2frames_(vid_f, frames_dir, start=0, end=-1):
    cap = cv.VideoCapture(vid_f.as_posix())

    if end < 0:
        end = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    frame = 0
    cap.set(1, start)
    while start < end:
        ret, image = cap.read()

        if not ret:
            break

        if image is None:
            continue

        save_path = frames_dir / f"{frame}.jpg"
        cv.imwrite(save_path.as_posix(), image)

        start += 1
        frame += 1

    cap.release()
    cv.destroyAllWindows()
    return frame


def vid2frames(vid_f, frames_dir, parallel=True):
    cap = cv.VideoCapture(vid_f.as_posix())
    tot_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    print("Total frames -", tot_frames)
    if tot_frames < 1:
        sys.exit()
    cap.release()

    if parallel:
        chunk_s = tot_frames // cpu_count

        start_frame_idx = [start for start in range(0, tot_frames, chunk_s)]
        end_frame_idx = [start + chunk_s for start in range(0, tot_frames, chunk_s)]
        end_frame_idx[-1] = -1

        with ProcessPoolExecutor(max_workers=cpu_count) as executor:

            outs = executor.map(
                vid2frames_,
                repeat(vid_f),
                repeat(frames_dir),
                start_frame_idx,
                end_frame_idx,
            )
            print(f"Created {cpu_count} processes")

            frames_done = 1
            for f in outs:
                frames_done += f
                print(f"Frames saved - {frames_done}/{tot_frames}", end="\r")
            print()
    else:
        out = vid2frames_(vid_f, frames_dir)
        print(f"Frames saved - {out}/{tot_frames}")


if __name__ == "__main__":
    vid2frames(vid_f, frames_dir, parallel=True)
    # vid2frames(vid_f, frames_dir, parallel=False)
