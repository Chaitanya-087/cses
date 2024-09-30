for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    def orientation(x1, y1, x2, y2, x3, y3):
        val = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        if val == 0: return 0
        return 1 if val > 0 else -1
        
    def onSegment(x1, y1, x2, y2, x3, y3):
        return min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2)
    
    def doIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
        o1 = orientation(x1, y1, x2, y2, x3, y3)
        o2 = orientation(x1, y1, x2, y2, x4, y4)
        o3 = orientation(x3, y3, x4, y4, x1, y1)
        o4 = orientation(x3, y3, x4, y4, x2, y2)
        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and onSegment(x1, y1, x2, y2, x3, y3): return True
        if o2 == 0 and onSegment(x1, y1, x2, y2, x4, y4): return True   
        if o3 == 0 and onSegment(x3, y3, x4, y4, x1, y1): return True
        if o4 == 0 and onSegment(x3, y3, x4, y4, x2, y2): return True
        return False

    if doIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
        print("YES")
    else:
        print("NO")
