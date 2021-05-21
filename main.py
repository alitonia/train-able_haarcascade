def next_step(step: str, l: list):
    i = l.index(step)
    return l[(i + 1) % len(l)]


positive_data = []
negative_data = []

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
            o['name'] = name
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

print(len(positive_data))
print(len(negative_data))

with open('wider_face_split/positive.info', 'w') as f:
    for o in positive_data:
        f.write(o['name'] + ' ' + str(o['items']) + ' ' + ' '.join(o['box']) + '\n')

with open('wider_face_split/negative.info', 'w') as f:
    for o in negative_data:
        f.write(o['name'] + '\n')
