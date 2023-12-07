<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 10:21:14 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.22.19image.png.webp?alt=media&token=794f5194-bcf4-4242-a0ef-81cd2cb73b68"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index.html page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.23.15image.png.webp?alt=media&token=e7dc77f5-f533-4c87-9ea7-f8a62701de94"/></td></tr>
<tr><td> <em>Caption:</em> <p>index page code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.24.38image.png.webp?alt=media&token=02a95eaf-9a5f-48a7-a1a2-94cff7d21753"/></td></tr>
<tr><td> <em>Caption:</em> <p>Nav SS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.25.12image.png.webp?alt=media&token=eac86d0d-c307-4210-9d1f-aad84d1fa18d"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.26.20image.png.webp?alt=media&token=f1b5d3c5-5b2d-47b5-b097-409b4ce8bf0b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Upload successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.26.35image.png.webp?alt=media&token=e4ce0e68-7d26-43f1-9116-c8e7119815da"/></td></tr>
<tr><td> <em>Caption:</em> <p>csv file check<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.29.45image.png.webp?alt=media&token=01b60c65-6afe-4c95-bec2-ad9aba9ee7ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reading as dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.30.37image.png.webp?alt=media&token=861c67a0-b7cb-4fae-834f-4be529036e52"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updating And Flash Messages<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.32.07image.png.webp?alt=media&token=9b900980-c6f7-4675-9170-2d7724e1c692"/></td></tr>
<tr><td> <em>Caption:</em> <p>List<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.32.20image.png.webp?alt=media&token=f1c76e62-eda0-4314-95aa-3c8dce656b23"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit page with prefilled values.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.32.38image.png.webp?alt=media&token=e20eb23d-376b-44d7-9f81-aa4488322085"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create donation page with empty fields.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.35.39image.png.webp?alt=media&token=508794b6-ff93-4dae-a34f-3be2e7c16482"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.35.51image.png.webp?alt=media&token=7845768e-f23b-4b46-bf63-01ff8349fb0e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.37.12image.png.webp?alt=media&token=84607091-8ee5-40b4-abb3-e28eb0d2718c"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.39.05image.png.webp?alt=media&token=8ea07585-0673-4e6c-8941-17febf9dc931"/></td></tr>
<tr><td> <em>Caption:</em> <p>With filter page of list donation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.39.32image.png.webp?alt=media&token=c7a85228-9cfc-4e32-8310-b97d913f13bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.39.39image.png.webp?alt=media&token=6e7e9abc-d52a-49aa-ac7b-9d37f3714ab0"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.40.08image.png.webp?alt=media&token=9d5ec719-0364-4e0a-99cf-191180877f32"/></td></tr>
<tr><td> <em>Caption:</em> <p>Without filters.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.42.09image.png.webp?alt=media&token=7d221452-9428-48f5-8439-7a434d1520e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.42.24image.png.webp?alt=media&token=c059ec13-4ce1-43cd-bcb6-41e6bd383baa"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.42.32image.png.webp?alt=media&token=e428abb9-f4b5-4796-91a9-def70b58ebd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.42.38image.png.webp?alt=media&token=df182f93-8e9f-437b-b32d-15f7cf5f9699"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.44.09image.png.webp?alt=media&token=77f8e010-0047-4282-82c5-b83a9ac95485"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.44.27image.png.webp?alt=media&token=4a118e2c-4c06-445a-a66f-eb804691b950"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.45.18image.png.webp?alt=media&token=e4a4da5b-53f6-472b-aad6-043d3d8268c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>query<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.47.14image.png.webp?alt=media&token=8dd6262b-278e-4c55-ae6d-099c947e0e58"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.47.28image.png.webp?alt=media&token=d210b8ea-1806-43de-a807-105eb3442154"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.47.33image.png.webp?alt=media&token=c2dd018d-2eb6-4e83-a699-8a68518b1bc2"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.47.41image.png.webp?alt=media&token=272fdce5-0e57-472e-99a6-0bda5171d45b"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.47.47image.png.webp?alt=media&token=8bcc2f2d-a110-4f19-be95-0ccbe4262884"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.49.13image.png.webp?alt=media&token=0b36654f-7070-40bf-b28a-c1d303b78bb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Example<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.49.17image.png.webp?alt=media&token=1c089cfe-df75-4d93-b8a4-245bdd64ff63"/></td></tr>
<tr><td> <em>Caption:</em> <p>Example<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.50.02image.png.webp?alt=media&token=55a9ae51-b32a-4298-bcc1-4e4bdc688ee6"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.51.20image.png.webp?alt=media&token=ea930953-a695-46cf-b2a2-485dcae12447"/></td></tr>
<tr><td> <em>Caption:</em> <p>Example of delete button<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.51.17image.png.webp?alt=media&token=06fef503-0dde-41ba-b9c9-769902effbda"/></td></tr>
<tr><td> <em>Caption:</em> <p>Example of missing Id<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.53.44image.png.webp?alt=media&token=757bd94d-a1a2-446e-984f-cf04a065519e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.53.49image.png.webp?alt=media&token=e475a1a3-dcc3-4195-aab5-fd8af4ced250"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.55.09image.png.webp?alt=media&token=3cd97863-6507-4e06-9b48-50af39ea10d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.55.05image.png.webp?alt=media&token=6eb2f1e4-20df-42db-bfe6-518d85a32bd8"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.57.29image.png.webp?alt=media&token=00910a82-91c3-450b-a10b-77d9a90ccd01"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.57.43image.png.webp?alt=media&token=f55ced38-b39a-48c5-8775-c77a20b1770f"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.58.01image.png.webp?alt=media&token=e7aeb40e-a980-4471-bf12-0379622c7a13"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.58.41image.png.webp?alt=media&token=02ec4c3a-f2bb-4f5c-8dad-25166962fc4d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Without Filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T02.59.15image.png.webp?alt=media&token=30e93fb5-0125-4f7d-bffc-64b3712b32df"/></td></tr>
<tr><td> <em>Caption:</em> <p>With Filters<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.01.18image.png.webp?alt=media&token=d6ad2ca1-7014-4d19-ab55-dc3ab9680056"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.01.25image.png.webp?alt=media&token=85c2ef0d-ad84-4417-b085-8e9add5cac79"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.01.30image.png.webp?alt=media&token=b04bd1a8-e51a-44f8-8dd9-9104afd9eca5"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.02.56image.png.webp?alt=media&token=78008bbe-20f7-49cd-ab25-ca4304d65fe9"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.02.58image.png.webp?alt=media&token=0ae13a87-398a-42fb-90e1-c698715951bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.03.02image.png.webp?alt=media&token=710f30c8-3ea8-43a4-aa1b-b9a5dae230e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.04.39image.png.webp?alt=media&token=8f8cae0e-f7d7-42b0-910f-926bd5974969"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.04.16image.png.webp?alt=media&token=82a03202-3fa1-417e-b795-cf709d2867e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.04.19image.png.webp?alt=media&token=9d0ee68a-c705-46f4-8b03-e2bf74dc0152"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.04.36image.png.webp?alt=media&token=06364804-1463-45da-a42b-549af30159ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.05.59image.png.webp?alt=media&token=b8f90cbd-1d1f-4c2f-a25e-c6f964af8dcd"/></td></tr>
<tr><td> <em>Caption:</em> <p>code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.07.36image.png.webp?alt=media&token=3700bc54-e5b6-41df-b464-ab8b8ed1f1c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.07.39image.png.webp?alt=media&token=0926ed2e-0e71-4738-8009-3504def3e6a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>websi<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.10.02image.png.webp?alt=media&token=4166ae6c-77c5-4288-9d09-99261f2337f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases all passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.10.58image.png.webp?alt=media&token=18d7d8db-503c-4193-9025-17e35e8a45b9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases all passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.11.24image.png.webp?alt=media&token=d17750f3-0f59-4be6-9c67-4aa692180f4d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases all passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.12.04image.png.webp?alt=media&token=fabea061-b842-4403-93ad-e7c63f3d3351"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases all passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>Yes, all test cases passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/18">https://github.com/p-kowadkar/psk-IS601-007/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.14.37image.png.webp?alt=media&token=25cc84bd-f49b-4cdd-bad6-327d5b77f3d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commits<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T03.17.59image.png.webp?alt=media&token=1d02f8e6-7611-4d73-9d82-07266c033c0e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wakatime records (I installed Wakatime on my primary submission device late, and the<br>other devices did not have Wakatime. I have worked for about 7hrs per<br>day during my break, but unfortunately, Wakatime does not have records of Friday<br>- Sunday)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-psk-td-3b8cc33866bd.herokuapp.com/">https://is601-007-psk-td-3b8cc33866bd.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/psk" target="_blank">Grading</a></td></tr></table>