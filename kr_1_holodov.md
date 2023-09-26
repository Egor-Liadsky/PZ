**Вариант 4**

#Задание 1

#include <iostream>

using namespace std;

int main()
{
    int number;
    cout << "Введите трехзначное число: ";
    cin >> number;

    int digit1 = number / 100;          
    int digit2 = (number / 10) % 10;    
    int digit3 = number % 10;           

    int sum = digit1 + digit2 + digit3; 

    cout << "Сумма цифр: " << sum << endl;

    return 0;
}
