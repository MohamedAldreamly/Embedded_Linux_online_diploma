#include <iostream>
using namespace std;

class Student
{
private:
    Student()
    {
        cout << "Private Constructor Called\n";
    }

public:
    static Student createObject()
    {
        return Student();
    }

    void print()
    {
        cout << "Hello Student\n";
    }
};

int main()
{

    Student s1 = Student::createObject();

    s1.print();

    return 0;
}