## U6

#Som en användare vill jag att hjärtat för favorit markering ska visas genomskinlig när jag flyttar musen övern boktiteln
#så att jag vet att det går att favoritmarkera böcker


Feature: Hover favorite

    Scenario:
        Given user is on the main paige
        When user hovers over a book title
        Then the favorite heart icon should appear transparent