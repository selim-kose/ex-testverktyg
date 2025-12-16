# U1
#som en anvvändare vill jag vill jag kunna favoritmarkera böcker
#så att jag har koll på vad jag vill läsa

Feature: Add favorite marking

  Scenario: Add favorite marking
    Given user is on the main page
    When user clicks on a heart icon next to a book title
    Then the heart icon should be filled, indicating the book is marked as favorite 
