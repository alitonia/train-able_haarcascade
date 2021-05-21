from os import walk


def next_step(step: str, l: list):
    i = l.index(step)
    return l[(i + 1) % len(l)]


relative_path_to_wider_images_from_root = 'WIDER_train/images/'
positive_data = []
negative_data = []

# wider face images
with open('wider_face_split/wider_face_train_bbx_gt.txt', 'r') as f:
    name = ''
    items = 0
    item_count = 0
    bounding_data = []
    steps = ['name', 'count', 'box']
    step = steps[0]
    skip_box = False
    o = dict()

    for (i, line) in enumerate(f):
        if item_count == items and step == steps[-1]:
            items = 0
            item_count = 0
            name = ''
            o['box'] = bounding_data
            if o['items'] == 0:
                negative_data.append(o)
            else:
                positive_data.append(o)
            o = dict()
            bounding_data = []
            step = next_step(step, steps)
            # done
            # break

        if step == steps[0]:
            name = line[:-1]
            step = next_step(step, steps)
            o['name'] = relative_path_to_wider_images_from_root + name
        elif step == steps[1]:
            items = int(line)
            o['items'] = items
            if items == 0:
                items = 1
            step = next_step(step, steps)

        else:
            x, y, w, h, *_ = line.split(' ')
            bounding_data.extend([x, y, w, h])
            item_count += 1

# non-face images
for (dirpath, dirnames, filenames) in walk('archive/natural_images'):
    if len(dirnames) == 0 and dirpath.find('person') == -1:
        negative_data.extend([{'name': dirpath + f_name} for f_name in filenames])

print(f"Positive: {len(positive_data)}")
print(f"Negative: {len(negative_data)}")

with open('generated/positive.dat', 'w') as f:
    for o in positive_data:
        f.write(o['name'] + ' ' + str(o['items']) + ' ' + ' '.join(o['box']) + '\n')

with open('generated/negative.dat', 'w') as f:
    for o in negative_data:
        f.write(o['name'] + '\n')

with open('log/run_main.log', 'w') as f:
    f.write(f"Positive: {len(positive_data)}\n")
    f.write(f"Negative: {len(negative_data)}\n")
