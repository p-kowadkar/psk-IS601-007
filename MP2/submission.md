<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 7:06:36 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T19.50.22image.png.webp?alt=media&token=11f042b1-5dfb-460a-bc4d-c9f8b0fc49c7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated calculate_cost method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T22.54.21image.png.webp?alt=media&token=c0372014-92e5-4387-9b37-3fb41191d1da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to calculate the cost<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.26.51image.png.webp?alt=media&token=a38371b9-7418-4ab0-ab77-1a625caaa9a7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output in expected format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>For calculating the total cost, I have looped over all the items,<br>and taken the sum of them.<div>2. For the currency formatting, t<span style="color: rgb(227,<br>227, 227); font-family: &quot;Google Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; white-space-collapse: preserve; background-color:<br>rgb(19, 19, 20); user-select: text !important;">he user is asked to enter a total<br>cost with two decimal places.</span><span style="color: rgb(227, 227, 227); font-family: &quot;Google Sans&quot;, &quot;Helvetica<br>Neue&quot;, sans-serif; font-size: 16px; white-space-collapse: preserve; background-color: rgb(19, 19, 20); user-select: text !important;"><br>The input is checked to ensure it is in the correct format before<br>proceeding.</span></div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.35.44image.png.webp?alt=media&token=1e94c860-4f47-477e-8a44-9a0609bdb758"/></td></tr>
<tr><td> <em>Caption:</em> <p>All the required exceptions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>OutOfStockException:</div><div>If the selected item is not in stock, the user is prompted to<br>select another option.</div><div><br></div><div>NeedsCleaningException:</div><div>If the machine needs cleaning, the user is prompted to type<br>"clean" to trigger the cleaning process.</div><div><br></div><div>InvalidChoiceException:</div><div>If the user selects an invalid option, an<br>appropriate message is displayed indicating the stage/category in which the invalid choice was<br>made.</div><div><br></div><div>ExceededRemainingChoicesException:</div><div>If the user exceeds the remaining choices for a particular stage/category, an appropriate<br>message is displayed and the user is moved to the next stage/category.</div><div><br></div><div>InvalidPaymentException:</div><div>If the<br>user's expected cost does not match the calculated cost, an appropriate message is<br>displayed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.40.09image.png.webp?alt=media&token=5b708793-aab3-4e2e-b195-be4d1126549d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Few test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.41.31image.png.webp?alt=media&token=a45ce093-9f1f-4495-a723-45047d949fd5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Next few test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.42.47image.png.webp?alt=media&token=e86d826b-4d1e-48b4-8852-dcb71e878e62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last few test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-27T23.46.26image.png.webp?alt=media&token=2c86baac-728d-4e5e-8c54-5f7b7bcd6339"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases running<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1 - Invalid Stage Exception</div><div>This test verifies that the user cannot add<br>face stencils or extras without first selecting a pumpkin.</div><div><br></div><div>Test 2 - Face stencils<br>are added when in stock</div><div>This test verifies that face stencils can only be<br>added if they are in stock.</div><div><br></div><div>Test 3 - Extras are added when in<br>stock</div><div>This test verifies that extras can only be added if they are in<br>stock.</div><div><br></div><div>Test 4 - Can add up to 3 face stencils of any combination</div><div>This<br>test verifies that the user can add up to 3 face stencils of<br>any combination.</div><div><br></div><div>Test 5 - Can add up to 3 face extras</div><div>This test verifies<br>that the user can add up to 3 face extras.</div><div><br></div><div>Test 6 - Cost<br>must be calculated properly</div><div>This test verifies that the cost is calculated properly based<br>on the user's choices.</div><div><br></div><div>Test 7 - Total Sales</div><div>This test verifies that the total<br>sales are calculated properly.</div><div><br></div><div>Test 8 - Total products variable should properly increment for<br>each purchase</div><div>This test verifies that the total products variable increments properly for each<br>purchase.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/15">https://github.com/p-kowadkar/psk-IS601-007/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I did accidentally uploaded venv file on github, so had to add the<br>venv file to .gitignore, and checkout the branch I was working in. I<br>then had to commit and pull the new changes again!&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T00.04.38image.png.webp?alt=media&token=9bb58c95-74fc-44b4-bdeb-ce4f669c8cee"/></td></tr>
<tr><td> <em>Caption:</em> <p>First successful execution<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-11-28T00.05.57image.png.webp?alt=media&token=5866131f-73b7-4431-9b64-dc727687d62c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Second successful execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/psk" target="_blank">Grading</a></td></tr></table>