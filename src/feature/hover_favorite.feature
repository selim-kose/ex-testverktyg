## U6 - Visuell indikation för favoritmarkering

#Som användare
#vill jag att favoritikonen visas genomskinlig när jag för musen över en bok i katalogen
#så att jag förstår att boken går att markera som favorit.


Feature: Hover favorite

    Scenario:
        Given users is on the main paige
        When user hovers over a book title
        Then the favorite heart icon should appear transparent