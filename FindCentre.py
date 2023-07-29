# Note to self: lower left corner of image is origin

def _validator(screen, m, n, x, y, prevC, newC):
    return not (x < 0 or x>= m or y < 0 or y>= n
                or screen[x][y] != prevC or screen[x][y] == newC)

# Inspired by the flood fill algorithm
def findCentre(screen, image, x, y, m=300, n=300, prevC=1, newC=2, validator=_validator):
    queue = []
    max_brightness = 0
    centre = []
     
    # Append the position of starting
    # pixel of the component
    queue.append([x, y])

    if image[x][y] > max_brightness:
        max_brightness = image[x][y]
        centre = [x, y]

    # Color the pixel with the new color
    screen[x][y] = newC
 
    # While the queue is not empty i.e. the
    # whole component having prevC color
    # is not colored with newC color
    while queue:
         
        # Dequeue the front node
        currPixel = queue.pop()
         
        posX = currPixel[0]
        posY = currPixel[1]
         
        # Check if the adjacent
        # pixels are valid
        if validator(screen, m, n, 
                posX + 1, posY, 
                        prevC, newC):
            
            if image[posX+1][posY] > max_brightness:
                max_brightness = image[posX+1][posY]
                centre = [posX + 1, posY]
            
            # Color with newC
            # if valid and enqueue
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])
         
        if validator(screen, m, n, 
                    posX-1, posY, 
                        prevC, newC):
            
            if image[posX-1][posY] > max_brightness:
                max_brightness = image[posX-1][posY]
                centre = [posX - 1, posY]
            
            screen[posX-1][posY]= newC
            queue.append([posX-1, posY])
         
        if validator(screen, m, n, 
                posX, posY + 1, 
                        prevC, newC):
            
            if image[posX][posY+1] > max_brightness:
                max_brightness = image[posX][posY+1]
                centre = [posX, posY + 1]
            
            screen[posX][posY+1]= newC
            queue.append([posX, posY + 1])
         
        if validator(screen, m, n, 
                    posX, posY-1, 
                        prevC, newC):
            
            if image[posX][posY-1] > max_brightness:
                max_brightness = image[posX][posY-1]
                centre = [posX, posY - 1]
            
            screen[posX][posY-1]= newC
            queue.append([posX, posY-1])
    
    centre.reverse()
    return centre
    