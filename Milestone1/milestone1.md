<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2023 9:37:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.20.31image.png.webp?alt=media&token=53eb16c5-65e3-4c74-8764-fbd4005d0bdd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password/ username<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.23.07image.png.webp?alt=media&token=92b706c0-f0a6-429e-85f1-b3f9d188afe8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password too short<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.26.42image.png.webp?alt=media&token=1eb2fdcd-a88c-46e6-898f-556a433256c2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.27.30image.png.webp?alt=media&token=aec154d0-fda2-4797-91c0-8a7a267104f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.29.12image.png.webp?alt=media&token=26acc074-3387-4c0a-9a2c-bf31242b63d4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.54.52image.png.webp?alt=media&token=59ca3dc3-f5e9-431d-8ec8-3ab184810d93"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid user data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1. The /register route manages registration, validating and hashing user data before inserting<br>it into the database. Errors trigger the check_duplicate function to handle duplicates.</div><div><br></div><div>2. Frontend<br>validation with WTForms ensures proper form data on the client side. Backend validation,<br>including custom username checks, is done in RegisterForm, invoking check_duplicate for errors.</div><div><br></div><div>3. User<br>passwords are securely hashed with Flask-Bcrypt during registration, enhancing security by avoiding plain<br>text storage.</div><div><br></div><div>4. Database interactions use the DB class, executing SQL queries to insert<br>user data. Exceptions, like duplicate entries, are managed by check_duplicate for user-friendly feedback.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.58.45image.png.webp?alt=media&token=b66121be-4ce1-40c6-aa64-890914e2b430"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T00.59.42image.png.webp?alt=media&token=049b32a7-7f24-487f-a9de-006476057109"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.00.19image.png.webp?alt=media&token=d154619a-6d74-4935-b34c-2bc431cf8be7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1. The /login route handles the login process, where the server validates the<br>LoginForm data. Upon validation, it queries the database for user authentication using email/username<br>and password. Successful login results in user authentication and retrieval of roles from<br>the database.</div><div><br></div><div>2. Frontend validation with WTForms ensures required fields are filled. Backend validation<br>in LoginForm checks email/username format and performs database queries for authentication, displaying flash<br>messages for issues.</div><div><br></div><div>3. During login, Flask-Bcrypt compares the provided password with the hashed<br>database password for authentication.</div><div><br></div><div>4. The DB class interacts with the database, executing an<br>SQL query to retrieve user information based on email/username. Successful login with verified<br>password uses Flask-Login, fetching roles from the database. Flash messages handle errors for<br>user feedback.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.05.00image.png.webp?alt=media&token=b2b7d7c3-c201-4d55-8300-c3faac5ae1d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logout successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.06.45image.png.webp?alt=media&token=e4f0655d-c98d-42bb-a819-66fffb7964da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In the Flask web app provided, session logic securely stores user info post-login.<br>User objects serialize to JSON and store in the session, enabling identity persistence<br>for authentication and personalized content. Logout removes keys like &#39;identity.name.&#39; If an unidentified<br>user tries accessing a protected page, redirection to a 401 HTML page occurs.&lt;img<br>src=&quot;&quot; alt=&quot;&quot;&gt;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.10.33image.png.webp?alt=media&token=a5e6c302-f7ea-4487-b71e-84785956354d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.20.51image.png.webp?alt=media&token=577f1b78-9830-40d0-8533-6f0651786ded"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.29.51image.png.webp?alt=media&token=adef4bb3-b2e4-4c57-9fff-8b0a855e826d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin and editor<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.29.15image.png.webp?alt=media&token=ea78f954-9158-4ccc-af69-a68100d23ae3"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles, with admin having user_id 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Flask-Login extension verifies user authentication for protected pages by checking the session. If<br>not authenticated, users are redirected to the login page. The session, handled by<br>Flask-Login, stores user info for state maintenance and authentication status checks. Helper functions<br>like login_user and current_user simplify login and user information retrieval in protected routes.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>In this role-protected application, verifying access involves checking user roles in the session<br>against required roles using Flask-Principal for role-based access control. User roles are obtained<br>from the database upon login and stored in the session. @roles_required decorator on<br>routes ensures access is restricted to users with specified roles. Flask-Login and Flask-Principal<br>manage the session for persisting user data and determining access permissions.<img src="" alt=""><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.42.23image.png.webp?alt=media&token=1a680072-6a37-4cba-b6a0-a347ad3be01d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tabular presentation of data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T01.58.58image.png.webp?alt=media&token=237378f4-e6ed-4cf6-84d8-fda7e2f1b3c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation and forms<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>The CSS styling in the code predominantly uses Bootstrap, as seen in the<br>integration of Bootstrap&#39;s CSS and JavaScript. The application exhibits a clean, responsive design<br>with Bootstrap&#39;s grid system for layout. Navbar elements, forms, and tables follow Bootstrap<br>styling, and flash messages provide user feedback. The footer is a sticky footer<br>with a light background. External files may contain specific styling details, allowing flexibility<br>for additional or custom styling beyond Bootstrap&#39;s default styles.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.02.31image.png.webp?alt=media&token=d6ccac2d-ba38-45e2-a4e6-f45971e4df86"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid username and password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.03.32image.png.webp?alt=media&token=f0c1cafe-4e17-4768-9569-8ca615fcb837"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>I&#39;ve added custom error pages for technical issues and integrated Flask&#39;s flash messages<br>for quick user-friendly notifications, enhancing the overall user experience.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.05.34image.png.webp?alt=media&token=1e31a3f1-0ed8-4f56-abcb-7c0de9e6a814"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prefilled user profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The /profile view in Flask first checks if the user is logged in,<br>redirecting to the login page if not. For logged-in users, it processes ProfileForm<br>data to update the password and profile in the database. The view refreshes<br>the session with the latest user data and renders the profile.html template. The<br>code ensures that only authenticated users can access and modify their profile, boosting<br>security and user-specific interactions.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.12.46image.png.webp?alt=media&token=98a21000-d267-4c38-bebb-285c67d746b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid user and password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.17.36image.png.webp?alt=media&token=a5a17a09-3f52-488f-94ce-d7beb899f6da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.20.00image.png.webp?alt=media&token=5909c27b-a2e7-46e5-b144-58b177523e9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.23.26image.png.webp?alt=media&token=8d8014bd-d9b0-4e61-83a2-c20995a04daa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.25.21image.png.webp?alt=media&token=1929316f-3c71-4e6e-b405-0ec92086d449"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-12T02.27.26image.png.webp?alt=media&token=f2fa80d3-2aa1-4c77-b810-eb59d7b89256"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing rose to rose2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/26">https://github.com/p-kowadkar/psk-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The /profile view in the Flask app uses ProfileForm for editing email, username,<br>and password. It verifies the current password before updating the database and ensures<br>data adheres to constraints. The view then updates the session and renders profile.html<br>with success or error messages, ensuring secure user profile modifications.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Dealing with tables presented a challenge for me since it was unfamiliar territory.<br>I encountered issues, notably an error on Heroku due to oversight in configuring<br>variables—I forgot to include the database URL and its corresponding value to link<br>it properly with Heroku.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/">https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/psk" target="_blank">Grading</a></td></tr></table>