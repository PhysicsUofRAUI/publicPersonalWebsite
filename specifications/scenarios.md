# Purpose
This file will detail a few theoretical scenarios to flesh out the website better

## Scenario One: View Project Posts
1. On the home page
2. Click on the Projects link
3. Will navigate to the project view
  - in background the recent posts will be retrieved
  - subcategories for posts will also be retrieved
4. The page will be displayed with the subcategories in one column and the posts in another column
5. It would be preferable for posts to be initially listed as previews but that can be left as future work

## Scenario Two: View Travel
1. On the home page
2. Click on the Travel link
3. Will navigate to the travel view
  - in background the recent posts will be retrieved
  - subcategories for posts will also be retrieved
4. The page will be displayed with the subcategories in one column and the posts in another column
5. Again preferable to have previews of posts

## Scenario Three: View Resume
1. On the home page
2. Click on Resume link
3. Go to the resume view
  - view will just have to load up the html since it will all be static
4. The html will be displayed
  - the downloads will be in the form of pdf links

## Scenario Four: View Gallery
1. On the home page
2. Click on Gallery link
3. System goes to the gallery view
  - the categories for photos will be pulled up
  - some photos with accompanying captions will be retrieved
4. One column will display the photos with the captions
5. A second column will show the categories.

## Scenario Five: Go To Home page From some other Page
1. On some other page
2. Click Home page link
3. System goes to the home page view
  - A selection of photos will be retrieved
  - rest will just be html
4. The photo roll will be at the top of the page
5. In the middle a hardcoded description of myself will exist
6. at the bottom a embeded twitter and facebook

## Scenario Six: Adding A Blog Post
1. See Scenario Nine
7. Click the 'add post' link
8. System will navigate to the 'add post' view
9. The 'add post' page will be rendered
10. User enters the category, subcategory, the title, and content
  - category is Travel or Blog Post
  - subcategory is classifiers for the separte blog posts (Morocco, Brazil for travel, and Blockchain, physics for the regular blog)
11. User submits the post
  - if successful move to step 12
  - if unsuccessful go to step 9 with unsuccessful post flag
12. The system will render the blog post in regular format
  - it will go through either the Travel view, or Blog view
  - this process still needs to be defined

## Scenario Seven: Adding A Photo
1. See Scenario Nine
7. Click the 'add photo' link
8. System will navigate to the 'add photo' view
9. The 'add photo' page will be rendered
10. User enters the filename (could do an upload something), the category, and the caption
  - flask does have uploading included but how about we leave that till later for now
11. User hits the submit button
  - if successful move to step 12
  - if unsuccessful go to step 9 with unsuccessful post flag
12. Go to the photo view
  - have the category of the photo shown.

## Scenario Eight: Attempting To Add Post without logging in
1. On home page.
2. Attacker manually types in link to Add/Edit/Delete view
3. The view checks if the user is authorized (logged in)
4. In this case the user is not
5. The view redirects to the home page

## Scenario Nine: Login
1. On the home page
2. Manually Type in address for the login page
  - will keep the login page 'hidden'
3. System will go to login View
4. type in the login credentials
5. The system will check the credentials
  - if login credentials are wrong go back to 3 with 'login failed' flag
  - if they are correct move to step 6
6. Go to home page
  - nav bar will have 'logout', 'add post', and 'add photo' fields

## Scenario Ten: Logout
1. On home page
2. Click the logout link
3. The logout view will be called
4. In that view the system will remove the cookie created to signify a login
5. A page will be displayed sayin logout has be successful

## Scenario Eleven: Choosing Specific Category Photos
1. On the main photo page
2. User clicks a specific category on the right hand side of the screen
3. The page gets reloaded with the flag of that specific category
  - in future verions an ajax call could be used
4. Only photos from the selected category are displayed.

## Scenario Twelve: Choosing Specific Category for travel
1. On the main travel page
2. User clicks a specific category on the right hand side of the screen
3. The page gets reloaded with the flag of that specific category
  - in future verions an ajax call could be used
4. Only travel posts from the selected category are displayed.

## Scenario Thirteen: Choosing Specific Category for Projects
1. On the main Projects page
2. User clicks a specific category on the right hand side of the screen
3. The page gets reloaded with the flag of that specific category
  - in future verions an ajax call could be used
4. Only project posts from the selected category are displayed.

## Scenario Fourteen: Downloading Resume or Cover Letter
1. On the Resume page
2. User clicks on either a resume or cover letter link
3. That link goes to the resume/cover letter as a pdf
4. The user then uses the web browser to download the file

## Scenario Fifteen: Edit a travel blog post
1. login via scenario nine
2. Go to Travel page
3. Click a specific post
  - the system will reload the page with that specific post specified as the post to present
4. The user clicks the edit button
5. The 'edit a post' view opens up with that post given as input
6. The screen to edit a post is brought up
  - the given's post current content is shown
7. The user makes the edits desired to the content
8. The user then clicks submit
9. The database is updated and the user is directed to the updated post.

## Scenario Fifteen: Edit a Projects blog post
1. login via scenario nine
2. Go to Projects page
3. Click a specific post
  - the system will reload the page with that specific post specified as the post to present
4. The user clicks the edit button
5. The 'edit a post' view opens up with that post given as input
6. The screen to edit a post is brought up
  - the given's post current content is shown
7. The user makes the edits desired to the content
8. The user then clicks submit
9. The database is updated and the user is directed to the updated post.

## Scenario Sixteen: Edit a Photo
1. login via scenario nine
2. Go to Gallery page
3. Click a specific photo
  - the system will reload the page with that specific photo specified as the photo to present
4. The user clicks the edit button
5. The 'edit a photo' view opens up with that photo given as input
6. The screen to edit a photo is brought up
  - the given photo's current content is shown
7. The user makes the edits desired to the content
8. The user then clicks submit
9. The database is updated and the user is directed to the updated photo.

## Scenario Seventeen: Delete a Photo
1. login via scenario nine
2. Go to Gallery page
3. Click a specific photo
  - the system will reload the page with that specific photo specified as the photo to present
4. The user clicks the delete button
5. The delete a photo view is brought up and that photo is promptly deleted in that view
6. The user is then directed back to the main photo page.

## Scenario eightteen: Delete a Travel Post
1. login via scenario nine
2. Go to Travel page
3. Click a specific post
  - the system will reload the page with that specific post specified as the post to present
4. The user clicks the delete button
5. The delete a post view is brought up and that post is promptly deleted in that view
6. The user is then directed back to the main travel page.

## Scenario eightteen: Delete a Projects Post
1. login via scenario nine
2. Go to Projects page
3. Click a specific post
  - the system will reload the page with that specific post specified as the post to present
4. The user clicks the delete button
5. The delete a post view is brought up and that post is promptly deleted in that view
6. The user is then directed back to the main Projects page.













:smile:
