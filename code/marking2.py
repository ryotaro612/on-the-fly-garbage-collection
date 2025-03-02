i, k = 0, M # Mはノード数
while k > 0:
  c = nodes[i].color // atomic
  if c == GRAY:
    k = M
    for side in range(2):
      succ := nodes[i].successors[side] // atomic
      // begin atomic
      if succ.color == WHITE:
        succ.color = GRAY
      // end atomic
      nodes[i].color = BLACK // atomic
  else:
    k -= 1
  i = (i + 1) % M
