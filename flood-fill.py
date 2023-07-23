class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        visited = [[0 for x in range(len(image[0]))] for i in range(len(image))]
        
        queue = []
        queue.append([sr,sc])
        while len(queue) > 0:
            index = queue.pop()
            print(index)
            if visited[index[0]][index[1]] == 0:
                visited[index[0]][index[1]] = 1
              
                image[index[0]][index[1]] = color
                if index[0]+1 < len(visited):
                    if visited[index[0]+1][index[1]] == 0 and image[index[0]+1][index[1]] == original:
                        queue.append([index[0]+1,index[1]])
                if index[0]-1 > -1:
                    if visited[index[0]-1][index[1]] == 0 and image[index[0]-1][index[1]] == original:
                        queue.append([index[0]-1,index[1]])
                if index[1]+1 < len(visited[0]):
                    if visited[index[0]][index[1]+1] == 0 and image[index[0]][index[1]+1] == original:
                        queue.append([index[0],index[1]+1])
                if index[1]-1 > -1:
                    if visited[index[0]][index[1]-1] == 0 and image[index[0]][index[1]-1] == original:
                        queue.append([index[0],index[1]-1])
        return image
                    





