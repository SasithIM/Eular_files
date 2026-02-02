#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

int unsorted[] = {3, 5, 1,9,6,7,4,8,2,4};

class minHeap {
private:
    vector<int> heap;
    
    int parent(int i) { return (i-1)/2;}
    int left(int i) { return 2*i + 1;}
    int right(int i) { return 2*i + 2;}

    void heapifyUp(int i){
        while (i>0 && heap[i] < heap[parent(i)]){
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

    void heapifyDown(int i){
        int smallest = i;
        int l = left(i);
        int r = right(i);

        if (l<heap.size() && heap[l]<heap[smallest]){
            smallest = l;
        }
        if (r<heap.size() && heap[r]<heap[smallest]){
            smallest = r;
        }
        if (smallest != i){
            swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    void insert(int val){
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }

    void pop(){
        if (heap.empty()){ return; }
        
        heap[0] = heap.back();
        heap.pop_back();

        if (!heap.empty()){ heapifyDown(0); }
    }

    int top(){
        if (heap.empty()){ throw runtime_error("Heap is empty");}
        return heap[0];
    }

    void printHeap() {
        for (int val : heap) cout << val << " ";
        cout << endl;
    }
};

int main(){
    minHeap heap;
    for (int val : unsorted){
        heap.insert(val);
        cout << val << " ";
    }
    cout << endl;

    heap.printHeap();

    int len = sizeof(unsorted)/sizeof(unsorted[0]);

    int sorted[len];
    for (int i = 0; i < len; i++) {
        sorted[i] = heap.top();
        heap.pop();
    }

    for( int val : sorted){
        cout << val << " ";
    }
    cout << endl;
}
