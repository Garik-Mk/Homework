#include <iostream>
#include <bits/stdc++.h>
#include <vector>

int main(){
    int N;
    int inp;
    std::cin >> N;
    std::vector<int> vec;

    for(int i = 0; i < N; ++i){
        std::cin >> inp;
        vec.push_back(inp);
    } 

    sort(vec.begin(), vec.end());

    for(int i = 0; i < N; ++i){
        std::cout << vec[i] << " ";
    }
}