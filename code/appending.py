for i in range(m):
  color := nodes[i].color // atomic
  if color == WHITE:
    free_list.append(nodes[i]) // atomic
  else: // color == BLACK
    nodes[i].color = WHITE // atomic
