#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

int main(){
    int n, m;
    std::cin>>n>>m;
    std::map<int, std::vector<int>> graph;
    for (int i = 0; i < n; ++i) {
        graph.insert({i, std::vector<int>});
    }
    int start, end;
    for (int i = 0; i < m; ++i) {
        std::cin>>start>>end;
        graph[start].push_back(end);
    }
    
    return 0;
}