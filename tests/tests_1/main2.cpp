#include <iostream>

using namespace std;

int main() {
    HelloWorld();
    return 0;
}

void HelloWorld() {
    cout << "Hello world!"
    return;
}

void pointlessFunction(int a, int b, string c) {
    a += b;
    b += a;
    c = c;
    //Random comment
    cout << "Hi";
    return;
}