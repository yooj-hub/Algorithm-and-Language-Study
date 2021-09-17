
#include "Queue.h"

using namespace std;

template<class T>
void ChangeSize1D(T *&a, const int oldSize, const int newSize) {
    if (newSize < 0)throw;

    T *temp = new T[newSize];
    int number = min(oldSize, newSize);
    copy(a, a + number, temp);
    delete[] a;
    a = temp;
}

template<class T>
Queue<T>::Queue(int queueCapacity) {
    capacity = queueCapacity;
    if (capacity < 1) throw invalid_argument("queue's capacity must be greater than 0");
    queue = new T[capacity];
    front = 0;
    rear = 0;
}

template<class T>
bool Queue<T>::IsEmpty() const {
    return front >= rear;
}

template<class T>
T &Queue<T>::Front() const {
    if(IsEmpty()) throw invalid_argument("queue is empty");
    return queue[front];
}

template<class T>
void Queue<T>::Pop() {
    if (IsEmpty()) throw invalid_argument("queue is empty");
    front++;
}

template<class T>
void Queue<T>::Push(const T &item) {
    if (rear == capacity) {
        ChangeSize1D(queue, capacity, capacity * 2);
    }
    queue[rear++] = item;
}

template<class T>
T &Queue<T>::Rear() const {
    return queue[rear - 1];
}




