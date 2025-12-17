## U7

#Som en användare vill jag kunna navigera till de 3 olika vyerna, "Katalog", "Lägg till bok" och "Mina böcker"
#så att det är möjligt att navigera till varje sida

Feature: Navigate views

    Scenario:
        Given user is on the main paige
        Then user should see the catalog of books
        When user klicks on "Lägg till bok"
        Then user should see "Titel" and "Författare" labels
        When user clicks on "Mina böcker"
        Then user should see the list of favorite books


