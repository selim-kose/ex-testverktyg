## U2 - Avmarkera favorit i katalogen

#Som användare
#vill jag kunna avmarkera en bok som favorit i katalogvyn
#så att jag kan ta bort böcker som inte längre är mina favoriter.


Feature: Remove favorite marking

  Scenario: Remove favorite marking
    Given user is on the main page and a book is marked as favorite
    When user clicks on a filled heart icon next to a book title
    Then the heart icon should be unfilled, indicating the book is unmarked as favorite