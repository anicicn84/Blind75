#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct Compare {
    bool operator()(const pair<int, pair<int, int>>& a, const pair<int, pair<int, int>>& b) {
        return a.first > b.first;
    }
};

vector<int> mergeKLists(vector<vector<int>>& lists) {
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, Compare> pq;
    vector<int> result;

    // Initialize the priority queue
    for (int i = 0; i < lists.size(); ++i) {
        if (!lists[i].empty()) {
            pq.push({lists[i][0], {i, 0}});
        }
    }

    while (!pq.empty()) {
        auto [val, indices] = pq.top();
        pq.pop();
        int listIdx = indices.first, elemIdx = indices.second;
        result.push_back(val);

        if (elemIdx + 1 < lists[listIdx].size()) {
            pq.push({lists[listIdx][elemIdx + 1], {listIdx, elemIdx + 1}});
        }
    }

    return result;
}

int main() {
    vector<vector<int>> lists = {{2, 6, 8}, {3, 6, 7}, {1, 3, 4}};
    vector<int> result = mergeKLists(lists);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
