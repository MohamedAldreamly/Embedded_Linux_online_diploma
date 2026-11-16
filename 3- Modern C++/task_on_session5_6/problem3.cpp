
#include <iostream>
#include <stack>
#include <string>

int main()
{
    bool state = true;

    std::stack<char> st;
    std::string name;

    std::cout << "Input: ";
    std::cin >> name;

    for (char letter : name)
    {
        if ((letter == '(') || (letter == '{') || (letter == '['))
        {
            st.push(letter);
        }
        else if ((letter == ')') || (letter == '}') || (letter == ']'))
        {
            if (st.empty())
            {
                state = false;
                break;
            }

            if ((letter == ')' && st.top() == '(') ||
                (letter == '}' && st.top() == '{') ||
                (letter == ']' && st.top() == '['))
            {
                st.pop();
            }
            else
            {
                state = false;
                break;
            }
        }
    }

    if (!st.empty())
    {
        state = false;
    }

    std::cout << "Output: " << state << std::endl;

    return 0;
}
