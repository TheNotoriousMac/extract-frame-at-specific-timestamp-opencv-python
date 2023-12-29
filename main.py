import cv2

video = cv2.VideoCapture('video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

# print(width, height, nr_frames, fps)

# duration = nr_frames/fps
# print(duration)

timestamp = input("Enter timestamp in hh:mm:ss format: ")

timestamp_list = timestamp.split(':')
# print(timestamp_list)

timestamp_list_floats = [float(i) for i in timestamp_list]
hours, minutes, seconds = timestamp_list_floats
# print(hours, minutes, seconds)

frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nr)
success, frame = video.read()

cv2.imwrite(f'Frame.jpg', frame)

# success, frame = video.read()
#
#
# count = 1
# while success:
#     cv2.imwrite(f'images/{count}.jpg', frame)
#     success,frame = video.read()
#     count += 1