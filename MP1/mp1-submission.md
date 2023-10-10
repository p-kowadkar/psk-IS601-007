<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 9:46:52 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.47.42image.png.webp?alt=media&token=1a28cb26-b8a6-421a-80f7-5613c7b284b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add task code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.48.29image.png.webp?alt=media&token=083338b7-9c98-4bc4-a801-06b3d58e166d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It begins by checking if the <b>name</b>,<br><b>description</b>,<br>     and <b>due</b> parameters are all provided. If any<br>of them are missing<br>     (i.e., one or more is<br>empty), it prints a message ("Missing data<br>     (name, description,<br>or due date)") and returns without adding the<br>     task.<o:p></o:p></span></li><br><br><li class="MsoNormal"><span lang="EN-IN">It then attempts to convert the <b>due</b> string into a<br> <br>   datetime object using a function called <b>str_to_datetime</b>. If the<br> <br>   conversion is successful, it assigns the resulting datetime object to<br>the <b>due</b><br>     field of the <b>task</b> dictionary. If the<br>conversion fails (returns <b>None</b>),<br>     it prints a message ("Invalid<br>due date format") and returns<br>     without adding the task.<o:p></o:p></span></li><br><br><li class="MsoNormal"><span lang="EN-IN">If both the checks in steps 1 and 2 pass, it<br>proceeds to update<br>     the <b>task</b> dictionary with the provided<br><b>name</b>, <b>description</b>,<br>     and the converted <b>due</b> datetime.<o:p></o:p></span></li><br> <li class="MsoNormal"><span<br>lang="EN-IN">It also updates the <b>lastActivity</b> field of the <b>task</b><br>    <br>dictionary with the current date and time using <b>datetime.now()</b>.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">The updated<br><b>task</b> is then appended to a list called <b>tasks</b>.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">Finally, it<br>prints a message ("New task added<br>     successfully") to confirm<br>that the new task was added successfully,<br>     and it<br>calls a <b>save</b> function (which is not defined in this code<br>  <br>  snippet but presumably saves the updated list of tasks).<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.49.59image.png.webp?alt=media&token=c36fdbcc-8f2e-4a92-9760-788e00ab25c4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Process Update task code with logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the provided <b>index</b> is<br>within the valid<br>     range (between 0 and the length<br>of the <b>tasks</b> list). If it's not a<br>     valid<br>index, it prints "Invalid index. Task not found." and<br>    <br>returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the index is valid, it retrieves the task at<br>that index from<br>     the <b>tasks</b> list.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It<br>then displays the existing task data for <b>name</b>, <b>description</b>,<br>    <br>and <b>due</b>.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It prompts the user for new values for <b>name</b>,<br><b>description</b>,<br>     and <b>due</b> using <b>input()</b>.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It calls<br>the <b>update_task</b> function with the updated<br>     values for the<br>task at the given index.<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.51.04image.png.webp?alt=media&token=ad005af5-35e4-4e8e-8b89-6d9c152f7366"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update task code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.51.55image.png.webp?alt=media&token=e547b27d-b708-4069-b8ae-3a9379748f9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the provided <b>index</b> is<br>within the valid<br>     range (between 0 and the length<br>of the <b>tasks</b> list). If it's not a<br>     valid<br>index, it prints "Invalid index. Task not found." and<br>    <br>returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the index is valid, it retrieves the task at<br>that index from<br>     the <b>tasks</b> list.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It<br>updates the task's properties (<b>name</b>, <b>description</b>,<br>     and <b>due</b>) if<br>new values are provided.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It updates the <b>lastActivity</b> field with the<br>current<br>     datetime.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It checks if any of<br>the task properties were updated. If so, it<br>     prints<br>"Task updated successfully." If no changes were provided,<br>     it<br>prints "Task was not updated. No changes provided."<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.52.37image.png.webp?alt=media&token=d471922a-f983-4e31-a823-ce1d87cadeb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function mark_done code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.53.30image.png.webp?alt=media&token=10ba3ab1-6f0d-4734-bb73-518482bfefdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the provided <b>index</b> is<br>within the valid<br>     range (between 0 and the length<br>of the <b>tasks</b> list). If it's not a<br>     valid<br>index, it prints "Invalid index. Task not found." and<br>    <br>returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the index is valid, it retrieves the task at<br>that index from<br>     the <b>tasks</b> list.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It<br>checks if the <b>done</b> property is already not false in<br>   <br> the task. If it is, it prints "Task is already marked as<br>done."<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the task is not marked as done, it records<br>the current<br>     datetime as the value of the <b>done</b><br>property.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It prints "Task marked as done successfully."<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T00.54.08image.png.webp?alt=media&token=7c5ea1fd-9094-4419-876e-059cdfe5bc02"/></td></tr>
<tr><td> <em>Caption:</em> <p>View task Function Code with logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.12.55image.png.webp?alt=media&token=c9604b02-2d88-4f84-a508-8a7fe51d36b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success/ Failure of the given view task.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.13.29image.png.webp?alt=media&token=8bd99af7-040a-4284-888d-a85b1e174162"/></td></tr>
<tr><td> <em>Caption:</em> <p>Required examples<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.14.07image.png.webp?alt=media&token=db9e4aab-7f17-4a49-ba2a-b6da51ac5f9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete_task code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.15.53image.png.webp?alt=media&token=00d03e7b-7ce0-48aa-be40-2b5c1ad95008"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the provided <b>index</b> is<br>within the valid<br>     range (between 0 and the length<br>of the <b>tasks</b> list). If it's not a<br>     valid<br>index, it prints "Invalid index. Task not found." and<br>    <br>returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the index is valid, it removes the task at<br>that index using<br>     the <b>pop</b> method and stores the<br>removed task in the <b>removed_task</b><br>     variable.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It<br>checks if the removal was successful (i.e., if <b>removed_task</b><br>    <br>is not <b>None</b>). If it was successful, it prints "Task deleted<br>  <br>  successfully." If it was not successful, it prints "Task<br>  <br>  deletion failed."<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.16.40image.png.webp?alt=media&token=a1991e42-9ac0-4e1c-9727-9ffce924fdd6"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_incomplete task code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.17.46image.png.webp?alt=media&token=a1f9fb62-a77c-4de6-9c56-a515e9d16131"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing incomplete tasks if in the tasks’ list otherwise a message “No tasks<br>to show”<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It creates a new list <b>_tasks</b> using<br>a list comprehension<br>     to filter tasks from the <b>tasks</b><br>list where the <b>done</b> property<br>     is explicitly <b>False</b>.<o:p></o:p></span></li><br> <li<br>class="MsoNormal"><span lang="EN-IN">It passes the <b>_tasks</b> list to the <b>list_tasks</b><br>    <br>function to print the incomplete tasks.<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.19.02image.png.webp?alt=media&token=f10755f9-b505-4c57-852e-d030619a6fbb"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_overdue_tasks function code with logic comment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.19.31image.png.webp?alt=media&token=51fe9e0f-66a1-4fe6-9a72-b7f29ca4d47c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure condition of overdue task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It creates a new list <b>_tasks</b> using<br>a list comprehension<br>     to filter tasks from the <b>tasks</b><br>list based on the following<br>     conditions:<o:p></o:p></span></li><br> <ul style="margin-top:0in" type="disc"><br><br> <li class="MsoNormal"><span lang="EN-IN">The task should not be marked as done (<b>task['done']</b> is<br><b>False</b>).<o:p></o:p></span></li><br>  <li class="MsoNormal"><span lang="EN-IN">The task should have a <b>due</b> property.<o:p></o:p></span></li><br>  <li<br>class="MsoNormal"><span lang="EN-IN">The <b>due</b> property's value should be less than the<br>   <br>  current datetime (i.e., it's in the past).<o:p></o:p></span></li><br> </ul><br> <li class="MsoNormal"><span lang="EN-IN">It<br>passes the <b>_tasks</b> list to the <b>list_tasks</b><br>     function to<br>print the overdue tasks.<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.20.35image.png.webp?alt=media&token=baf75f98-9ba6-4960-b541-1f9fd9e3ddd5"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_time_remaining function’s code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.28.32image.png.webp?alt=media&token=fd9bc4fe-6a25-4075-80d9-835b77d33227"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failures for due case.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <ol style="margin-top:0in" start="1" type="1"><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the provided <b>index</b> is<br>within the valid<br>     range (between 0 and the length<br>of the <b>tasks</b> list). If it's not a<br>     valid<br>index, it prints "Invalid index. Task not found." and<br>    <br>returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It retrieves the task at the specified index from the<br><b>tasks</b><br>     list.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It checks if the task<br>has a <b>due</b> property. If it doesn't,<br>     it prints<br>"Due date not set for this task." and returns.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">It parses<br>the due date into a datetime object and calculates<br>    <br>the time difference between the due date and the current time.<o:p></o:p></span></li><br> <li class="MsoNormal"><span<br>lang="EN-IN">If the calculated time difference is negative, it indicates<br>    <br>that the task is overdue, so it sets the <b>overdue</b> flag to <b>True</b><br><br>    and takes the absolute value of the time difference.<o:p></o:p></span></li><br><br><li class="MsoNormal"><span lang="EN-IN">It calculates the number of days, hours, minutes, and seconds<br> <br>   from the time difference.<o:p></o:p></span></li><br> <li class="MsoNormal"><span lang="EN-IN">If the task is<br>not overdue, it prints the time remaining in the<br>    <br>format "X days, X hours, X minutes, X seconds remaining." If<br>  <br>  it's overdue, it prints the time overdue in the format "X<br>days, X<br>     hours, X minutes, X seconds overdue."<o:p></o:p></span></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.34.29image.png.webp?alt=media&token=064a3654-abba-4c3b-b3cc-8f3fe152ad68"/></td></tr>
<tr><td> <em>Caption:</em> <p>Some standard tests<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-10T01.35.25image.png.webp?alt=media&token=7de775af-165c-4ce1-9b29-58e0d1f57075"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last saved .json file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div><div>I faced some issues while executing "git push origin MP1-Tracker", I had to<br>check online and speak to classmates to find the below commands, which resolved<br>my issue:</div><div>- nano .git/config</div><div>- sshCommand = ssh -i ~/.ssh/IS601007</div><div>I had to follow this<br>process since I was attempting to submit the project from my laptop, whereas<br>the previous submissions were done on my Tablet. Due to some issues with<br>my tablet, I had to redo the assignment on my laptop, and submit<br>it.<br><div><br></div></div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/psk" target="_blank">Grading</a></td></tr></table>