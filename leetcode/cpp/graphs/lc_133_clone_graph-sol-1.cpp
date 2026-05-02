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
    Node* cloneGraph(Node* node) {
        // first check if we are given an empty graph
        if (node == nullptr) {
            // if we are then return null
            return nullptr;
        }

        // init our oldToNew hashmap
        // key = old node pointer, value = new node pointer that we create
        std::unordered_map<Node*, Node*> oldToNew;
        // setup our visited set to keep track of the nodes
        // we have already deep cloned or are in the bfs queue
        // to be deep cloned later on.
        std::unordered_set<Node*> visited;

        // init our standard bfs queue
        std::queue<Node*> bfsQueue;
        // add the first node to the bfs queue
        bfsQueue.push(node);
        // mark the first node as visited
        visited.insert(node);

        // standard bfs loop until the queue is empty
        while (!bfsQueue.empty()) {
            // get the pointer to the old node at the front of the queue
            Node* oldNode = bfsQueue.front();
            // remove the old node pointer at the front of the queue
            bfsQueue.pop();

            // if we have not already created a new node for this old node
            // then create the new node and assign it to the oldToNew hashmap
            if (!oldToNew.contains(oldNode)) {
                Node* newNode = new Node(oldNode->val);
                oldToNew[oldNode] = newNode;
            }

            // loop through all the old neighbours of the old node
            for (Node* oldNeighbour: oldNode->neighbors) {
                // if we have not already created a new node for this old neighbour
                // then create the new node and assign it to the oldToNew hashmap
                if (!oldToNew.contains(oldNeighbour)) {
                    Node* newNeighbour = new Node(oldNeighbour->val);
                    oldToNew[oldNeighbour] = newNeighbour;
                }

                // add the new neighbour to the neighbours vector of the new parent node
                oldToNew[oldNode]->neighbors.push_back(oldToNew[oldNeighbour]);

                // if we have not visited the old neighbour before (deep cloned it)
                // then add it to bfs queue and mark it as visited.
                if (!visited.contains(oldNeighbour)) {
                    bfsQueue.push(oldNeighbour);
                    visited.insert(oldNeighbour);
                }
            }
        }

        // finally return the new node we initially created
        // and stored in the oldToNew hashmap
        return oldToNew[node];
    }
};
