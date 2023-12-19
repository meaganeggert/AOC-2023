#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	ifstream puzzleData;
	puzzleData.open("puzzleData.txt");

	string temp;
	char tempChar;
	int firstChar = 0;
	int lastChar = 0;
	string numberString = "";
	int sum = 0;

	while (puzzleData) {
		getline(puzzleData, temp);
		istringstream tempStream(temp);
		while (tempStream) {
			tempStream >> tempChar;
			if (!tempStream) break;
			if (isdigit(tempChar)) {
				numberString += tempChar;
			}
		}
		if (!puzzleData) break;
		cout << temp << endl;
		cout << numberString << endl;
		if (numberString.length() == 1) {
			numberString += numberString;
		}
		else if (numberString.length() > 2) {
			firstChar = numberString.at(0) - 48;
			lastChar = stoi(numberString) % 10;
			numberString = to_string(firstChar) + to_string(lastChar);
		}
		
		cout << numberString << endl;
		sum += stoi(numberString);
		numberString = "";
	}

	cout << sum << endl;

	puzzleData.close();
}