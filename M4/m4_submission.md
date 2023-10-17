<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 9:44:39 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.09.10image.png.webp?alt=media&token=82a649e4-1086-4cad-a4d9-5459cb495614"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.09.33image.png.webp?alt=media&token=072d5642-10ad-411d-bf5c-7fab5a918da1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.10.02image.png.webp?alt=media&token=aa687087-7675-49ab-8663-657a0ad485a7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.10.25image.png.webp?alt=media&token=6820f9dc-43f9-4ccd-9aaa-24ec922f38aa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.19.49image.png.webp?alt=media&token=ddc0740e-3956-477f-926c-993d2a93a6d4"/></td></tr>
<tr><td> <em>Caption:</em> <p>add test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.22.46image.png.webp?alt=media&token=1bfffaca-4ea4-413b-a3a4-825cfa73d8de"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.19.24image.png.webp?alt=media&token=f474fb1f-fb61-4969-9369-6068240266b1"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans_add test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.23.09image.png.webp?alt=media&token=63d5d4b0-5d29-4c0b-b785-2bc0ec89f2ba"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.18.20image.png.webp?alt=media&token=9d6e0957-3882-477f-b8a3-595fc19d5bb8"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.23.29image.png.webp?alt=media&token=23e016b5-fb3b-4ecd-bc7c-8c28c7a1bef3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.17.36image.png.webp?alt=media&token=7fb49b6d-92b9-45e7-8c7e-5e69b6d14eaa"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans_sub test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.23.42image.png.webp?alt=media&token=5a89245e-9266-48af-a67f-9bf2d6fa3934"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.16.57image.png.webp?alt=media&token=e2dac85a-c0bd-4f57-94bd-1a59d8b2b225"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.23.56image.png.webp?alt=media&token=d69fb6ba-757b-4e14-9aa2-e184784e0e51"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.15.48image.png.webp?alt=media&token=b8a1117d-951b-4d4f-a2f8-3b38aa7c4f43"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans_mul test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.24.13image.png.webp?alt=media&token=b09e75f2-5e12-48bc-ad32-26753af2e089"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.15.03image.png.webp?alt=media&token=f9ff9717-752c-466c-824a-0d81d4db0737"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.24.30image.png.webp?alt=media&token=6fe353c1-b335-4fa1-9f7c-a9d91cccd269"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.13.55image.png.webp?alt=media&token=5a98b247-fa3c-4fc2-9505-13a271bf954c"/></td></tr>
<tr><td> <em>Caption:</em> <p>test for ans_div<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-10-17T01.24.44image.png.webp?alt=media&token=959dd116-42f9-4a86-b45e-839a3714d05a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>Greatest challenges in this project were type conversions and error handling. I also<br>learnt the method to create test cases, which was a new experience.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>Test for ans_add, ans_sub, ans_mul, and ans_div were failing due to incorrect call<br>of the ans in main folder, which was further handled. Other parts of<br>this project were handled much more smoothly.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/10">https://github.com/p-kowadkar/psk-IS601-007/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/psk" target="_blank">Grading</a></td></tr></table>