#include <iostream>
using namespace std;

#define PI 3.14159

double calculateArea(double radius)
{
    return PI * radius * radius;
}
double calculatePerimeter(double radius)
{
    return 2 * PI * radius;
}

int main()
{
    double radius;

    cout << "Enter the radius of the circle: ";

    cin >> radius;
    double area = calculateArea(radius);
    double perimeter = calculatePerimeter(radius);
    cout << "The area of the circle is: " << area << endl;
    cout << "The perimeter of the circle is: " << perimeter << endl;
    return 0;
}