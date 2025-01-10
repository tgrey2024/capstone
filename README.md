# AI Augmented FullStack Bootcamp - Individual Capstone Project <a id="top"/>
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
    - [Imagery](#imagery)
- [Key Features](#key-features)
    - [Nav Bar](#nav-bar)
    - [Footer](#footer)
- [Responsive Design](#responsive-design)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
    - [Platform](#platform)
    - [High Level Deployment Steps](#high-level-deployment-steps)
    - [Verification and Validation](#verification-and-validation)
    - [Security Measures](#security-measures)
- [Testing](#testing)
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
- **Link to User Stories in GitHub Projects:**
  - [Add a link to the GitHub Projects kanban board.]
<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Design
### Wireframes
  - [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
<details>
  <summary>More wireframes</summary>
  <b>Add other wireframes</b>
</details>

  - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
### Mockup
  - [Canva Mockup](https://www.canva.com/design/DAGbzmo_8Iw/GjNxoK5LvaTmJT1r-8IEiQ/view?utm_content=DAGbzmo_8Iw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hf37b8eca3e)
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]
<p align="right"><a href="#top">Back to top</a></p>

## Key Features
- **Feature 1:** [Briefly describe the implemented feature.]
- **Feature 2:** [Briefly describe the implemented feature.]
- **Inclusivity Notes:** 
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

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.
<p align="right"><a href="#top">Back to top</a></p>

## Testing Summary

- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing:**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]
<p align="right"><a href="#top">Back to top</a></p>

## Future Enhancements
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.
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

### Libraries
![Static Badge](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Static Badge](https://img.shields.io/badge/FontAwesome-icons-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-Typography-blue)
### Tools and Programs
![Static Badge](https://img.shields.io/badge/LogoAI-LogoGenerator-red)
![Static Badge](https://img.shields.io/badge/Favicon.io-icons-navy)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/MSCopilot-AI-orange)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI-orange)
Perplexity AI
DiagramGPT/Eraser

<p align="right"><a href="#top">Back to top</a></p>

## Credits
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
