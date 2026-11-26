/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    Node* dfs(Node* node, std::unordered_map<Node*, Node*>& clonemap){
        if (clonemap.contains(node)){
            //if in clonemap, return the clone
            return clonemap[node];
        }

        //if not in map, create a clone, with its value being the node val
        Node* clone = new Node(node->val);
        clonemap[node] = clone; //map it to the node
        for (Node* nei : node->neighbors){
            //for each neighbour, the clones neighbours should push to the neighbour
            clone->neighbors.push_back(dfs(nei, clonemap));
        }

        return clone;
    }
public:
    Node* cloneGraph(Node* node) {
        std::unordered_map<Node*, Node*> clonemap;

        if (node != nullptr){
            //if weve got a real node, run dfs on the node and map
            return dfs(node, clonemap);
        }

        return nullptr;
    }
 };
