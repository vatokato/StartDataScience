standard_input = "43 40 32 40 30"

boxes = sorted([int(b) for b in input().split()], reverse=True)

parent_box = boxes[0]
boxes_count = 1
for b in boxes:
    if b + 3 <= parent_box:
        parent_box = b
        boxes_count += 1

print(boxes_count, parent_box)
