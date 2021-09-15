#ifndef ALGORITHMSTUDYANDDATASTRUCTURE_BAG_H
#define ALGORITHMSTUDYANDDATASTRUCTURE_BAG_H


class Bag {
public:
    Bag(int bagCapacity=10);
    ~Bag();

    int Size() const;
    bool isEmpty() const;
    int Element() const;
    void Push(const int);
    void Pop();

private:
    int *array;
    int capacity;
    int top;

};


#endif //ALGORITHMSTUDYANDDATASTRUCTURE_BAG_H
