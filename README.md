# AI Augmented FullStack Bootcamp - Individual Capstone Project - Remineez Digital Scrapbooks <a id="top"/>
![logoWithTitle_small](https://github.com/user-attachments/assets/7346270b-a846-4ff9-bfc9-d2c90da22432)

## Overview
Reminineez is a Django-based digital scrapbook app that allows authenticated users to create individualised scrapbooks of photos, songs, etc for seniors with problems with memory and/or language, to serve as a memory aid as part of their reminiscence therapy. Research has shown that personalised memory aids can significantly improve the quality and quantity of conversations with carers and loved ones, stimulate neural connections and enhances self-esteem and wellbeing. Conversations about the past can also help to bring the family closer and build stronger bonds.

Live site: [https://remineez-6fa07ac70d1d.herokuapp.com/](https://remineez-6fa07ac70d1d.herokuapp.com/)

## Table of Contents
- [User Experience Design Process](#user-experience-design-process)
    - [Problem Statement](#problem-statement)
    - [Project Brief](#project-brief)
    - [Use Case](#use-case)
    - [Users](#users)
- [Planning](#planning)
    - [User Stories](#user-stories)
    - [Project Scope and Schedule](#project-scope-and-schedule)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [User Flow](#user-flow)
    - [Database](#database)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Mockups](#mockups)
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

### Problem Statement

Many people with dementia or similar cognitive impairments may experience significant challenges with memory and language, making it difficult to recall names, words and faces, which affects their daily tasks, their wellbeing and their self-esteem. Carers and loved ones find it difficult to understand and connect with the patient, which can impact on their well-being. Visual aids are often used in occupational therapy, but visual aids with personal meaning could encourage more neural connections to be made, thus can further enhance cognitive and speech development.

Reminiscence Therapy is a form of therapy that uses prompts such as photographs, music, or familiar items to encourage individuals, particularly the elderly, to recall and share memories from their past. Potential benefits include:
- Enhances mood and reduces depression
- Improves cognitive function and memory recall
- Strengthens personal identity and sense of self
- Encourages social interaction and reduces isolation
- Provides a focus to initiate meaningful conversation

## Project Brief

The aim is to develop a digital scrapbooking solution to support users in their reminiscence therapy, through which they could improve their cognitive functions, speech and wellbeing.

The site user's goal is to create and use personal digital scrapbooks of photos of their mementos as a means of recalling their memories for cognitive development, and a means of communicating valued thoughts and emotions with their loved ones, carers and therapists.

The project goal is to produce a functional prototype of a user-friendly scrapbook web app which facilitates publishing and private-sharing of scrapbooks, that can be tested with users as a proof of concept and to further define user requirements.

### Use Case

Research has shown that memory aids such as individualised photo memory books can improve communications between seniors with dementia and their family, and reminiscence therapy can stimulate memory function, enhance mood, increase social interaction and combat loneliness, low self-esteem and depression. 

### Users

<strong>Seniors with Memory and/or Language Problems:</strong> These are the primary users for whom the app is designed. These seniors may be dealing with conditions such as dementia or other cognitive impairments. The app aims to enhance their quality of life by providing a personalised digital space where they can compile cherished photos, favourite songs, newspaper articles, videos and other memory aids. This resource serves as a valuable tool to help them recall significant events, personal stories, maintain cognitive function and engage more actively with their surroundings. Colour blindness, in particular colour vision deterioration e.g. tritanopia ("blue-yellow" colour blindness) is also common in those aged 70 and over.

<strong>Carers and Loved Ones:</strong> These users include family members, friends and caregivers who interact with the seniors on a daily basis. They may be helping the seniors to use the app to create, update and manage the individual memory books/blogs for their loved ones, or they may be the ones creating the blogs on behalf of the seniors. By incorporating familiar and beloved content, they can improve the quality and quantity of their conversations with the seniors. This process not only helps to strengthen emotional bonds but also provides carers with insights into the senior's life story, enabling more empathetic and tailored care.

<strong>Developer/Admin:</strong> This superuser is responsible for developing, maintaining and updating the web app. They ensure the app is functional, secure, user friendly and handles any user support and content issues.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Planning

### User Stories

Here are all the user stories that have been prioritised (all must have and some should have ones) for the current implementation of the webapp:

| User Stories                                    | MoSCoW priority           |  Status |
|:----------------------------------------------- |:-------------------------:|:-------:|
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
| Homepage Hero and Testimonials                  | should have               |   Done  |
| Interactive Scrapbook and Post cards            | should have               |   Done  |

All user stories were logged on the [Kanban Project Board](https://github.com/users/tgrey2024/projects/14) on GitHub Projects, along with the assessment criteria and expected performance for the project, which were also prioritised as must-have.

As well as using the Project Board to track progress on our project, I also used it during testing to log any significant bugs that need to be fixed before the project deadline. These were then assigned and prioritised alongside other issues and user stories.

### Project Scope and Schedule

The broad project plan was to secure the MVP, fully tested and documented sufficiently before incorporating the optional should have and could have features.

| Milestone |                      Scope                      |      Scheduled    |       Actual      |
|:----------|:----------------------------------------------- |:-----------------:|:-----------------:|
| v0.1      | Plan, design, Django and Heroku setup           |  Day 1-3          |  Day 1-2          |
| v1.0      | MVP (all must-haves), automated tests           |  Day 1-7          |  Day 1-7          |
| v1.0.1    | Initial validation, manual tests, bug fixes     |  Day 6-8          |  Day 6-9          |
| v1.1      | Shared Access, unit tests and manual tests      |  Day 9-10         |  Day 9-12         |
| v1.2      | Homepage Add-ons and About Page                 |  Day 10-11        |  Day 11           |
| v1.2.1    | Animation and other UX enhancements             |  Day 12           |  Day 12           |
| v1.2.2    | Polish, integration test, wrap up               |  Day 12-14        |  Day 12-14        |


<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Design
When designing for the UI for Remineez, it was important to remember that our primary target users are seniors who may be diagnosed with dementia or other cognitive challenges. Colour contrast needs to be sufficient for improved readability and accessibility. There may also be certain vision challenges due to the age of this user group, e.g. colour blindness. Many senior users may already use assistive tools on their devices, such as screen readers. It is important to design the site for accessibility. Semantic tags, image alt tags and ARIA labels help screen reader users to understand and navigate the content more easily. Font Awesome icons have been used to help remind users what each function does on the page. The early deployed site was tested for accessibility using tools like Chrome Dev Tools Lighthouse Audit and <a href="https://wave.webaim.org/" target="blank">WAVE Web Accessibility Evaluation Tool</a> and bugs were logged and prioritised for fixing.

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

### Database
Using the user stories, Perplexity gave me a schema of the entities, fields and relationships. Using this, Eraser DiagramGPT provided an initial ERD from which I built the initial models.
![ERD](https://github.com/user-attachments/assets/2435aaff-e7db-42a4-8e20-1806ca021293)

During MVP development and as new requirements were introduced with subsequent releases, it was necessary to change the model to fit the requirements. With every change in the Django model, it is necessary to make migrations and migrate in order to control the versions of the model and map the changes.

Here is the ERD of the final model:

![image](https://github.com/user-attachments/assets/17122097-8c80-448c-b793-34b1e681ce11)

Post - a container for a single image asset, with a title and some caption content, an author who is a registered and logged in user and date-time fields when the post is created and updated. The slug is system-generated as a unique id which forms part of the URL for CRUD functions.

Scrapbook - a collection of Posts, which also has a title, slug and content text, along with an author, create and updated fields. The description field is an author to make notes to themselves for producing the scrapbook. This 'note-to-self' is only visible to the author.

User - a registered user who is identified by their username and has a password for logging in.

SharedAccess - when an author (User A) wants to share his/her scrapbook with User B, a new instance of SharedAccess is created for User B as the user of the SharedAccess, shared_by User A of a specific scrapbook. 

In the current version scrapbooks are shared at the Scrapbook level, ie. all posts in the shared Scrapbook are also shared. In future versions the Post-SharedAccess could be fully implemented so users can have finer control of the sharing of posts in the same way as the sharing of scrapbooks (see Future Enhancements on the sharing function).

### Colour Scheme
The aim of the web app is for users to collate and showcase the memorable photos and other media that they cherish, while making it cheerful and calm for users of any age or gender. A lot of photos in the sample research are black and white or sepia toned. I used [Coolors](https://coolors.co/174f11-f2e3bc-2660a4-c47335-a15317-56351e) to find a palette that would complement those tones:<br>
![colour palette_v2](https://github.com/user-attachments/assets/e6e7cee8-61a9-4ce7-b837-621b6819ab24)<br><br>
I also needed to check the colour palette works for any colour blind users, particularly Tritan colour blindness, which becomes more common as one ages. The symptoms include difficulty differentiating blue and green, yellow and pink, purple and red, etc. I therefore also used the colour blindness check in Coolors to test the colours are distinguishable for users with Tritanopia.<br>
![tritanopia colour palette_v2](https://github.com/user-attachments/assets/de444e1e-81ee-4afb-807a-b6e324e88655)<br>

It is also important to design for a higher colour contrast, since many dementia patient also suffers from poor contrast perception. I used the WCAG extension to scan my initial design and found that the key concerns were the colours chosen for the Bootstrap navbar, as shown below on the left.<br>

Once I built the Bootstrap navbar, I tested with different shades of background colours (see middle screenshot below), but I found it difficult to find to get a contrast ratio higher than 4 with the Bootstrap default styles for nav links. By overriding the nav link styles and making the hover colours more vibrant, I managed to improve the WCAG colours above 5 (see below right screenshot).<br>

| Bootstrap Navbar with light brown background | Bootstrap Navbar with mid brown background | Bootstrap Navbar with bespoke white text and yellow hover effect |
|    :----:   |    :----:   |    :----:   |

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

### Imagery

On Pexels, I found a collection of old photos on Pexels that provided a good sample of the range of photos that might be added to a digital scrapbook by the target users, as well as images that could be used to draw users to share and connect with loved ones.

![placeholder](https://github.com/user-attachments/assets/6772097c-88b1-421e-a4e5-063ebba69c4e)
<details>
    <summary>Other Pexels images used</summary>
    
![pexels-rodolfoclix-3031501](https://github.com/user-attachments/assets/53bf2b90-96f2-457f-b18e-c77b5512f73e)
![about](https://github.com/user-attachments/assets/b70e7499-dcf6-4b08-b9c2-ab3c17c0d916)

![class photo](https://github.com/user-attachments/assets/01db0a23-a54c-4714-ba83-faa5a5a4a8b4)

![teddies](https://github.com/user-attachments/assets/12a76682-8362-43b2-816c-b79630fe24ce)

![pexels-jason-shi-2104613-29549028](https://github.com/user-attachments/assets/aa1f8465-9b74-4860-97e1-65bf7795e3a9)

</details>




MS Copilot and DALL-E also provided some AI generated imagery.

![carousel1](https://github.com/user-attachments/assets/ffa8f5b1-cbc5-4971-b464-e00984c0dc3c)

<details>
    <summary>Other AI generated images</summary>
    
![close-up of old photos and letters with less clutter](https://github.com/user-attachments/assets/2a2e83f2-bfe9-4f83-a027-5acc42b74ac7)
    
![carousel2](https://github.com/user-attachments/assets/64257867-a7b3-40a5-91f0-d40384713619)
    
![elderly patients making a digital scrapbook](https://github.com/user-attachments/assets/a8fb5f42-843f-4d68-adb3-f624c2f26c73)

</details>

### Mockups
It is important to involve users early in the project to discuss product requirements. Canva was used to sketch a [mockup of the Homepage and About page](https://www.canva.com/design/DAGbzmo_8Iw/GjNxoK5LvaTmJT1r-8IEiQ/view?utm_content=DAGbzmo_8Iw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hf37b8eca3e). Using the preview mode, the UI design was user tested with a small sample of potential users, including users from the primary target age group and profile, and allowed for quick changes to the layout and colour palette which helped to confirm the design before building the site.

Users were keen to know on the homepage what the product is and whether it is for them. This is valuable but not key to deliverying value as part of the MVP, hence it was only prioritised as a should-have.
  
  ![image](https://github.com/user-attachments/assets/18a313f7-7db7-4e96-8aed-139c02aec140)

#### Design Rationale
  - [Explain key design decisions, how accessibility guidelines (e.g., WCAG) were integrated.]
  -   - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]



#### Reasoning For Any Final Changes
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

### Responsive Design

Since most users are expected to access the site on mobile devices, the UI has been designed with a mobile first approach. The site is responsive to different screen sizes as it was built using components from the Bootstrap Library.

![responsive](https://github.com/user-attachments/assets/1f39077f-45df-4424-b8c6-231e805caa59)


<p align="right"><a href="#top">Back to top</a></p>

## Key Features
### Authentication
Parts of the site are only accessible when users are registered and logged in:
| Features                           | Unauthenticated Users     |  Authenticated Users |
|:---------------------------------- |:-------------------------:|:--------------------:|
| Homepage                           |           Yes             |          Yes         |
| About                              |           Yes             |          Yes         |
| My Scrapbooks                      |           No              |          Yes         |
| Shared Scrapbooks                  |           No              |          Yes         |
| Register                           |           Yes             |          No          |
| Login                              |           Yes             |          No          |
| Logout                             |           No              |          Yes         |

### Header and Footer Navigation
[add screenshots, show how they use the base template, how they change for logged in and unlogged in users]

A Bootstrap Navbar has been implemented to ensure that the top navigation bar is responsive on all devices. On smaller screens a hamburger icon is used to expand the navbar options:

![image](https://github.com/user-attachments/assets/845e02f2-a62a-4be9-b3a5-4f55f2617f4f)

The midtone brown (#a15317) has been chosen from the colour palette for better contrast. To overcome the colour contrast issue described earlier, the colours for the Bootstrap link and hover have been overridden to use a white (#ffffff) and a brighter yellow (#ffffa7) which are more noticeable and have higher contrast against the navbar background colour.

The Navbar items are different before and after logging in:

For unauthenticated users:
![image](https://github.com/user-attachments/assets/f48b3699-fae9-4926-a887-6b93e6943d5d)

For authenticated users:
![image](https://github.com/user-attachments/assets/2f91ae2b-d6a8-43ba-880f-fcf05c124377)

A simple footer in dark brown(#56351e) has the brand and copyright, with links to social media in more subtle tones. This is also responsive to different screen sizes:

![image](https://github.com/user-attachments/assets/6d3a5a5d-2ed5-402d-b99a-c52ddbb050f1)
![image](https://github.com/user-attachments/assets/01b9771f-89b9-4aff-a1b3-71ce5f1da576)

The navbar in the header and the footer, as well as the notification message, are implemented in the base template, which all templates extend and therefore are rendered with these features available to users.

### Homepage and Published Scrapbooks
The highest priority section of the homepage, namely the published scrapbooks, needed to be implemented first. Bootstrap cards have been used to ensure that the layout of the cards is responsive to different screen sizes. The same layout is used to list the scrapbooks on My Scrapbooks and Shared Scrapbooks.
![image](https://github.com/user-attachments/assets/a6e0a1ad-fad7-427f-b670-7dabab999909)
![image](https://github.com/user-attachments/assets/8288f09b-0d64-4d11-a770-e19b38da2075)
![image](https://github.com/user-attachments/assets/1ef10163-d7c3-4807-ad5e-52c92cc6ba7e)

Portrait and landscape images uploaded are displayed within the limits set in the custom CSS for the card image in order to achieve a consistent size of cards and a neater layout of scrapbook cards. This is also replicated on My Scrapbook and Shared Scrapbook lists.

#### Hero image
In v1.2, the hero section was added with a call-to-action button, which changes depending on whether the user is logged in. This is mirrored in the hero section on the About page.
![image](https://github.com/user-attachments/assets/49bc984c-4ef5-40a7-bf61-f46bb8fc09af)
![image](https://github.com/user-attachments/assets/8afafe76-4dc2-4b88-8c55-60a9c18ba90c)
The image of a scattered collection of old sepia photos brings to mind nostalgia and happy childhood memories which is aligned with the purpose of this app.

#### Testimonials
In v1.2, Github Copilot generated code for the Bootstrap Carousel, which was adapted to include thumbnail images generated by DALL-E and quotes generated by ghost text.

![image](https://github.com/user-attachments/assets/2e2901ea-c9dc-4957-8994-c95a201cb48a)

This provides user with more information on how other users feel about the product.

### About Page
The About page was created to provide the user a better understanding of the purpose of the site and the benefits it could deliver:
![image](https://github.com/user-attachments/assets/5b901560-fe4a-4559-8415-664da66f8f33)

It also includes an FAQ which could be used to provide more information on data security and how to use the site:
![image](https://github.com/user-attachments/assets/fda83069-3e95-4302-8646-eccf97e781e8)

### Accounts Management
Django AllAuth and Users have been used to implement the registration and authentication of users in the front-end. The default templates for signup, log in and log out extend the base template to keep a consistent look-and-feel. The signup and log in pages use Crispy Forms for the implementation of form fields. Form validation has been implemented in the sign up form for the email field to ensure the user enters a valid email address.
![image](https://github.com/user-attachments/assets/cdde58ca-9f12-484e-9018-f74880116865)
![signup_email_validation](https://github.com/user-attachments/assets/d07d7019-8db6-47fa-842c-b5f014084898)

A Cancel button has been added to allow users to go back to opt out of submitting and return to the previous page.

### Log in Status
The logged in status message and icon in the top right under the navbar tells users whether they are logged in or not.
![image](https://github.com/user-attachments/assets/b956b0ab-b129-43de-82ce-799ec63a48e9)

![image](https://github.com/user-attachments/assets/af166bfe-0684-409f-a949-adf94d4d26e8)

On smaller screens, the message is shortened to fit on screen better:
![image](https://github.com/user-attachments/assets/d4544e39-4150-4ff2-a216-c4391b60232d)

### Publish Status
<details>
    <summary>When creating or editing scrapbooks, users can choose the status of their scrapbook. The same applies when creating/editing posts:
</summary>
    
![image](https://github.com/user-attachments/assets/1550d47d-3f81-4146-a153-438bde61f17b)

</details>

* Draft: Users can save their work in progress and return to finish it another time. Only they can see any draft content.
* Private: This may be content that users don't want to be published. Private scrapbooks can be shared with nominated users.
* Public: Any scrapbooks set to Public status should be listed on the homepage for any users to see without logging in.

The status of each scrapbook is denoted by the Font Awesome icons after the title:

* Draft (icon: fa-solid fa-pen)
* Private (icon: fa-solid fa-lock)
* Public (icon: fa-solid fa-globe)

Draft Scrapbooks and Posts are also displayed as cards with some opacity applied to the card body.
![image](https://github.com/user-attachments/assets/a094f87f-cd0a-4dae-829b-849edb2430c7)

### CRUD Functions

Here is a summary of the CRUD functionalities implemented. 
|     Features          |     Create    |      Read      |     Update     |      Delete     |
| :--------------------- |:-------------:|:---------------:|:---------------:|:---------------:|
| Draft Scrapbook       |Logged-in users|   Author only  |   Author only  |   Author only   |
| Private Scrapbook     |Logged-in users|   Author & Users with Shared Access only  |   Author only  |   Author only   |
| Published Scrapbook   |Logged-in users|   All users    |   Author only  |   Author only   |
| Draft Post            |Logged-in users| Same as its scrapbook |   Author only  |   Author only   |
| Private Post          |Logged-in users| Same as its scrapbook |   Author only  |   Author only   |
| Published Post        |Logged-in users| Same as its scrapbook |   Author only  |   Author only   |

All users, logged-in or not, can read published scrapbooks and posts. All other CRUD functions are all only accessible to logged-in users.

### Access Control
Django Template Language has been used to implement the conditions as detailed in the CRUD table above.

It was also necessary to ensure that users without permissions cannot access the CRUD functions for the scrapbooks and post. A LoginRequiredMixin has been used to control the access to those views.

### Create and Edit Scrapbooks/Posts
The same template is used for the creation and editing of scrapbooks, and the content is updated dynamically using Django Template language.

Crispy Forms is used to implement the form fields, but it was not sufficiently clear whether the right image has been selected.
![image](https://github.com/user-attachments/assets/10a6f668-1cc8-4c85-99ed-b5ba60543b7d)

I wrote an image uploader in Javascript to listen for when images are selected and give the user a preview of the image.

A similar design is used for creating and editing posts.

### Post Detail
[add screenshots, set size for photo but max-width limited on very large screens]

### Delete Scrapbook or Post
The delete page gives the user the name of the item being deleted so that they can confirm or cancel the deletion. 
![image](https://github.com/user-attachments/assets/072c9203-e39d-4cf4-b8ca-fcc3aac6d59f)


### My Scrapbooks
Logged in users can create, edit and delete their own scrapbooks and posts, and there is a link in the navbar directly to My Scrapbooks so users can see all their own scrapbooks. All scrapbook cards on this page allow the user to Open, Edit, Delete and Share their scrapbooks:
![image](https://github.com/user-attachments/assets/21d812ef-a843-4967-bae2-d31435cf82e2)


### Shared Scrapbooks
Logged in users can also see the scrapbooks that have been shared with them, and they can navigate directly to it from the Shared Scrapbooks link in the navbar. In this version, users that have permission to a shared scrapbook also have permission to access the posts in that scrapbook, but only private and public posts. Draft posts can only be accessed by the author of the scrapbook.
![image](https://github.com/user-attachments/assets/e6cc9844-741c-4a49-8b0c-f02960d65c1a)


### Notifications
Users receive notifications when they log in or out and with any CRUD functions. This is implemented in the base template just on top of the navbar, and adapts to the screen size of the user. Javascript has been used to time out and fade out the message after 9s.
![image](https://github.com/user-attachments/assets/a143f052-1054-45d3-8777-6586eafd6b3b)

### Admin Panel
The Admin Panel is set up for the admin or superuser to have access to the data in the database, including the Scrapbook, Post and SharedAccess models and the User model. Additional fields have been added to verify data changes after CRUD functions in the front end.
![image](https://github.com/user-attachments/assets/1d7f1767-c479-468d-a68c-6b83a74d202c)

### Custom Error Pages
Custom error pages have been implemented to handle 403, 403 CSRF, 404 and 500 errors in order to give users a more familiar and tailored message when an error is raised, and also provides them with the option to use the Homepage button provided or the navbar in the base template to go to other parts of the site.
![image](https://github.com/user-attachments/assets/d669401f-9669-4cc5-975b-18e8f57f3af8)

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
Some unclosed empty tags were found on the initial parses of HTML validation during MVP development. These were resolved and subsequently no errors were found in the HTML files from the code I wrote.

The only 4 errors come from HTML in the Sign up pages default when setting up authentication using AllAuth, so should be considered out of scope for this project. Here are the screenshots from running the HTML validation:

<details>
  <summary>HTML validation - Homepage - No errors:</summary>

![image](https://github.com/user-attachments/assets/f48e5248-a2cb-4f13-903a-ee322ef17489)

</details>
<details>
  <summary>HTML validation - About - No errors:</summary>
    
![image](https://github.com/user-attachments/assets/65fb1d91-01c2-4661-b56c-9d4ef697b8ec)

</details>
<details>
  <summary>HTML validation - My Scrapbooks - No errors </summary>
  
![image](https://github.com/user-attachments/assets/40ba7ec7-84a4-4372-ab70-aaa823353d9e)

</details>
<details>
  <summary>HTML validation - My Scrapbook Detail - No errors </summary>
  
![scrapbook_detail_validation](https://github.com/user-attachments/assets/95703b94-ee3f-4a0e-a61b-ce28f9b62994)


</details>
<details>
  <summary>HTML validation - Shared Scrapbooks - No errors </summary>
  
![image](https://github.com/user-attachments/assets/0525fe01-2e6b-4676-a30c-4e506d748a11)


</details>
<details>
  <summary>HTML validation - Shared Scrapbook Detail - No errors </summary>
  
![image](https://github.com/user-attachments/assets/d8c8c7a6-8e69-4e2b-acdf-9dfc960696f4)

</details>
<details>
  <summary>HTML validation - Post Detail - No errors :</summary>
    
![image](https://github.com/user-attachments/assets/243b2a2f-cb94-4350-8216-4d3bcc2b4ca1)

</details>
<details>
  <summary>HTML validation - Create/Edit Scrapbook - No errors </summary>
  
![image](https://github.com/user-attachments/assets/111d6569-dfa2-44af-a2a0-492eb71af002)


</details>
<details>
  <summary>HTML validation - Delete Scrapbook/Post - No errors </summary>
  
![image](https://github.com/user-attachments/assets/7aa4a994-4047-44c0-bd6b-cdc6a9ed4eae)

</details>
<details>
  <summary>HTML validation - Sign Up - 4 errors </summary>

![image](https://github.com/user-attachments/assets/4de62907-4ea3-4daa-8be3-351c6f4ad772)

The 4 errors in the signup page relate to the span tag around the unordered list tag for the help instructions for making a valid password for signing up. This is set up by default in AllAuth and inserted using the standard {{ form.as_p }} using Crispy Forms, and therefore cannot be edited in my code.
  
![image](https://github.com/user-attachments/assets/1d29d557-dda1-49b1-88d7-9c5147bc808f)


</details>
<details>
  <summary>HTML validation - Log In - No errors </summary>
  
![image](https://github.com/user-attachments/assets/6e6da528-1f0c-4ff6-b72e-1b0f8ecb0e5b)

</details>
<details>
  <summary>HTML validation - Log Out - No errors </summary>
  
![image](https://github.com/user-attachments/assets/06759461-a628-4b83-b4c4-86aea1d0b7ed)


</details>
<details>
  <summary>HTML validation - Custom Error Pages e.g. 404 error page: - No errors </summary>
  
![image](https://github.com/user-attachments/assets/00320c6d-f070-45b8-978e-a897cb3a68f4)

</details>

#### CSS Validation
No errors were found in the CSS file.
<details>
  <summary>CSS validation screenshot - No errors:</summary>
    
  ![image](https://github.com/user-attachments/assets/4a079e15-bc09-4854-8dbe-76263af8790a)

</details>

### JSHint Linter

- Used [JS Hint](https://jshint.com/) to test Javascript for ES version 6 and got no warnings. Results are included below:<br>
script.js
<details>
  <summary>messages.js:</summary>
    
  ![JSHint_messages](https://github.com/user-attachments/assets/6a318515-e340-4d42-826a-3e5d3d26fd0a)

</details>

<details>
<summary>thumbnail-image.js:</summary>
    
  ![JSHint_thumbnail-image](https://github.com/user-attachments/assets/ed7bfe5a-3bec-468e-be28-fb19057eb863)
</details>

#### Python Linter
- Used [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to check all Python code I have written meets the PEP8 standard and got no warnings. Results from linting one of the files (test_models.py) has been included below:<br>

<details>
  <summary>test_models.py:</summary>
    
  ![python_linter_example_test-models](https://github.com/user-attachments/assets/47a4c704-a8a4-4d10-8983-3498ca15d851)

</details>


#### Lighthouse Audit
Chrome Dev Tools Lighthouse was used to audit the site for response time and accessibility. Testing was done during MVP development after deploying v1 Homepage with only the cards of published scrapbooks, allowing more time for bug fixes.<br>

Colour constrast issues:
* Colour contrast issues in navbar as mentioned above in [Colour Scheme](#colour-scheme) [resolved]
* Colour constrast issues in card text and subtitle [resolved]
* Cloudinary not using https [resolved]

Screenshots of Lighthouse Audit on the Homepage after fixes:

Mobile:
![image](https://github.com/user-attachments/assets/f25b0992-9387-450d-8cf0-0892db24e85c)

Desktop:
![image](https://github.com/user-attachments/assets/c63df866-6159-4a8f-bc22-d0437f1bd56a)

Pages without Cloudinary content were scored much better on the Chrome version of Lighthouse:
![image](https://github.com/user-attachments/assets/e708b291-5102-40e4-82ee-231fb1eb7af0)

Lighthouse Audits run on MS Edge achieved better scores as the Cloudinary cookies were not considered an issue:

![lighthouse_home_edge](https://github.com/user-attachments/assets/461bc5d0-8fa0-44ce-afa7-bcc9e00341c3)
![lighthouse_post_detail_edge](https://github.com/user-attachments/assets/42904d31-3cac-4434-9668-d2c13b7eb013)

#### WAVE Accessibility Evaluation
The WAVE tool was used to test for accessibility and usability. No errors were raised. The alert was on visible and hidden buttons adjacent to each other having similar functions, but these are used to tailor the user experience for different users.

![image](https://github.com/user-attachments/assets/2428093d-6a09-42c2-8457-7eda9be3db77)


#### Outstanding issues
* Third-party cookies from Cloudinary: Chrome has recently deprecated its support for third-party cookies and gives a warning in Chrome Dev Tools. Cloudinary has yet to give a [response](https://community.cloudinary.com/discussion/596/third-party-cookies-will-be-blocked-how-to-solve-it) on how this can be resolved.

<p align="right"><a href="#top">Back to top</a></p>

## Testing Summary

#### Browser and Device Testing
The site was tested on my laptop (Surface Pro  7) across the 3 popular browsers. The test is passed if the expected result is produced:

|     Features          |     Test and Expected Result    |      Chrome      |     Firefox     |      MS Edge     |
| :--------------------- |:-------------:|:---------------:|:---------------:|:---------------:|
| Responsive Design: the site is rendered correctly for mobile, ipad and laptop screens	| change screen size in Devtools |	Pass |	Pass |	Pass
| CSS Rendering: styles and animations are rendered correctly| navbar colours and hover, card hover animation and posts expand/collapse|	Pass	|Pass	|Pass |
| Grid and Flexbox Layouts: card layout adapts to screen size | cards change layout in DevTools | Pass | Pass | Pass |
| JavaScript Behavior: message alert timeout and image thumnbnail preview |	message disappears after 9s and preview updates when new image chosen |	Pass |	Pass| Pass|
| JavaScript Errors: check Devtools console for errors|	no errors while tested above JS functions |	Pass| Pass|Pass|
| Form Validation: prompts user for correct type|	Sign up: alert when submit text with no @ in email field|Pass|Pass|Pass|
| Loading Times: tested in Lighthouse Audit under Performance|	homepage loading, score > 70	| Pass|Pass|Pass|
| Keyboard Navigation: users can interact with UI using only keyboard|	Scrapbook Detail: users can <tab> through navbar and collapsed cards and <Enter> to open a post|	Pass|	Pass|	Pass|
| Error Pages: custom error pages are displayed|	use URL to access post after deleted, should get custom error page|	Pass|	Pass|	Pass|

The same tests (except for varying screen size and keyboard navigation) were also run in Chrome on an iPhone SE and passed.
In future, more testing will need to be done on other devices and on Safari.

### Automated Testing
Automated Tests were set up in Django test_ files to test the implementation of models, views, forms and templates in the project. These all use Django TestCase and focus on unit tests and edge tests. Tests were developed towards the end of MVP implementation to verify models, views and forms have been built as intended. As features are added the automated tests are run before code is committed. 

Also see the [AI Reflection on Automated Unit Testing](automated-unit-testing) below on how tests were written with the help of Github Copilot.

#### Bugs to be Fixed
* Third-party cookies from Cloudinary: as mentioned in Chrome Lighthouse Audit
* The Back buttons on each page needs to be more thought through and tested to make sense in each user flow, as it does not make sense to e.g. take a user back to the Delete page after they have deleted a post or scrapbook.
* The validation error in the Sign Up page is dependent on code provided by a third party. The page is currently functional but 

#### Models: test_models.py:

##### Scrapbook Model
<details>
    <summary>Unit tests (8 tests, passed)</summary>
    
Unit tests on creating instances of Scrapbook, relationships, slug generation uniqueness, ordering and blank fields
    
![image](https://github.com/user-attachments/assets/350e714e-2b33-4ab3-aead-ad9436c955dc)
</details>

<details>
    <summary>Edge tests (16 tests, passed)</summary>
    
Edge tests on max and exceeding lengths, trailing spaces, image file formats and special characters 

![image](https://github.com/user-attachments/assets/7ecd8092-3e29-428c-ad50-f9be46c41c2d)

</details>

##### Post Model

<details>
    <summary>Unit tests (9 tests, passed)</summary>
    
Unit tests on creating instances of Posts, relationships, slug generation uniqueness, ordering, default values and blank fields
    
![image](https://github.com/user-attachments/assets/3ae01201-c76c-46c2-9cbf-e04f7ce0ffb1)

</details>

<details>
    <summary>Edge tests (13 tests, passed)</summary>
    
Edge tests on max and exceeding lengths, trailing spaces, image file formats and special characters 

![image](https://github.com/user-attachments/assets/97df4741-56fc-41c8-87eb-55317596e700)


</details>

##### SharedAccess Model

<details>
    <summary>Unit tests (6 tests, passed)</summary>
    
Unit tests on creating instances on SharedAccess using test instances of Scrapbook, Post and Users

![image](https://github.com/user-attachments/assets/e2933049-0a6b-491d-8f20-092d208b4f74)

</details>

<details>
    <summary>Edge tests (2 tests, passed)</summary>
    
Edge tests on missing user data and missing shared by field when creating instances of SharedAccess 

![image](https://github.com/user-attachments/assets/cc81c1d2-6798-490c-82d6-8dd42b9b06cf)

</details>

#### Views: test_views.py

##### Scrapbook Views

<details>
    <summary>Unit tests (5 tests, passed)</summary>
    
Unit tests on Scrapbook List View, Detail View, Create View, Update View and Delete View
    
![image](https://github.com/user-attachments/assets/7c415079-ba67-43ee-8136-100f7bbeeada)

</details>

<details>
    <summary>Edge tests (2 tests, passed)</summary>
Edge tests on creating scrapbook views with long titles and invalid image format 

![image](https://github.com/user-attachments/assets/705e7d6a-c006-4e67-bf1b-f8ed6bb861d5)

</details>

##### Post Views

<details>
    <summary>Unit tests (4 tests, passed)</summary>
Unit tests on Post Detail View, Create View, Update View and Delete View
    
![image](https://github.com/user-attachments/assets/1b35328f-bc51-4c46-ada7-e5881b2f6e7c)


</details>

<details>
    <summary>Edge tests (2 tests, passed)</summary>
Edge tests on updating post with special characters and deleting non-existent posts 

![image](https://github.com/user-attachments/assets/0f67ce1c-2958-4ac9-912f-6d748eefd5da)

</details>

##### Access Control and SharedAccess Views

<details>
    <summary>Permissions for Access (2 tests, passed)</summary>
Tests whether users without permissions can access private scrapbooks, and whether a user can access a scrapbook shared with them
    
![image](https://github.com/user-attachments/assets/c3ec8c4a-a920-431e-8f97-9f0f6115ecb5)

</details>

<details>
    <summary>SharedAccess Views (7 tests, passed)</summary>
Unit tests on SharedAccess and whether shared scrapbooks are segmented from the user's own scrapbooks.

![image](https://github.com/user-attachments/assets/2f509c3c-1b8a-403b-b9ec-262c67a98ab9)

</details>

#### Forms: test_forms.py

##### Scrapbook Forms

<details>
    <summary>Unit Tests (4 tests, passed)</summary>
Tests the form with valid and invalid data, and missing title and image fields
    
![image](https://github.com/user-attachments/assets/d38376c8-3626-4805-a0ec-27a51e0be621)

</details>

<details>
    <summary>Edge Tests (5 tests, passed)</summary>
Tests the form title field with special characters, maximum and exceeding title lengths. Tests image uploading with invalid file formats and large image files.
    
![image](https://github.com/user-attachments/assets/a709e370-a6bb-480e-9d4c-d2d7d46674bf)

</details>

##### Post Forms

<details>
    <summary>Unit Tests (4 tests, passed)</summary>
Tests the form with valid and invalid data, and missing title and image fields
    
![image](https://github.com/user-attachments/assets/b8c1929f-9039-463d-876b-c5d2c6dc6bc7)

</details>

<details>
    <summary>Edge Tests (5 tests, passed)</summary>
Tests the form title field with special characters, maximum and exceeding title lengths. Tests image uploading with invalid file formats and large image files.
    
![image](https://github.com/user-attachments/assets/78c52b29-c29c-4262-9522-882ab4f8698a)

</details>

##### SharedAccess Forms

<details>
    <summary>Unit Tests (4 tests, passed)</summary>
Tests the form with valid and invalid data, and missing user and existing shared access
    
![image](https://github.com/user-attachments/assets/383a551a-e55c-4d83-9e2b-96b74e7c14ee)


</details>

#### About: test_about.py
<details>
    <summary>Unit Tests (4 tests, passed)</summary>
Tests that the About page loads and contains the right content for authenticated and unauthenticated users
    
![image](https://github.com/user-attachments/assets/798745e6-87fb-44f8-a822-9fe8df9c010e)



</details>

#### Error Handling: test_error_handling.py
<details>
    <summary>Unit Tests (4 tests, passed)</summary>

![image](https://github.com/user-attachments/assets/40a0f22c-a7f9-4046-bcdb-8c473c6cedaa)

</details>

### Manual Testing
With the completion of every feature, the site is manually tested in addition to the automated tests to ensure that existing functionalities are still in place and not impacted by the latest changes in the code. Any bugs could then be prioritised in the project board and scheduled for fixing.

Towards the end of the project, the final system that has been unit tested was also tested as a whole for integration testing. The table below shows the scope of the functions tested and the results from manual testing:

![image](https://github.com/user-attachments/assets/c317e1cc-3abf-4d25-85b5-279e6ad0bb53)

In addition to that, all pages were tested for broken links and interactive effects on the deloyed site to ensure all parts of the site are rendering as intended on the deployment site before final delivery.

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
![Static Badge](https://img.shields.io/badge/HTML5-language-red)
![Static Badge](https://img.shields.io/badge/CSS3-language-%23663399)
![Static Badge](https://img.shields.io/badge/Javascript-language-yellow)
![Static Badge](https://img.shields.io/badge/Python-language-blue)

![Static Badge](https://img.shields.io/badge/Heroku-deployment-%2379589f)
![Static Badge](https://img.shields.io/badge/GitHub-repo_hosting-black)
![Static Badge](https://img.shields.io/badge/Cloudinary-image_hosting-black)
![Static Badge](https://img.shields.io/badge/Gitpod-IDE-yellow)
![Static Badge](https://img.shields.io/badge/VS_Code-IDE-yellow)

![Static Badge](https://img.shields.io/badge/PostgreSQL-DBMS-blue)

### Libraries and Frameworks
![Static Badge](https://img.shields.io/badge/Bootstrap-frontend_dev_framework-purple)
![Static Badge](https://img.shields.io/badge/FontAwesome-icon_library-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-typography_library-blue)

![Static Badge](https://img.shields.io/badge/Django-web_framework-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_AllAuth-authentication_package-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_Whitenoise-static_file_serving_package-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_CrispyForms-layouts_package-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_CrispyBootstrap-layouts_package-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_Summernote-rich_text_editor_package-%2311593e)
![Static Badge](https://img.shields.io/badge/Django_Pillow-imaging_library_for_image_testing-%2311593e)

All Django packages installed are listed in [requirements.txt](https://github.com/tgrey2024/capstone/blob/main/requirements.txt).

### Tools and Programs
![Static Badge](https://img.shields.io/badge/LogoAI-logo_generator-red)
![Static Badge](https://img.shields.io/badge/Favicon.io-icons-red)
![Static Badge](https://img.shields.io/badge/Coolers-colour_palette_testing-red)
![Static Badge](https://img.shields.io/badge/WCAG-colour_contrast_testing-red)

![Static Badge](https://img.shields.io/badge/Balsamiq-wireframes-brown)
![Static Badge](https://img.shields.io/badge/Canva-mockups-brown)
![Static Badge](https://img.shields.io/badge/Lucidchart-diagramming-brown)

![Static Badge](https://img.shields.io/badge/MSCopilot-AI-orange)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI_pair_programming-orange)
![Static Badge](https://img.shields.io/badge/Perplexity_AI-DB_Design-orange)
![Static Badge](https://img.shields.io/badge/Eraser_DiagramGPT-AI_generated_ERDs-orange)

<p align="right"><a href="#top">Back to top</a></p>

## AI Implementation and Orchestration
### Planning

During brainstorming, [MS Copilot](https://copilot.microsoft.com/) suggested 40+ ideas for a Django web-app that a beginner developer could build alone in two weeks. Having chosen the project and defined the project goals and scope, I prompted Copilot to suggest a list of user stories. These were reviewed and edited to meet the project goals. Then Copilot identified some relevant acceptance criteria and tasks for each one, which provided the basis for planning each user story.

Using the user stories, [Perplexity AI](https://www.perplexity.ai/) gave me a schema of the entities, fields and relationships. Having made some adjustments, I put this schema into [Eraser DiagramGPT](https://www.eraser.io/diagramgpt) which then provided me with an initial ERD for my initial database design, which later evolved into the [final database ERD](#database).

The [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) extension was installed in my local version of Visual Studio Code. In the planning stages, Copilot was prompted to suggest implementation ideas, e.g. when I was researching options for sharing content between users privately. Copilot was asked for options suitable for a junior developer to implement, and it provided two options including pros and cons, and suggested reading on the subject.

### Code Generation

Using the Github Copilot extension, I was able to write prompts or highlight functions in pseudocode and ask Copilot to suggest code snippets. Suggestions needed to be reviewed before they were included, as code may refer to e.g. variables that have not been declared or not yet been imported.

GitHub Copilot helped to generate model fields and CRUD views, which were adjusted to fit the project requirements. It also helped to speed up the building of Bootstrap components like the navbar, grid, cards and testimonials, which were then adjusted and tested for functionality, usability and responsiveness. Copilot suggested CSS and Bootstrap enhancements to the cards, but these did not work, so they were adjusted after I found code references on the required effects.

When I come across suggested code that I don't understand, I used the inline editor to ask for an explanation of the selected code with a breakdown of each step and a concise summary. With larger sections of code suggestions, the chat provided more space for me to question specific parts of functions so Copilot could adjust the recommendations to accommodate my specific requirements. 

Reverse prompting was used when asking for recommendations to be refined, e.g. when Copilot asked me a series of questions about uploading images, whether I wanted to upload multiple images per post, etc. Once an approach was agreed, Copilot was prompted to provide a checklist of steps and walked through the process incrementally.

Occasionally Copilot suggested code in ghost text unnecessarily, introduced extraneous closing tags in its code suggestions, or even removing code it thinks is unnecessary. It is important to keep a close eye on what is changed, but on the whole using AI as a pair programmer has allowed me to write code faster and learn more efficiently.

### Content Creation

MS Copilot provided textual content for scrapbooks and posts based on a selection of themes that were commonly used in reminiscence therapy. It also provided content for the About page, which only required minor adjustments.

DALL-E helped generate images for the About page, but only some of the images were useful due to biases, misinterpretation of prompts or incorrect limbs, so I only used a small selection of the AI-generated images that were appropriate.

Github Copilot suggested the testimonials in ghost text while suggesting code for building the Bootstrap carousel.

### Debugging

Copilot was regularly used for debugging code, either by highlighting specific code in the inline editor, or using @workspace if Copilot needs more context. Copilot suggested debugging code to help identify issues in the code, which helped to resolve issues much faster. Copilot also proposed ways to fix errors. These did not always work, and when questioned about any inconsistencies, the revised solution was much more suitable. This paired programming approach was generally faster and more effective than searching through documentation alone to find potential fixes.

When using Chrome DevTools to inspect the preview or deployed pages, Chrome DevTools AI Assistance panel was also used to explain the errors raised in the Console.

### Performance and UX Optimisation

While learning to write class-based views, apart from reading Django references and documentation, I also prompted Copilot to debug the class-based views that were written. Once tested to run correctly, Copilot was prompted to optimise the code. It was important to keep a version of the original code commented out while testing that the optimised code produced the same result before incorporating it into the code. 

### Automated Unit Testing

Automated tests were written by prompting Copilot for test skeletons for unit tests without implementation. Copilot also suggested edge test cases that were beyond what I could have considered on my own.

Having chosen the relevant test cases to include, I used Copilot to suggest ghost text to implement each one. Each test case was reviewed and tested separately, and Copilot also helped with suggesting necessary fixes resolve any failures, although it was also important to test that the changes have not broken any functions in the affected part of the app.

### Impact on Workflow

On the whole, it has been useful to pair program with Copilot and use it for suggest and explain code while learning as a junior developer. Due to the tight timescale of the project, I used AI where possible to streamline development, from brainstorming solutions to suggesting commit messages. 

### Use Cases and Reflections
[Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.]

<p align="right"><a href="#top">Back to top</a></p>



## Credits
### Code References

[Classy Class-Based Views](https://ccbv.co.uk/) - references to Django class-based views with examples and links to Django documentation

Override Bootstrap styles in navbar links - [CodePen](https://codepen.io/skde/pen/ExyrBYg)

Collapsible Bootstrap cards: [Examples](https://preview.keenthemes.com/html/metronic/docs/base/cards#collapsible%20)

[Card Collapse Tricks](https://disjfa.github.io/bootstrap-tricks/card-collapse-tricks/)

Animate Bootstrap Cards using CSS: [YouTube video](https://www.youtube.com/watch?v=WihYWBf9FmI)

[UNRESOLVED] Deprecation of Chrome support of third-party cookies: [Cloudinary response](https://community.cloudinary.com/discussion/596/third-party-cookies-will-be-blocked-how-to-solve-it)

[Mark Down guide](https://www.markdownguide.org/)

[Static.io](https://shields.io/badges) for making static badges

### Content References

MS Copilot was used to generate much of the homepage, about page and blog content.

### Image References

* Pexels - [https://www.pexels.com/](https://www.pexels.com/)
* DALL-E - AI-generated images

#### Acknowledgements

Many heartfelt thanks to:
* everyone in my WECA group who has been so helpful and supportive leading up to and throughout this project,
* Code Institute tutors (Dillon, Mark and Roo) for your patience and answering my endless questions,
* my patient in-house testers (aka my family) for giving me feedback on requirements, colour choice, usabilty, etc. throughout development,
* and my parents who gave me the inspiration for this project (much better than the 40+ AI-generated ideas), and spent hours reminiscing over photos of old Hong Kong, family and friends, 60s icons, comfort food...just to test the product.

<p align="right"><a href="#top">Back to top</a></p>
