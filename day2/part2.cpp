#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <unordered_map>
using namespace std;

int main() {
	ifstream puzzleData;
	puzzleData.open("puzzleData.txt");

	string thisLine;
	int sum = 0;
	int gameID = -37;
	int lastAdded = 9999;
	int maxBlue = 14;
	int maxRed = 12;
	int maxGreen = 13;
	bool gameLegit = true;
	int numRed = 0;
	int numBlue = 0;
	int numGreen = 0;
	int minRed = -99;
	int minBlue = -88;
	int minGreen = -77;
	int power = 0;
	int powerSum = 0;

	unordered_map<string, int> colorMap = { {"red", 0}, {"blue", 0}, {"green", 0} };



	while (puzzleData) {
		getline(puzzleData, thisLine);
		if (!puzzleData) break;
		istringstream thisLine_stream(thisLine);
		string temp = "";
		thisLine_stream >> temp; // read in "Game"
		//cout << temp << endl;
		thisLine_stream >> temp; // read in ID #
		temp.erase(temp.length() - 1, 1);
		gameID = stoi(temp);

		//cout << gameID << endl;

		int tempNum = -99;
		while (thisLine_stream) {
			string tempKey = "";
			thisLine_stream >> temp;
			if (!thisLine_stream) break;
			if (all_of(temp.begin(), temp.end(), ::isdigit)) {
				tempNum = stoi(temp);
				cout << tempNum << " ";
			}
			else {
				if (temp.at(temp.length() - 1) == ',') {
					tempKey = temp.erase(temp.length() - 1, 1);
					cout << tempKey << endl;
					// Assign number values to their respective colors
					if (tempKey == "red") {
						numRed = tempNum;
						if (numRed > minRed) {
							minRed = numRed;
						}
					}
					else if (tempKey == "green") {
						numGreen = tempNum;
						if (numGreen > minGreen) {
							minGreen = numGreen;
						}
					}
					else if (tempKey == "blue") {
						numBlue = tempNum;
						if (numBlue > minBlue) {
							minBlue = numBlue;
						}
					}

				}
				else if (temp.at(temp.length() - 1) == ';') {
					tempKey = temp.erase(temp.length() - 1, 1);
					cout << tempKey << endl;
					// Assign number values to their respective colors
					if (tempKey == "red") {
						numRed = tempNum;
						if (numRed > minRed) {
							minRed = numRed;
						}
					}
					else if (tempKey == "green") {
						numGreen = tempNum;
						if (numGreen > minGreen) {
							minGreen = numGreen;
						}
					}
					else if (tempKey == "blue") {
						numBlue = tempNum;
						if (numBlue > minBlue) {
							minBlue = numBlue;
						}
					}
					// Check if the shown amounts for red/green/blue are possible
					if (numRed > maxRed) {
						gameLegit = false;
					}
					if (numBlue > maxBlue) {
						gameLegit = false;
					}
					if (numGreen > maxGreen) {
						gameLegit = false;
					}
					//cout << gameLegit;
					cout << endl;
				}
				else {
					tempKey = temp;
					cout << tempKey << endl;
					cout << "---------";
					// Assign number values to their respective colors
					if (tempKey == "red") {
						numRed = tempNum;
						if (numRed > minRed) {
							minRed = numRed;
						}
					}
					else if (tempKey == "green") {
						numGreen = tempNum;
						if (numGreen > minGreen) {
							minGreen = numGreen;
						}
					}
					else if (tempKey == "blue") {
						numBlue = tempNum;
						if (numBlue > minBlue) {
							minBlue = numBlue;
						}
					}
					// Check if the shown amounts for red/green/blue are possible
					if (numRed > maxRed) {
						gameLegit = false;
					}
					if (numBlue > maxBlue) {
						gameLegit = false;
					}
					if (numGreen > maxGreen) {
						gameLegit = false;
					}
					//cout << gameLegit;
					cout << endl;
					if (gameLegit and gameID != lastAdded) {
						sum += gameID;
						lastAdded = gameID;
						cout << "Added: " << gameID << endl << endl;
					}
					power = minRed * minBlue * minGreen;
					powerSum += power;

					cout << "Min Red: " << minRed << endl;
					cout << "Min Green: " << minGreen << endl;
					cout << "Min Blue: " << minBlue << endl;
					cout << "Power: " << power << endl;
					
					numRed = 0;
					numBlue = 0;
					numGreen = 0;
					gameLegit = true;
					minRed = minBlue = minGreen = 0;
				}				
				
			}
			

		}
	}

	cout << "Power Sum: " << powerSum << endl;
	cout << "Sum of GameID's: " << sum << endl;


	puzzleData.close();
}