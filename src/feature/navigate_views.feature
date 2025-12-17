## U7 - Navigera mellan vyer

#Som användare
#vill jag kunna navigera mellan vyerna “Katalog”, “Lägg till bok” och “Mina böcker”
#så att jag enkelt kan använda alla funktioner på webbplatsen.

Feature: Navigate views

    Scenario:
        Given user is on the main paige
        Then user should see the catalog of books
        When user klicks on "Lägg till bok"
        Then user should see "Titel" and "Författare" input fields
        When user clicks on "Mina böcker"
        Then user should see the list of favorite books


