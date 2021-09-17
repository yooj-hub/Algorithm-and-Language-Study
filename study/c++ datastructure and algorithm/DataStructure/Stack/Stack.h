/**
 * Stack
 * Date: 2021 09 14
 * Programmer: yooj
 * Using: Clion & c++17
 */
#ifndef ALGORITHMSTUDYANDDATASTRUCTURE_STACK_H
#define ALGORITHMSTUDYANDDATASTRUCTURE_STACK_H

template <class T>
class Stack {
public:
    Stack(int stackCapacity=10);

    bool IsEmpty() const;

    T& Top() const;

    void Push(const T& item);

    void Pop();

private:
    T *stack;
    int top;
    int capacity;

};


#endif //ALGORITHMSTUDYANDDATASTRUCTURE_STACK_H
