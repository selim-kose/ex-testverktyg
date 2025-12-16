## U3
#Som en användare vill jag kunna lägga till böcker
#så att jag vet vilka böcker jag har läst

Feature: Add book

  Scenario: Add a new books
    Given user is on the main pages
    When user clicks on the "Lägg till bok" button
    When user adds the following books:
        | book_title            | book_author           |
        | The Great Gatsby      | F. Scott Fitzgerald   |
        | To Kill a Mockingbird | Harper Lee             |
        | 1984                  | George Orwell          |
    And user clicks on the "Katalog" button
    Then the books should appear in the book list