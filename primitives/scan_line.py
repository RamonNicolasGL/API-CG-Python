from primitives.setPixel import set_pixel

##
def intersecao(y, pi, pf):

  if pi[1] == pf[1]:
    return -1
    
  if pi[1] > pf[1]:
    aux = pi
    pi = pf
    pf = aux
    
  t = (y - pi[1])/(pf[1] - pi[1])
  
  if (t <= 0) or (t > 1) :
    return -1
    
  x = pi[0] + t*(pf[0] - pi[0])

  return (x,y)

##
def print_scan(screen, p_int, intensidade):
  
  p_int = sorted(p_int, key=lambda x: x[0])

  y = p_int[0][1]
  
  for i in range(0, len(p_int) - 1, 2):
        x1 = p_int[i][0]
        x2 = p_int[i + 1][0]  
        
        for x in range(round(x1), round(x2) + 1):  
            set_pixel(screen, round(x), y, intensidade)


##
def scanline(screen, pol, intensidade):

  #y min e max
  y_min = min(p[1] for p in pol)
  y_max = max(p[1] for p in pol)

  for y in range(y_min, y_max + 1):

    p_int = []

    pi = pol[0]

    for p in pol[1:]:
      pf = p
    
      intersec = intersecao(y, pi, pf)

      if intersec != -1:

        p_int.append(intersec)

      pi = pf
    #erro ta aqui####
    aux = pol[0]

    intersec = intersecao(y, pi, aux)
    if intersec != -1:

        p_int.append(intersec)

    if len(p_int) != 0:
      print_scan(screen, p_int, intensidade)
    ##################
 

'''function img = print_scan(im, p_int, intensidade)
  img = im;
  
  p_int = sort(p_int, 1);
  
  y = p_int(1, 2);
  
  for i = 1:2:rows(p_int)-1
   
    x1 = p_int(i, 1);
    x2 = p_int(i+1, 1);
    
    for x = x1:x2
      img = set_pixel(img, round(x), y, intensidade);
    endfor
    
  endfor
endfunction'''