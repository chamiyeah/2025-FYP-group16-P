import os
import shutil
import csv

#this script goes through the data students csv and filter out the images which are corrosponding to our group.
#and then it put in a subfolder and make a new csv .

data_dir = os.path.join("data")
csv_file = os.path.join( "data-student.csv")
output_csv = os.path.join("filtered_images.csv")
output_dir = os.path.join("filtered_images")


os.makedirs(output_dir, exist_ok=True)


filtered_images = []
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        filename, label = row
        if label == 'P':
            filtered_images.append(filename)
            shutil.copy(os.path.join(data_dir, filename), output_dir)


with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    for image in filtered_images:
        writer.writerow([image])

print(f"Filtered images have been copied to {output_dir} and listed in {output_csv}")