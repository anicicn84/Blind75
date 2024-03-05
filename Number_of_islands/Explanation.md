## Explanation of the approach

To count the number of islands in a 2D array (a matrix) containing only 1s (land) and 0s (water), we can use a Depth-First Search (DFS) algorithm. The idea is to iterate over each cell in the matrix, and every time we find a cell with a `1` (land) that has not been visited, we start a DFS from that cell. During the DFS, we mark all reachable cells (horizontally or vertically) that form the connected component (island) as visited. This way, we ensure each island is only counted once.
_**An alternative**_ (to save memory) is to mark the visited cells as water and in that case we do not need an extra array to store
booleans for each visited cell. 


### A step-by-step algorithm:

1. **Initialize:** Create a `visited` matrix of the same dimensions as the input matrix to keep track of visited cells.
2. **Iterate:** Go through each cell in the matrix. If the cell value is `1` (land) and it has not been visited, it is part of a new island.
3. **DFS:** From this cell, perform a _Depth-First Search_ to visit all connected lands (`1s`), marking them as visited in the visited matrix.
4. For each land cell found, check its four neighbors (up, down, left, right) for other land cells that are not visited.
Recursively apply DFS to those neighbors.
5. **Count:** Each time DFS is initiated, increment the island count.
6. **Result:** After completing the iteration over all cells, the island count will represent the number of islands in the matrix. 