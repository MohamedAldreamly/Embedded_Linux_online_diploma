
#include <iostream>
#include <utility> // For std::move
using namespace std;

class person
{
    char id;
    int age;
    int *ptr;

public:
    // Default Constructor: Initialize members
    person() : id('\0'), age(0), ptr(nullptr)
    {
        cout << "Default Constructor\n";
    }

    // Parameterized Constructor with Constructor Delegation
    person(char id, int age, int *ptr) : person()
    {
        this->id = id;
        this->age = age;
        this->ptr = ptr; // Take ownership of allocated memory
        cout << "Parameterized Constructor\n";
    }

    // Deep Copy Constructor: Allocate separate memory
    person(const person &obj)
    {
        this->id = obj.id;
        this->age = obj.age;
        this->ptr = obj.ptr ? new int(*obj.ptr) : nullptr;
        cout << "Copy Constructor\n";
    }

    // person(const person &obj) = delete; // Prevent copying if needed

    // Move Constructor: Transfer memory ownership
    person(person &&obj) noexcept
    {
        this->id = obj.id;
        this->age = obj.age;
        this->ptr = obj.ptr; // Steal the pointer
        obj.ptr = nullptr;   // Prevent double deletion
        cout << "Move Constructor\n";
    }

    // Destructor: Release allocated memory
    ~person()
    {
        cout << "Destructor\n";
        delete ptr; // Safe even if ptr is nullptr
    }

    // Return a copy of the current object
    person getPerson()
    {
        return *this; // Calls Copy Constructor
    }

    // Modify current object and return its reference
    person &increaseAge(int inc)
    {
        this->age += inc;
        return *this; // No copy, enables chaining
    }

    // Update member values
    void set(char id_var, int age_var, int *ptr_var)
    {
        id = id_var;
        age = age_var;

        // Copy the pointed-to value, not the pointer address
        if (ptr && ptr_var)
            *ptr = *ptr_var;
    }

    // Display object data
    void get()
    {
        cout << id << " " << age << endl;
    }
};

int main()
{
    // Parameterized + Delegated Default Constructor
    person i('A', 15, new int(5));

    // Deep Copy: i2 owns separate memory
    person i2(i);

    // getPerson() returns by value, so Copy occurs
    person obj3(i.getPerson());

    // Create another object with dynamic memory
    person i3('C', 20, new int(10));

    // Move: Transfer ownership from i3 to i4
    person i4(std::move(i3));

    // Method Chaining: Modify the same object
    i.increaseAge(5).increaseAge(5).increaseAge(5).get();

    // Destructors run in reverse construction order
    return 0;
}
