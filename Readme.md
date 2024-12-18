# AI Daily Task Assistant - Project Roadmap

This document outlines the steps required to build an AI-powered daily task assistant that integrates with Todoist, uses screen sharing with Google Gemini (Bard), provides task breakdown, and offers voice guidance.

## Overview

This project aims to create an application that will:

1. **Connect to Todoist:** Retrieve and manage tasks from a user's Todoist account.
2. **Share Screen with Gemini:** Enable screen sharing for Gemini (Bard) to visually track tasks and user interactions.
3. **Task Breakdown:** Utilize AI to analyze tasks and suggest smaller, manageable subtasks.
4. **Voice Assistance:** Provide real-time voice guidance to the user during task execution.

## Step-by-Step Tasks

Here's a breakdown of the development process:

**Phase 1: Setup and Core Functionality**

1. **Project Setup:**
   *   [x] **Create a new project directory.**  (e.g., `ai-daily-task-assistant`)
   *   [x] **Choose a programming language and framework.(Django)** 
   *   [ ] **Install necessary libraries.** (e.g., `todoist-api-python`, any web framework related packages, websockets for real time communication, etc.)
   *   [ ] **Initialize a Git repository.**
   *   [ ] **Create a `.gitignore` file.**

2.  **Todoist API Integration:**
    *   [ ] **Create a Todoist developer application** and obtain an API token.
    *   [ ] **Implement authentication with the Todoist API.**
    *   [ ] **Implement functionalities to:**
        *   [ ] **Fetch all active tasks.**
        *   [ ] **Create new tasks.**
        *   [ ] **Update task status (completed, in progress).**
        *   [ ] **Read task descriptions and other details.**

3.  **Basic UI:**
    *  [ ] **Design a very basic UI**
    *  [ ] **Display Todoist task list.**
    *  [ ] **Include basic task controls (start, complete).**

4.  **Screen Sharing Implementation (Proof of Concept):**
    * [ ] **Research available libraries and methods:**
       *  WebRTC could be a potential candidate for the screen share functionality.
       *  Investigate the Gemini API limitations/options.
    * [ ] **Implement a basic screen-sharing mechanism**
    * [ ]  **Establish connection between the app and Gemini.** (This may require external services like a socket server).

**Phase 2: AI Integration**

5.  **Gemini Integration (Basic):**
    *   [ ] **Obtain API key for Google Gemini (Bard) API.**
    *   [ ] **Send text prompts to Gemini** for testing purposes.
    *   [ ] **Receive and display responses from Gemini.**

6.  **Task Breakdown with Gemini:**
    *   [ ] **Design a prompt for Gemini to break down tasks.** (e.g., "Break down the task '{task_name}' into smaller subtasks").
    *   [ ] **Implement logic to send tasks to Gemini.**
    *   [ ] **Parse and display the generated subtasks.**
    *   [ ] **Allow user to accept/reject subtasks.**

7.  **Voice Recognition and TTS:**
    *   [ ] **Choose a voice recognition library/service** (e.g., Web Speech API, Google Cloud Speech-to-Text).
    *   [ ] **Implement basic voice recognition functionality**
    *   [ ] **Choose a text-to-speech library/service** (e.g., Web Speech API, Google Text-to-Speech).
    *   [ ] **Implement basic text-to-speech** functionalities.

**Phase 3: Enhanced Functionality and Polishing**

8. **Real-time screen tracking:**
    *   [ ] **Implement real time screen sharing.**
    *   [ ] **Send regular screen captures to Gemini.**
    *   [ ] **Design prompts to Gemini based on user interactions.**

9.  **Voice Guidance with Gemini:**
    *   [ ] **Develop prompts to guide the user during task completion.** (e.g., "What's the next step?", "You are now doing ...")
    *   [ ] **Use Gemini's response to provide voice prompts** to the user.
    *  [ ] **Manage context** of conversation during voice guidance.

10. **Advanced AI Integration**
    *   [ ] **Personalize task breakdown based on user history.**
    *   [ ] **Implement smart reminders based on task progress.**

11. **UI/UX Improvement:**
    *   [ ] **Enhance the UI with better visual appeal and user experience.**
    *   [ ] **Improve error handling and user feedback.**

12. **Testing and Debugging:**
    *   [ ] **Thoroughly test all features and fix bugs.**
    *   [ ] **Gather user feedback and iterate on the design.**

13. **Deployment:**
    *  [ ] **Choose a deployment platform** (e.g., Heroku, AWS, Google Cloud)
    *  [ ] **Deploy the application.**

## Technologies to Consider

*   **Programming Languages:** Python, JavaScript
*   **Frameworks:**
    *   **Backend:** Flask, Django, Express.js
    *   **Frontend:** React, Vue.js, Angular
*   **APIs:** Todoist API, Google Gemini API (Bard), Web Speech API, Google Cloud APIs
*   **Libraries:**
    *   `todoist-api-python` (Python) or equivalent for your chosen language.
    *   `websockets`
    *   WebRTC Library if necessary
    *   Any UI frameworks libraries
*  **Deployment:** Heroku, AWS, Google Cloud

## Important Considerations

*   **API Rate Limiting:** Be aware of API rate limits and implement necessary logic.
*   **User Privacy:** Handle user data securely and transparently.
*   **Error Handling:** Implement proper error handling and logging.
*   **Real-time Communication:** Utilize websockets or similar technologies for real-time screen sharing and voice interaction.
*   **Scalability:** Design the application with scalability in mind.
*   **Security:**  Ensure security best practices throughout the development process.

## Next Steps

1.  **Start by completing the tasks in Phase 1.**
2.  **Break down each task into smaller, more manageable subtasks.**
3.  **Use Git to track your progress and version control.**
4.  **Document your code and APIs thoroughly.**

This roadmap should give you a good starting point for building your AI Daily Task Assistant. Good luck!