l = [(lambda lbl:(item + lbl for item in t))(label) for t, label in zip(tees,"ab")]