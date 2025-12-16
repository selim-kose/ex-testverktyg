## U3
#Som en användare vill jag kunna lägga till böcker
#så att jag vet vilka böcker jag har läst

Feature: Add book

  Scenario: Add a new book
    Given user is on the main page
    When user clicks on the "Lägg till bok" button
    And user fills in the book title
    And user fills in the author
    And user submits the form by pressing the "Lägg till ny bok" button
    And user click on the "Katalog" button
    Then the new book should appear in the book list