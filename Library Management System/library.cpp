#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class LibraryManagementSystem {
    string id, name, author, search;
    fstream file;

public:
    void addBook();
    void showAll();
    void extractBook();
};

void LibraryManagementSystem::addBook() {
    cout << "\nEnter Book ID :: ";
    getline(cin, id);
    cout << "Enter Book Name :: ";
    getline(cin, name);
    cout << "Enter Book's Author name :: ";
    getline(cin, author);

    file.open("bookData.txt", ios::out | ios::app);
    if (file.is_open()) {
        file << id << '*' << name << '*' << author << endl;
        file.close();
        cout << "Book Added Successfully...!" << endl;
    } else {
        cout << "Error opening file for writing." << endl;
    }
}

void LibraryManagementSystem::showAll() {
    file.open("bookData.txt", ios::in);
    if (file.is_open()) {
        cout << "\n\n";
        cout << "\t\t Book Id \t\t\t Book Name \t\t\t Author's Name" << endl;
        while (getline(file, id, '*') && getline(file, name, '*') && getline(file, author, '\n')) {
            cout << "\t\t " << id << " \t\t\t\t " << name << " \t\t\t " << author << endl;
        }
        file.close();
    } else {
        cout << "Error opening file for reading." << endl;
    }
}

void LibraryManagementSystem::extractBook() {
    showAll();
    cout << "Enter Book Id :: ";
    getline(cin, search);

    file.open("bookData.txt", ios::in);
    if (file.is_open()) {
        cout << "\n\n";
        cout << "\t\t Book Id \t\t\t Book Name \t\t\t Author's Name" << endl;
        while (getline(file, id, '*') && getline(file, name, '*') && getline(file, author, '\n')) {
            if (search == id) {
                cout << "\t\t " << id << " \t\t\t " << name << " \t\t\t " << author << endl;
                cout << "Book Extracted Successfully...!" << endl;
                return;
            }
        }
        cout << "Book not found." << endl;
        file.close();
    } else {
        cout << "Error opening file for reading." << endl;
    }
}

int main() {
    LibraryManagementSystem obj;
    char choice;

    do {
        cout << "----------------------------------" << endl;
        cout << "1-Show All Books" << endl;
        cout << "2-Extract Book" << endl;
        cout << "3-Add books(ADMIN)" << endl;
        cout << "4-Exit" << endl;
        cout << "----------------------------------" << endl;
        cout << "Enter Your Choice :: ";
        cin >> choice;

        switch (choice) {
            case '1':
                cin.ignore();
                obj.showAll();
                break;
            case '2':
                cin.ignore();
                obj.extractBook();
                break;
            case '3':
                cin.ignore();
                obj.addBook();
                break;
            case '4':
                return 0;
            default:
                cout << "Invalid Choice...!" << endl;
        }
    } while (choice != '4');

    return 0;
}
