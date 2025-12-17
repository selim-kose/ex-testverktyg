## U5

#Som en användare vill jag kunna lägga till böcker i katalogen som sedan syns i katalogvyn
#så att jag kan favoritmarkera de



Feature: Add books

  Scenario: Add new books
    Given user is on the main pages
    When user clicks on the "Lägg till bok" button
    When user adds the following books:
        | book_title            | book_author           |
        | The Great Gatsby      | F. Scott Fitzgerald   |
        | To Kill a Mockingbird | Harper Lee             |
        | 1984                  | George Orwell          |
    And user clicks on the "Katalog" button
    Then the books should appear in the book list