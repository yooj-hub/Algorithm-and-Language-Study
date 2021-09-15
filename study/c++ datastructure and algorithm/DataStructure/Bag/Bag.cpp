#include "Bag.h"

using namespace std;

template<class T>
void ChangeSize1D(T *&a, const int oldSize, const int newSize) {
    if (newSize < 0)throw "New length must be >= 0";

    T *temp = new T[newSize];
    int number = min(oldSize, newSize);
    copy(a, a + number, temp);
    delete[] a;
    a = temp;
}

Bag::Bag(int bagCapacity) : capacity(bagCapacity) {
    if (capacity < 1) throw "Capacity must be >0";
    array = new int[capacity];
    top = -1;
}

Bag::~Bag() { delete[] array; }

inline int Bag::Size() const { return top + 1; }

inline bool Bag::isEmpty() const { return Size() == 0; }

inline int Bag::Element() const {
    if (isEmpty()) throw "Bag is Empty";
    return array[0];
}

void Bag::Push(const int x) {
    if (capacity == top + 1) ChangeSize1D(array, capacity, capacity * 2);
    capacity *= 2;
    array[++top] = x;

}

void Bag::Pop() {
    if (isEmpty()) throw "Bag is empty. cannot delete";
    int deletePos = top / 2;
    copy(array + deletePos + 1, array + top + 1, array + deletePos);
    top--;
}


