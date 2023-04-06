new_frames = audioop.lin2lin(frames, old_width, new_width)
if 1 == new_width:
   new_frames = audioop.bias(new_frames, 1, 128)