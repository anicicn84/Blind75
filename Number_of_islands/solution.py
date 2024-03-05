def countIslands(matrix):
    if not matrix: # matrix is empty
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Mark all of the fields as visited.
    # We can also mark the fields as visited by setting 1s to 0s to save space, too (an alternative, as explained in md file)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    totalIslands = 0
    
    def dfs(row, col):
        # row and col need to be within the bounds;
        # Matrix cell we are visiting must not be visited, otherwise it is taken into account;
        # Matrix cell should, also, not be 0, then we skip immediately.
        # With this all of the cases are covered: bounds, visited and 0 elements
        if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col] or matrix[row][col] == 0:
            return
        
        # Not to forget to set the visited cell as visited, otherwise we will have deep recursion
        # until the app breaks, since all of the neighboring nodes will again refer to this node, again and again.
        visited[row][col] = True
        
        # Recursion to take care of surrounding nodes and their surrounding nodes in the next level of recursion.
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
        
        
    for row in range(rows):
        for col in range(cols):
            # Found one that is not visited and 1 -> do dfs on it to mark all surrounding 1s as visited
            if matrix[row][col] == 1 and not visited[row][col]:
                dfs(row, col)
                totalIslands += 1
            
    return totalIslands


test_case1 = [[0, 1, 1, 1, 0],[0, 0, 0, 1, 1],[0, 1, 1, 1, 0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0]]
expected_output1 = 1

assert(countIslands(test_case1) == expected_output1)

test_case2 = [[1, 1, 1, 0, 0],[0, 1, 0, 0, 1],[0, 0, 1, 1, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0]]
expected_output2 = 3

assert(countIslands(test_case2) == expected_output2)