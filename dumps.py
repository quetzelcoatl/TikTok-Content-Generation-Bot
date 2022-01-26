isExist = os.path.exists('merged')
if not isExist:
    os.makedirs('merged')
time1 = time.perf_counter()
for x in t1:
    for y in t2:
        file = open('li.txt', 'w')
        x1 = f"mainTemp\{x}"
        y1 = f"outroTemp\{y}"
        file.write("file '{}'\n".format(x1))
        file.write("file '{}'\n".format(y1))
        fname = get_random_string(10)
        q = f'ffmpeg -f concat -safe 0 -i li.txt -c copy merged/{fname}.mp4 '
        try:
            os.system(f"""{q}""")
        except:
            pass


m2 = os.listdir('merged')

for x in musicPathFiles:
    for y in m2:
        x1 = f"{musicPath}\{x}"
        y1 = f" merged\{y}"
        fname = get_random_string(10)
        try:
            os.system(
                f"""ffmpeg -i {y1} -i {x1} -map 0:v -map 1:a -c:v copy -shortest {outputPath}/{fname}.mp4 """)
        except:
            pass
time2 = time.perf_counter()
print("Time taken for Merging and Adding Music is {} sec".format(time2 - time1))
