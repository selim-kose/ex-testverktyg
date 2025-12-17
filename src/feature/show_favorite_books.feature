## U3 - Visa favoritböcker i “Mina böcker”

#Som användare
#vill jag kunna se alla mina favoritmarkerade böcker i vyn “Mina böcker”
#så att jag får en samlad lista över mina favoriter.


Feature: Show favorite books
    
    Scenario:
        Given user is on the main paige and no books is marked as favorite
        When user klicks on heart icon next to a book title
        Then the heart should be filled, indicating the book is marked as favorite
        When user clicks on "Mina böcker" button
        Then user should see the book listed as a favorite