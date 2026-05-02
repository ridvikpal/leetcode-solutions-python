#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

/**
 * https://leetcode.com/problems/clone-graph/description/
 *
 * Time complexity: O(n) where n = number of nodes in graph
 * Space complexity: O(n) where n = number of nodes in graph
 */
// Definition for a Node.
class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = std::vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = std::vector<Node*>();
    }
    Node(int _val, std::vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    // create a helper recursive dfs clone function
    Node* dfsClone(Node* oldNode, std::unordered_map<Node*, Node*>& oldToNew) {
        // our base case for recursion is if we have already
        // deep cloned this old node, which is if the hashmap contains
        // the old node already
        if (oldToNew.contains(oldNode)) {
            // in that case, just return the deep cloned new node directly
            return oldToNew[oldNode];
        }

        // otherwise we have not deep cloned this node before
        // so create a new node and add it to the old to new hashmap
        Node* newNode = new Node(oldNode->val);
        oldToNew[oldNode] = newNode;

        // loop through all the old neighbours of the old node
        for (Node* oldNeighbour: oldNode->neighbors) {
            // run dfs clone on the neighbours to get the new neighbour node pointer
            Node* newNeighbour = dfsClone(oldNeighbour, oldToNew);
            // assign the new neighbour node pointer to the neighbours vector of the new parent node
            oldToNew[oldNode]->neighbors.push_back(newNeighbour);
        }

        // finally return the new node we created via the hashmap
        return oldToNew[oldNode];
    }

    Node* cloneGraph(Node* node) {
        // first check if we have a null pointer exception
        if (node == nullptr) {
            return nullptr;
        }

        // create our oldToNew hashmap
        // key = old node pointer, value = new node pointer
        std::unordered_map<Node*, Node*> oldToNew;

        // run dfs clone with the parent node and return
        // the new deep cloned parent node
        return dfsClone(node, oldToNew);
    }
};
