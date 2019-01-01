import ffmpy, os, datetime


def compress_video(file_name):
    print(f"Compressing {file_name}...")
    inputs = {file_name: None}
    output_file_name = file_name[0:file_name.rfind(".")] + "_compressed" + file_name[file_name.rfind("."):]
    outputs = {output_file_name: None}

    ff = ffmpy.FFmpeg(inputs=inputs, outputs=outputs)
    ff.run()

    print(f"[{datetime.datetime.now()}] Finished compressing {file_name}. Output filename: {output_file_name}")


def walk_directories(starting_directory):
    for root, dirs, files in os.walk(starting_directory):
        for filename in files:
            compress_video(f"{root}\\{filename}")
        for dir in dirs:
            walk_directories(dir)


def compile_file_list(starting_directory):
    file_names = []
    for root, dirs, files in os.walk(starting_directory):
        for filename in files:
            file_names.append(f"{root}\\{filename}")
        # for dir in dirs:
        #   for file in compile_file_list(dir):
        #      files.append(file)
    return file_names


# starting folder goes here. Every file under folder will get picked up (even in sub-folders)
starting_location = input("Please enter a folder location to start compressing")

start_time = datetime.datetime.now()
print(f"[{start_time}] Starting compression run")

file_names = compile_file_list(starting_location)
total_files = len(file_names)

print(f"[{datetime.datetime.now()}] Files left to compress: {total_files}")

i = 0
for file_name in file_names:
    compress_video(file_name)
    i = i + 1
    percent = (i / total_files) * 100
    # print (f"{percent:6.2f}% completed")
    print(f"[{datetime.datetime.now()}] {i}/{total_files} files compressed - {round(percent, 2)}% completed")

end_time = datetime.datetime.now()
print(
    f"[{end_time}] Finished compression run. Total files compressed: {total_files}. Time taken: {end_time - start_time}")
