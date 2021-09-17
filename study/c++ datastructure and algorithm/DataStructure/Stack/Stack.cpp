#include "Stack.h"

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
Stack<T>::Stack(int stackCapacity) {
    capacity = stackCapacity;
    if (capacity < 1) { throw invalid_argument("stack capacity must be greater than 0"); }
    stack = new T[capacity];
    top -= 1;
}

template<class T>
bool Stack<T>::IsEmpty() const { return top == -1; }

template<class T>
inline T &Stack<T>::Top() const {
    if (IsEmpty()) throw invalid_argument("stack is empty");
    return stack[top];
}

template<class T>
void Stack<T>::Push(const T &item) {
    if (top == capacity - 1) {
        ChangeSize1D(stack, capacity, capacity * 2);
        capacity *= 2;
    }
    stack[++top] = item;
}

template<class T>
void Stack<T>::Pop() {
    if (IsEmpty())throw invalid_argument("stack is empty");
    stack[top--].~T();
}