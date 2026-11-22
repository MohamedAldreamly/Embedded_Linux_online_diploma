#include <iostream>
using namespace std;

// inline (C++17): Allows defining and initializing a static member
// inside the class without a separate definition outside.
// It does not affect the ability to modify its value.

class Counter
{
public:
    int count = 0;

private:
    static Counter *instance; // declare a static pointer to hold the single instance of the class
    // OR
    // inline static Counter* instance = nullptr;
    Counter()
    {
        cout << "Constructor Called\n";
    }

public:
    static Counter *get_instance()
    {
        if (instance == nullptr)
        {
            instance = new Counter();
        }
        return instance;
    }
};

// Define and initialize the static member
Counter *Counter::instance = nullptr;

class CounterStack
{
public:
    int count = 0;

private:
    // Prevent direct object creation
    CounterStack()
    {
        cout << "CounterStack Constructor\n";
    }

public:
    // Return reference to the same instance
    static CounterStack &get_instance()
    {
        // Created only once on the first call
        static CounterStack instance;

        return instance; // Return reference, not copy
    }
};

int main()
{
    Counter *c1 = Counter::get_instance();
    Counter *c2 = Counter::get_instance();

    c1->count = 10;

    cout << c2->count << endl;
    cout << (c1 == c2) << endl;

    return 0;
}