#include <iostream>
using namespace std;

int main() {
  int a = 0, b = 0, c = 0;
  cout << "Enter 1st number: ";
  cin >> a;
  if (cin.fail()) {
    cout << "Only interger type inputs allowed";
    return 1;
  }
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  cout << "Enter 2nd number: ";
  cin >> b;
  if (cin.fail()) {
    cout << "Only interger type inputs allowed";
    return 1;
  }
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  cout << "Enter 3rd number: ";
  cin >> c;
  if (cin.fail()) {
    cout << "Only interger type inputs allowed";
    return 1;
  }
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  // cout << a << " " << b << " " << c << endl;
  if (a <= 0 || b <= 0 || c <= 0) {
    cout << "Invlaid input";
  } else if ((long)a + b <= c || (long)b + c <= a || (long)c + a <= b) {
    cout << "Not a triangle";
  } else if (a == b && b == c) {
    cout << "Equilateral triangle";
  } else if ((a == b && a != c && b != c) || (b == c && b != a && c != a) ||
             (c == a && c != b && a != b)) {
    cout << "Isoselece triangle";
  } else if (a != b && b != c && c != a) {
    cout << "Scalene triangle";
  }
  cout << endl;
  return 0;
}
