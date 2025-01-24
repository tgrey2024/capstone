# AI Augmented FullStack Bootcamp - Individual Capstone Project - Remineez Digital Scrapbooks <a id="top"/>
![logoWithTitle_small](https://github.com/user-attachments/assets/7346270b-a846-4ff9-bfc9-d2c90da22432)

## Overview
Reminineez is a Django-based digital scrapbook app that allows authenticated users to create individualised scrapbooks of photos, songs, etc for seniors with problems with memory and/or language, to serve as a memory aid as part of their reminiscence therapy. Research has shown that personalised memory aids can significantly improve the quality and quantity of conversations with carers and loved ones, stimulate neural connections and enhances self-esteem and wellbeing. Conversations about the past can also help to bring the family closer and build stronger bonds.

Live site: [https://remineez-6fa07ac70d1d.herokuapp.com/](https://remineez-6fa07ac70d1d.herokuapp.com/)

## Table of Contents
- [User Experience Design Process](#user-experience-design-process)
- [Project Brief](#project-brief)
- [Users](#users)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Mockups](#mockups)
    - [Imagery](#imagery)
    - [Responsive Design](#responsive-design)
- [Key Features](#key-features)
    - [Authentication](#authentication)
    - [Header and Footer Navigation](#header-and-footer-navigation)
    - [Homepage and Published Scrapbooks](#homepage-and-published-scrapbooks)
    - [Accounts Management](#accounts-management)
    - [Log in Status](#log-in-status)
    - [CRUD Functions](#crud-functions)
    - [Access Control](#access-control)
    - [Create and Edit Scrapbooks](#create-and-edit-scrapbooks)
    - [Create and Edit Posts](#create-and-edit-posts)
    - [Post Detail](#post-detail)
    - [Delete Scrapbook or Post](#delete-scrapbook-or-post)
    - [My Scrapbooks](#my-scrapbooks)
    - [Publish Status](#publish-status)
    - [Notifications](#notifications)
    - [Admin Panel](#admin-panel)
    - [Inclusivity Notes](#inclusivity-notes)
- [Deployment](#deployment)
    - [Platform](#platform)
    - [High Level Deployment Steps](#high-level-deployment-steps)
    - [Verification and Validation](#verification-and-validation)
    - [Security Measures](#security-measures)
- [Testing Summary](#testing-summary)
- [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)
- [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
    - [Planning](#planning)
    - [Code Generation](#code-generation)
    - [Content Creation](#content-creation) 
    - [Debugging](#debugging)
    - [Performance and UX Optimisation](#performance-and-ux-optimisation)
    - [Automated Unit Testing](#automated-unit-testing)
    - [Impact on Workflow](#impact-on-workflow)
    - [Use Cases and Reflections](#use-cases-and-reflections)
- [Credits](#credits)


<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## User Experience Design Process
<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Project Brief
<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Users
<strong>Seniors with Memory and/or Language Problems:</strong> These are the primary users for whom the app is designed. These seniors may be dealing with conditions such as dementia or other cognitive impairments. The app aims to enhance their quality of life by providing a personalised digital space where they can compile cherished photos, favourite songs, newspaper articles, videos and other memory aids. This resource serves as a valuable tool to help them recall significant events, personal stories, maintain cognitive function and engage more actively with their surroundings. Colour blindness, in particular colour vision deterioration e.g. tritanopia ("blue-yellow" colour blindness) is also common in those aged 70 and over.

<strong>Carers and Loved Ones:</strong> These users include family members, friends and caregivers who interact with the seniors on a daily basis. They may be helping the seniors to use the app to create, update and manage the individual memory books/blogs for their loved ones, or they may be the ones creating the blogs on behalf of the seniors. By incorporating familiar and beloved content, they can improve the quality and quantity of their conversations with the seniors. This process not only helps to strengthen emotional bonds but also provides carers with insights into the senior's life story, enabling more empathetic and tailored care.

<strong>Developer/Admin:</strong> This superuser is responsible for developing, maintaining and updating the web app. They ensure the app is functional, secure, user friendly and handles any user support and content issues.


<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### User Stories

Here are all the user stories that have been prioritised (all must have and some should have ones) for the current implementation of the webapp:

| User Stories                                    | MoSCoW priority           |  Status |
| ----------------------------------------------- |:-------------------------:| -------:|
| User-Friendly Navigation and Responsive Design  | must have                 |   Done  |
| Account Registration                            | must have                 |   Done  |
| View Paginated Posts                            | must have                 |   Done  |
| Create Scrapbook                                | must have                 |   Done  |
| Read Scrapbook                                  | must have                 |   Done  |
| Update Scrapbook Metadata                       | must have                 |   Done  |
| Delete Scrapbook                                | must have                 |   Done  |
| Create Post                                     | must have                 |   Done  |
| Open a Post                                     | must have                 |   Done  |
| Update a Post                                   | must have                 |   Done  |
| Delete a Post                                   | must have                 |   Done  |
| CRUD Draft Scrapbook                            | must have                 |   Done  |
| User Authentication                             | must have                 |   Done  |
| Change Post and Scrapbook Status                | must have                 |   Done  |
| Post and Scrapbook Access Control               | must have                 |   Done  |
| Give Shared Access to Nominated Users           | should have               |   Done  |
| View About Page                                 | should have               |   Done  |

All user stories were logged on the [Kanban Project Board](https://github.com/users/tgrey2024/projects/14) on GitHub Projects, along with the assessment criteria and expected performance for the project, which were also prioritised as must-have.

As well as using the Project Board to track progress on our project, I also used it during testing to log any significant bugs that need to be fixed before the project deadline. These were then assigned and prioritised alongside other issues and user stories.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Design
### Wireframes
Based on the user stories, I used Balsamiq to design the wireframes for the main UI, starting with mobile first.

<details>
  <summary>Mobile devices</summary>
    Here are the wireframes for mobile devices:
    
![mobile](https://github.com/user-attachments/assets/c668523a-b7b0-46ca-9401-1489da1ae9bb)

</details>
<details>
  <summary>iPad screens</summary>
    Here are the wireframes for tablets and iPads:
    
![ipads](https://github.com/user-attachments/assets/83e3f658-86aa-46b5-b37b-e7dc06da84bd)

</details>
<details>
  <summary>Laptop and larger screens</summary>
    Here are the wireframes for larger screens and laptops:
    
![laptops](https://github.com/user-attachments/assets/1f76da7f-b9d3-4ddb-8175-a4e849c5b015)

</details>

### User Flow

To better understand how users would need to navigate through the webapp for different use cases, I mapped the different user journeys in a user flow diagram as shown below:
<details>
  <summary>User Flow Diagram</summary>

An unregistered site user would be able to visit the Homepage and About page, but in order to use the system fully they would need to either Register on the Signup page or Login if they have already signed up. These are indicated by the pink arrows in the diagram.

Once the user has logged in, the navbar offers more options. The blue arrows show how logged-in users can go to My Scrapbooks to access their own scrapboooks, or go to Shared Scrapbooks to see any scrapbooks that have been shared with them.

The purple arrows show the user flows for the creation, updating and deleting of both Scrapbooks and the Posts within them. They also show how users can share access to their own scrapbooks with specific users.
    
![userflow](https://github.com/user-attachments/assets/304aee1f-f7c7-418b-9a85-0b2bca4cab89)

</details>


### Colour Scheme
The aim of the web app is for users to collate and showcase the memorable photos and other media that they cherish, while making it cheerful and calm for users of any age or gender. A lot of photos in the sample research are black and white or sepia toned. I used [Coolors](https://coolors.co/174f11-f2e3bc-2660a4-c47335-a15317-56351e) to find a palette that would complement those tones:<br>
![colour palette_v2](https://github.com/user-attachments/assets/e6e7cee8-61a9-4ce7-b837-621b6819ab24)<br><br>
I also needed to check the colour palette works for any colour blind users, particularly Tritan colour blindness, which becomes more common as one ages. The symptoms include difficulty differentiating blue and green, yellow and pink, purple and red, etc. I therefore also used the colour blindness check in Coolors to test the colours are distinguishable for users with Tritanopia.<br>
![tritanopia colour palette_v2](https://github.com/user-attachments/assets/de444e1e-81ee-4afb-807a-b6e324e88655)<br>

It is also important to design for a higher colour contrast, since many dementia patient also suffers from poor contrast perception. I used the WCAG extension to scan my initial design and found that the key concerns were the colours chosen for the Bootstrap navbar, as shown below on the left.<br>

Once I built the Bootstrap navbar, I tested with different shades of background colours (see middle screenshot below), but I found it difficult to find to get a contrast ratio higher than 4 with the Bootstrap default styles for nav links. By overriding the nav link styles and making the hover colours more vibrant, I managed to improve the WCAG colours above 5 (see below right screenshot).<br>

![navbar test](https://github.com/user-attachments/assets/9a5ecb5c-364d-4efd-a2f6-68457dd29f5f)<br>
<br>
![WCAG_navbar link text](https://github.com/user-attachments/assets/4a5dc435-642b-478c-b5d9-05b14abade01)


### Typography
After testing different font combinations on [Google Fonts](https://fonts.google.com/) and [Online Fonts](https://online-fonts.com/), I have chosen sans-serif fonts as they are easier to read for most users.<br>

Philosopher<br>
![PhilosopherExample](https://github.com/user-attachments/assets/75024fdb-5e29-45a9-b2ea-bdb7c9e02cf3)<br>
I have chosen Philosopher for my titles and headings, as it is more distinctive with its playful kicks. Google Fonts has been used as these are convenient to embed into the CSS file as an @import. Open Sans is used as a backup font.<br>

<br>Lucida Sans Unicode<br>
![LucidaExample](https://github.com/user-attachments/assets/8cc52d4c-1690-47b2-943c-1b9ea508e054)<br>
For the paragraph and menu text, I have picked the widely-available and reliable Lucida Sans Unicode because of its legibility and support for different character sets.<br>






  - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]


### Mockups
  - [Canva Mockup](https://www.canva.com/design/DAGbzmo_8Iw/GjNxoK5LvaTmJT1r-8IEiQ/view?utm_content=DAGbzmo_8Iw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hf37b8eca3e)
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]


### Imagery
add AI and Pexels imagery

### Responsive Design
add amiresponsive screenshot



<p align="right"><a href="#top">Back to top</a></p>

## Key Features
### Authentication
Parts of the site are only accessible when users are registered and logged in:

| Features                           | Unauthenticated Users     |  Authenticated Users |
| ---------------------------------- |:-------------------------:| --------------------:|
| Homepage                           |           Yes             |          Yes         |
| About                              |           Yes             |          Yes         |
| My Scrapbooks                      |           No              |          Yes         |
| Register                           |           Yes             |          No          |
| Login                              |           Yes             |          No          |
| Logout                             |           No              |          Yes         |

### Header and Footer Navigation
[add screenshots, show how they use the base template, how they change for logged in and unlogged in users]

### Homepage and Published Scrapbooks
### Accounts Management
[add screenshots, show how they use the same template, register and cancel buttons]
### Log in Status
[add screenshots of logged in status text with icon, plus shortened version for small screens]
### CRUD Functions

Here is a summary of the CRUD functionalities implemented. 
|     Features          |     Create    |      Read      |     Update     |      Delete     |
| --------------------- |:-------------:|---------------:|---------------:| ---------------:|
| Draft Scrapbook       |Logged-in users|   Author only  |   Author only  |   Author only   |
| Private Scrapbook     |Logged-in users|   Author only  |   Author only  |   Author only   |
| Published Scrapbook   |Logged-in users|   All users    |   Author only  |   Author only   |
| Draft Post            |Logged-in users|   Author only  |   Author only  |   Author only   |
| Private Post          |Logged-in users|   Author only  |   Author only  |   Author only   |
| Published Post        |Logged-in users|   All users    |   Author only  |   Author only   |

All users, logged-in or not, can read published scrapbooks and posts. All other CRUD functions are all only accessible to logged-in users.

### Access Control
### Create and Edit Scrapbooks
[add screenshots to show they use the same template, context passed from each view to determine and dynamically change content for better UI]
### Create and Edit Posts
[add screenshots to show they use the same template, context passed from each view to determine and dynamically change content for better UI]
### Post Detail
[add screenshots, set size for photo but max-width limited on very large screens]

### Delete Scrapbook or Post
[add screenshots, show how they use the same template, confirmation and cancel buttons]

### My Scrapbooks
### Publish Status
[add screenshots, show how they are set and updated, icons, how it determines whether they can be accessed]

### Notifications
[add screenshots, list which messages get sent to alert, disappear after 15s if not closed]

### Admin Panel
[add screenshots, show which columns were added]

### Inclusivity Notes
  - [Mention how the features address the needs of diverse users, including those with SEND.]
<p align="right"><a href="#top">Back to top</a></p>

## Deployment
### Platform
The web app is hosted on Heroku using Eco Dynos, and is deployed via the designated Github repository.

A request is made via the CI Database Maker, which generates a PostgreSQL database hosted on AWS, with the database credentials sent to the email address provided in the request.

### High-Level Deployment Steps
The [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template) was used to create the GitHub repository, so that the website could be developed in the correct setup of Gitpod IDE.

The GitHub Copilot extension was also installed in my local client version of MS VS Code, which was also connected with the same GitHub repository and linked to Gitpod via SSH. This allows for AI pair programming in the initial stages of development to create certain sections faster.

The deployment process is as follows:
1. Login to your GitHub profile and go to [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template). **Use this template** and **Create a new repository**.
2. Open the Code Institute Gitpod IDE workspace. Open VS Code locally, connect and open the workspace. Create the MVP.
3. Login to Heroku and create a new app using a unique name and select the correct region. Add Config Vars in Settings.
4. Install web server gunicorn and freeze requirements.
5. Create a new Procfile in the root directory and specify the running of the web app with process type as gunicorn in the Procfile.
6. Add deployed apps to ALLOWED_HOSTS in settings.py, and set Debug = False. Add, commit and push to the Github repo.
7. In Heroku, go to Deploy tab, search for the correct Github repo and under manual deploy click **Deploy Branch**.
8. **View app** to verify that it is been deployed correctly. This deployed site can now be validated and tested e.g. in Chrome Dev Tools.
9. In the app's Resources tab, check that Eco Dynos are used and remove any unnecessary Add-ons.
10. Subsequent changes to the code will need to be pushed to the Github repo and manually deployed on Heroku.

### Verification and Validation
  - Steps taken to verify the deployed version matches the development version in functionality.
  - [Include any additional checks to ensure accessibility of the deployed application.]

### Security Measures
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.
<p align="right"><a href="#top">Back to top</a></p>

Validation of HTML/CSS, Lighthouse Audits, Bugs
#### HTML Validation
Add details of HTML validation:
<details>
  <summary>HTML validation screenshots:</summary>
  <b>Add screenshots</b>
</details>

#### CSS Validation
Add details of CSS validation:
<details>
  <summary>CSS validation screenshots:</summary>
  <b>Add screenshots</b>
</details>


#### Lighthouse Audit
### Bugs yet to be Fixed
*  

<p align="right"><a href="#top">Back to top</a></p>

## Testing Summary

### Manual Testing
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
### Automated Testing
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]
<p align="right"><a href="#top">Back to top</a></p>

## Future Enhancements
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.
- Manage Shared Access:
  - in addition to creating shared access, users could also have finer control of shared access so they can:
      - see who they have given access to
      - update or remove the access so they can manage who has access to their creations and when
      - manage permissions by family or friend groups
- Incorporate links, videos and audio clips in their scrapbook posts, as multimedia content such as songs, soundbytes, music and contemporary video footage can all enrich the experience of reminiscencing and make the experience more immersive.
- Audio input as a means of scrapbooking, whether as sound clips or through voice-to-text input, making it easier for users to enter content about their memories and emotions, thus encouraging users to express themselves through speech.

<p align="right"><a href="#top">Back to top</a></p>

## Technologies Used
### Languages and Technologies
![Static Badge](https://img.shields.io/badge/HTML5-Language-blue)
![Static Badge](https://img.shields.io/badge/CSS3-Language-blue)
![Static Badge](https://img.shields.io/badge/GitHub-RepoHosting-black)
Heroku
Cloudinary
![Static Badge](https://img.shields.io/badge/Gitpod-IDE-yellow)
Javascript
Python
Django
DB PostgreSQL
Whitenoise
AllAuth

### Libraries and Frameworks
![Static Badge](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Static Badge](https://img.shields.io/badge/FontAwesome-icons-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-Typography-blue)

Django, AllAuth, Whitenoise, Crispy Forms, Crispy Bootstrap, Summernote, Pillow
All Django packages installed is listed in requirements.txt(add link).

### Tools and Programs
![Static Badge](https://img.shields.io/badge/LogoAI-LogoGenerator-red)
![Static Badge](https://img.shields.io/badge/Favicon.io-icons-navy)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/MSCopilot-AI-orange)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI-orange)
Perplexity AI
DiagramGPT/Eraser
Coolers
WCAG

<p align="right"><a href="#top">Back to top</a></p>

## AI Implementation and Orchestration
### Planning
[user stories, identify entities and relationships, generate initial ERD]
### Code Generation
[review below before deadline]
The GitHub Copilot extension was installed in our local versions of Visual Studio Code. We were therefore able to write prompts or highlight functions in pseudocode and ask Copilot to suggest code snippets. Suggestions needed to be reviewed before they were included, as occassionally code may refer to e.g. variables that have not been declared or not yet been imported.

Copilot was also able to suggest higher-level implementation ideas, e.g. when I was researching options for sharing content between users privately. Copilot was prompted for options suitable for a junior developer to implement, and it provided three options including pros and cons, and suggested reading on the subject.

When I come across suggested code that I don't understand, I prompted Copilot for an explanation of the selected code with a breakdown of each step and a concise summary. 

Occassionally it can be annoying when Copilot suggests code in ghost text unnecessarily, or introduces additional closing tags or brackets unnecessarily. Nonetheless, when used with specific prompts and context, some of the results provided by Copilot have been mostly usable, thus speeding up development.

[    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.]

### Content Creation
[DALL-E images, post text]
### Debugging
Copilot was regularly used for debugging code, either by highlighting specific code in the inline editor, or using @workspace if Copilot needs more context. During automated testing, any failure errors are copied into the Copilot chat to give AI a better idea of what needs to be fixed.

When using Chrome DevTools to inspect the preview or deployed pages, Chrome DevTools AI Assistance panel was also used to explain the errors raised in the Console.

[    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.]

### Performance and UX Optimisation
While learning to write class-based views, apart from reading Django references and documentation, I also prompted Copilot to debug the class-based views that were written. Once tested to run correctly, Copilot was prompted to optimise on the code. 
[give outcome]
Again, this needed to be tested fully before it was incorporated into the code. Running the resultant code produces the same result as before.

[    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.]

### Automated Unit Testing
Automated tests were written by prompting Copilot for test skeletons for unit tests and edge tests without implementation. I selected the relevant test cases to include and Copilot suggested ghost text for each one which I accepted using the Tab key or Ctrl+-> key. Each test case had to be reviewed and tested separately, and Copilot also helped with suggesting fixes to the models, views and forms, although it was also important to test that the changes hasn't broken any functions in the affected part of the app.
[    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.]

### Impact on Workflow
On the whole, it has been useful to pair program with Copilot and use it for debugging and testing as we code. Due to the tight timescale of the project, I used AI wherever possible to reduce development time, from creating user stories to suggesting commit messages. When 
[  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.]
  - 
### Use Cases and Reflections
[Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.]

<p align="right"><a href="#top">Back to top</a></p>



## Credits
### Code References
[Classy Class-Based Views](https://ccbv.co.uk/) - references to Django class-based views with examples and links to Django documentation
Example of how to override Bootstrap styles for navbar links in custom CSS: [CodePen](https://codepen.io/skde/pen/ExyrBYg)

### Content References
MS Copilot was used to generate much of the homepage and blog content.

### Media References
#### Photos:
* Pexels - [https://www.pexels.com/](https://www.pexels.com/)

#### Acknowledgements
Many thanks to my patient testers for helping me test throughout development, 
Everyone in my WECA group who have been so helpful and supportive leading up to this project, and
Code Institute tutors (Dillon, Mark and Roo) for answering my endless questions
<p align="right"><a href="#top">Back to top</a></p>
