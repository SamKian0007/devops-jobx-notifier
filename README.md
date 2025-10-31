# DevOps Job Explorer — Final Project

This project was developed by **Sam Parsakian**, **Veronika**, and **Kenan** as part of the final Python course assignment.
A structured Flask web application was created to search, display, and notify users about DevOps job openings in Sweden.

---

## Project Concept and Planning

The development began with a **basic project skeleton** that included the main Flask structure and folders for templates, static files, and data.
Discussions and planning were carried out through **Miro**, where different ideas for data sources and user interaction were evaluated.
After reviewing available public APIs, the team agreed to use the **Arbetsförmedlingen (JobTech API)** to fetch job listings.
To enable notifications, **Twilio’s email API** was selected as the second external provider.

---

## Implementation Process

The coding process was divided into several stages:

1. **Core Application Logic**Flask routes were implemented to display job listings, visualize them using Plotly charts, perform local searches, and apply filters.Each feature was connected to the JobTech API for live data fetching and a local JSON file for offline filtering.
2. **Email Notification**A notification function was implemented to send summarized job information to users by email through the Twilio SendGrid service.
3. **Front-End Templates**HTML templates were written using Bootstrap styling, providing a clean, responsive interface for all pages.
4. **Testing and Verification**
   Tests were written using **pytest** throughout the development — both during and after feature implementation.
   The tests verified route responses, mocked API calls, and validated email notifications to ensure the app’s practicality and reliability.

---

## Testing Results

- A total of **11 tests** were executed using `pytest` and `pytest-flask`.
- All tests passed successfully, achieving about **72% overall coverage**.
- Core routes and business logic reached full or near-full coverage, confirming correct behavior for all major user actions.

---

## Outcome

The application successfully demonstrates integration with external APIs, structured Flask design, and functional testing.
It was built collaboratively and tested iteratively, ensuring both **code quality** and **realistic functionality** according to final project requirements.
