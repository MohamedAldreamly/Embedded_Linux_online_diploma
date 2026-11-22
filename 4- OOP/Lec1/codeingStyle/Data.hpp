#pragma once

class Data
{
private:
    int num1;
    int num2;

public:
    Data();
    Data(int a, int b);

    void print() const;
    void setNum1(int value);
};