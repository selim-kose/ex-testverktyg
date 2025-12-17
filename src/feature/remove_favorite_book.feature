## U4 - Uppdaterad lista vid avmarkering  

#Som användare
#vill jag att en bok tas bort från “Mina böcker” när jag avmarkerar den som favorit
#så att listan alltid visar mina aktuella favoritböcker.

Feature: Remove favorite book
    Scenario: 
        Given user is on the main page and marks a book as favorite
        When user clicks on a "Mina böcker" button
        Then user should see the marked book listed as a favorite
        When user clicks on "Katalog" button
        And user clicks on the filled heart icon next to a book title
        Then the heart icon should be removed, indicating the book is unmarked as favorite
        When user clicks on "Mina böcker" button again
        Then user should not see the book listed as a favorite anymore