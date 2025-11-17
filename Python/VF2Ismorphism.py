import java.util.*;

public class VF2GraphIsomorphism {
    final private int[][] graph1;
    final private int[][] graph2;
    public VF2GraphIsomorphism(int[][] graph1, int[][] graph2) {
        //initiate each graph with the graph
        this.graph1 = graph1;
        this.graph2 = graph2;

    }

    public boolean areIsomorphic() {
        int length1 = graph1.length;
        int length2 = graph2.length;
        //checks if they have the same lengths if not will return false
        if (length1 != length2) {
            //System.out.println("Graph lengths have two different sizes.");
            return false;
        }

        // Check degree sequences to see if it matches and if not it will return false
        if (!checkDegreeSequence()) {
            //System.out.println("The degree sequences of the graphs aren't the same.");
            return false;
        }

        //intialize backtracking
        boolean[] visited1 = new boolean[length1];
        boolean[] visited2 = new boolean[length2];
        int[] permutation = new int[length1];
        //filling the permutation array with -1 to show what spaces are being used
        Arrays.fill(permutation, -1);

        //recusion call
        return vf2Match(visited1, visited2, permutation);
    }

    //base case recursion
    private boolean vf2Match(boolean[] visited1, boolean[] visited2, int[] permutation) {
        return vf2Match(0, visited1, visited2, permutation);
    }

    //full recursion depth first search
    private boolean vf2Match(int depth, boolean[] visited1, boolean[] visited2, int[] permutation) {
        int length = graph1.length;

        // If all vertices are matched, see if it is valid and return true if it is
        if (depth == length) {
            //System.out.println("Found a valid permutations: " + Arrays.toString(permutation));
            return true;
        }

        for (int i = 0; i < length; i++) {
            if (!visited1[i]) {
                for (int j = 0; j < length; j++) {
                    if (!visited2[j] && isPossible(i, j, permutation)) {
                        // adds to visited and permutation before doing the vf2Match recursion
                        visited1[i] = true;
                        visited2[j] = true;
                        permutation[i] = j;

                        // Recursively match the next vertex
                        if (vf2Match(depth + 1, visited1, visited2, permutation)) {
                            return true;
                        }
                        //if the vf2Match doesn't return true it will access these lines
                        // and backtrack because it is not possible with this current vertex
                        visited1[i] = false;
                        visited2[j] = false;
                        permutation[i] = -1;
                    }
                }

                // If no valid permutation for this vertex backtrack
                return false;
            }
        }
        return false;
    }
    //checks if the permutation is possible to do to become isomorphic
    private boolean isPossible(int i, int j, int[] permutation) {
        //for debugging
        //System.out.println("Testing permutation: "  + Arrays.toString(permutation));
        // Check degree to see if it is possible for this to become a permutation
        if (getDegree(graph1, i) != getDegree(graph2, j)) {
            return false;
        }

        // Check adjacency preservation for already matched vertices
        for (int k = 0; k < graph1.length; k++) {
            if (permutation[k] != -1) {
                // Compare adjacency relationships
                if (graph1[i][k] != graph2[j][permutation[k]]) {
                    return false;
                }
                //makes sure the adjacency matrix is adjacent and if not checks directed graphs
                if(graph1[k][i] != graph2[permutation[k]][j]) {
                    return false;
                }
            }
        }

        return true;
    }
    //get the specific degree of the vertex
    private int getDegree(int[][] graph, int vertex) {
        int degree = 0;
        for (int edge : graph[vertex]) {
            degree += edge;
        }
        return degree;
    }
    //this function sorts the degrees in highest to lowest order so we can compare
    // the degrees of both graphs and return true if they match to keep the program going
    private boolean checkDegreeSequence() {
        int[] degrees1 = getDegrees(graph1);
        int[] degrees2 = getDegrees(graph2);
        Arrays.sort(degrees1);
        Arrays.sort(degrees2);
        return Arrays.equals(degrees1, degrees2);
    }
    //this function is for the checkDegreeSequence() to get all the degrees in each graph
    private int[] getDegrees(int[][] graph) {
        int[] degrees = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                if (graph[i][j] == 1) {
                    degrees[i]++;
                }
            }
        }
        return degrees;
    }
}

